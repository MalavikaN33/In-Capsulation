from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm
from django.http import HttpResponse
import csv
from django.contrib import messages
from .forms import IssueForm, ReceiveForm
from .forms import ReorderLevelForm
from .forms import suppliercreateform,updatesupplier
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    title = 'Welcome: We are In-capsulation'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)



@login_required
def list_item(request):
    header = 'List of Items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    form = StockSearchForm(request.POST or None)
    if request.method == 'POST':
        category = form['category'].value()
        queryset = Stock.objects.filter(
            item_name__icontains=form['item_name'].value()
        )

        if (category != ''):
            queryset = queryset.filter(category_id=category)

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response
        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "list_item.html", context)


@login_required
def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('/list_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('/list_item')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/list_item')
    return render(request, 'delete_items.html')


def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
        # "title": queryset.item_name,
        "queryset": queryset,
    }
    return render(request, "stock_detail.html", context)


def issue_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.receive_quantity = 0
        #instance.quantity -= instance.issue_quantity
        instance.issue_by = str(request.user)
        messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(
            instance.item_name) + "s now left in Store")
        instance.save()

        return redirect('/stock_detail/' + str(instance.id))
    # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": 'Issue ' + str(queryset.item_name),
        "queryset": queryset,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "add_items.html", context)


def receive_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.issue_quantity = 0
        instance.quantity += instance.receive_quantity
        instance.receive_by = str(request.user)
        #instance.issue_by = instance.issue_by
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(
            instance.item_name) + "s now in Store")

        return redirect('/stock_detail/' + str(instance.id))
    # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": 'Receive ' + str(queryset.item_name),
        "instance": queryset,
        "form": form,
        "username": 'Receive By: ' + str(request.user),
    }
    return render(request, "add_items.html", context)


def reorder_level(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(
            instance.reorder_level))
        return redirect("/list_item")
    context = {
        "instance": queryset,
        "form": form,
    }
    return render(request, "add_items.html", context)


