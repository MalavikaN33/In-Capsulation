from django import forms

from .models import Stock

from .models import supplier

class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']

   def clean_category(self):
       category = self.cleaned_data.get('category')
       if not category:
           raise forms.ValidationError('This field is required')


       return category

   def clean_item_name(self):
       item_name = self.cleaned_data.get('item_name')
       if not item_name:
           raise forms.ValidationError('This field is required')
       for instance in Stock.objects.all():
           if instance.item_name == item_name:
               raise forms.ValidationError(str(item_name) + ' is already created')
       return item_name

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
      model = Stock
      fields = ['category', 'item_name']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity', 'receive_by']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity','issue_by']

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']

class suppliercreateform(forms.ModelForm):
   class Meta:
     model = supplier
     fields = ['supplier_name','supplier_business','supplier_email','due_date','amount','status']

class updatesupplier(forms.ModelForm):
	class Meta:
		model = supplier
		fields = ['status']