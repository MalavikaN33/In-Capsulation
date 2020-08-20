# In-Capsulation
American Express CodeStreet20

The idea is to meet the demand of the people while bridging the gap of shortage as well as avoiding excess of supplies. Forecast fluctuations and divert resources accordingly. Inventory management is the first of Capital Management after all.

## Steps

1. Clone this repository to your local.

2. Open the project in an editor of your preference.

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

    bash
      pip install django
    
4. Run your server

   bash
      python manage.py runserver 
    
   or, the below command if your default python version is python2 use [python3](https://www.python.org/downloads/)

    bash
      python3 manage.py runserver 
    

5. Your server should be up and running now.




## IN-CAPBOT SERVICE AND SLACK
We provided two options for normal User to clarify their doubts. Both of them is discussed below. We have used IBM Service for Chatbot Services

+ IN-CAPBOT
        
    This BOT can be seen as an interactive user-manual. It can answer general queries of the user and helps in navigating through the webite.


## Main Tables

+ USER

  This table contains details of all user.

+ LIST ITEMS

  This stable contains the stock available.

+ TRANSACTIONS

  This table contains details of transactions between supplier and receiver and serves as sales dat

+ Supplier 

  This table contains details of the account payables. The amount due and due date is recored to manage the payables on time. 

  
## Time Series Forecast

Time series forecasting is important because there are so many prediction problems that involve a time component. These problems are neglected because it is this time component that makes time series problems more difficult to handle.

One such problem that can be perfectly solved using time series analysis is inventory management. The time series model used is ARIMA Autoregressive Integrated Moving Average model. The data being used is stationarised by the back end without user interaction and used for forecasting.



*Note : All Data being used is demo data.*
               


   Thank You :)