@login_required
def list_history(request):
    header = 'TRANSACTIONS'
    #form = StockSearchForm(request.POST or None)
    queryset = StockHistory.objects.all()

    context = {
        "header": header,
        "queryset": queryset,
    }
    form = StockSearchForm(request.POST or None)
    if request.method == 'POST':
        category = form['category'].value()
        queryset = StockHistory.objects.filter(
            item_name__icontains=form['item_name'].value()
        )

        if (category != ''):
            queryset = queryset.filter(category_id=category)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Stock History.csv"'
            writer = csv.writer(response)
            writer.writerow(
                ['CATEGORY',
                 'ITEM NAME',
                 'QUANTITY',
                 'ISSUE QUANTITY',
                 'RECEIVE QUANTITY',
                 'RECEIVE BY',
                 'ISSUE BY',
                 'LAST UPDATED'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                    [stock.category,
                     stock.item_name,
                     stock.quantity,
                     stock.issue_quantity,
                     stock.receive_quantity,
                     stock.receive_by,
                     stock.issue_by,
                     stock.last_updated])
            return response

        context = {
            "form": form,
            "header": header,
            "queryset": queryset,
        }
    return render(request, "list_history.html", context)

def Arima(request):
    global model_fit
    import pandas as pd
    import numpy
    from pandas import datetime
    from pandas.plotting import autocorrelation_plot
    from pandas import DataFrame
    import statsmodels
    from statsmodels.tsa.arima_model import ARIMA
    from matplotlib import pyplot
    from sklearn.metrics import mean_squared_error
    import statsmodels.api as sm

    def parser(x):
        return datetime.strptime(x, '%d-%m-%Y')

    df = pd.read_csv("/Users/shriram/PycharmProjects/AMEXCODESTREET/set.csv", index_col=0, parse_dates=[0], header=0, squeeze=True, date_parser=parser)
    series = df[df['item'] == 1]
    series = series.drop('item', axis=1)

    from statsmodels.tsa.stattools import adfuller
    from matplotlib import pyplot as plt
    def test_stationarity(timeseries, window=12, cutoff=0.01, count=0):

        # Determing rolling statistics
        rolmean = timeseries.rolling(window).mean()
        rolstd = timeseries.rolling(window).std()

        # Perform Dickey-Fuller test:
        # print('Performing Dickey-Fuller Test:')
        dftest = adfuller(timeseries, autolag='AIC', maxlag=20)
        dfoutput = pd.Series(dftest[0:4],
                             index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput['Critical Value (%s)' % key] = value
        pvalue = dftest[1]
        if pvalue >= cutoff:
            count += 1
            # print("differentiating")
            first_diff = series.sales - series.sales.shift(1)
            first_diff = first_diff.dropna(inplace=False)
            test_stationarity(first_diff, window=12)
        return (count)


    i = test_stationarity(series['sales'])
    # print("I =",i)


    def difference(dataset, interval=1):
        diff = list()
        for i in range(interval, len(dataset)):
            value = dataset[i] - dataset[i - interval]
            diff.append(value)
        return numpy.array(diff)

    # invert differenced value
    def inverse_difference(history, yhat, interval=1):
        return yhat + history[-interval]

    sum_p = 0
    sum_e = 0
    c = 0
    X = series.values
    size = int(len(X) * 0.6)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = sm.tsa.statespace.SARIMAX(history, trend='n', order=(6, i, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        # print('predicted=%d, expected=%d' % (yhat, obs))
        '''sum_p+=yhat
        sum_e+=obs
        c+=1
        if c==30:
            print('predicted=%d, expected=%d' % (sum_p, sum_e))
            c=0
            sum_p=0
            sum_e=0'''
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)

    X = series.values
    days_in_year = 365
    differenced = difference(X, days_in_year)

    start_index = len(differenced)
    end_index = start_index + 6
    forecast = model_fit.predict(start=start_index, end=end_index)
    # invert the differenced forecast to something usable
    history = [x for x in X]
    day = 1
    lst=list()
    for yhat in forecast:
        inverted = inverse_difference(history, yhat, days_in_year)
        print('Day %d: %d' % (day, inverted))
        lst.append(int(inverted))
        history.append(inverted)
        day += 1
    for i in lst:
        print(i)
    return render(request,"forecast.html",{'lst':lst})

def supplier_list(request):
    header = 'Supplier'
    form = suppliercreateform(request.POST or None)
    queryset = supplier.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
        "form": form,
    }
    return render(request, "supplier_list.html", context)


def add_supplier(request):
    form = suppliercreateform(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('/supplier_list')
    context = {
        "form": form,
        "title": "Add Supplier",
    }
    return render(request, "add_supplier.html", context)

def update_supplier(request, pk):
    queryset = supplier.objects.get(id=pk)
    form = updatesupplier(instance=queryset)
    if request.method == 'POST':
        form = updatesupplier(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/supplier_list')

    context = {
        'form':form
    }
    return render(request, 'add_supplier.html', context)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user1 = Userinfo.objects.filter(username=username)
        if user1:
            messages.error(request, "This username is not valid. Please try with other username.")
            return redirect('home')

        if len(username)>10 :
            messages.error(request, "Username length must be less than 10 character.")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain character or numbers.")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password not matched. Please try again")
            return redirect('home')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        userinformation = Userinfo(username=username, firstname=fname,lastname=lname, email=email, password=pass1,phone=phone)
        userinformation.save()
        messages.success(request,"You have successfully registered in this Blog. Welcome!")
        return redirect('home')
    else:
        return HttpResponse("404 not Found")


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In. Welcome!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials. Please try again")
            return redirect('home')
    messages.error(request, "You need to Login to access this page")
    return redirect('home')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out. Visit after website again!. If you have any issue then post it on contact tab. Thankyou!")
    return redirect('home')

