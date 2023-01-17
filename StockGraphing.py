
import numpy as np
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

def data(dataframe):
    high = list(dataframe['High'])
    low = list(dataframe['Low'])
    opened = list(dataframe['Open'])
    closed = list(dataframe['Close'])

    list_mean = []
    list_indexing = []
    for i in range(len(high)):
        list_indexing.append(high[i])
        list_indexing.append(low[i])
        list_indexing.append(opened[i])
        list_indexing.append(closed[i])

        list_mean.append(np.mean(list_indexing))
        list_indexing.clear()

    return list_mean

stocks = [
    'AAPL',
    'AMZN',
    'GOOG',
    'MSFT',
    'TSLA'
]

# Period = 'ytd' or you can do start = 'YYYY-MM-DD', end = 'YYYY-MM-DD'
def graph_generator(title, starting_date, ending_date):
    for stock in stocks:
        dataframe = data(yf.download(stock, start = starting_date, end = ending_date))
        original_price = dataframe[0]
        current_price = dataframe[-1]
        stock_label = stock + ': ' + str(round((((current_price - original_price) / original_price) * 100), 3)) + '%'

        # Left plot
        plt.subplot(1, 2, 1)
        plt.plot(range(len(dataframe)), dataframe, label = stock_label)
        plt.title(title)
        plt.xlabel('Days')
        plt.ylabel('Value')

        # Right plot
        plt.subplot(1, 2, 2)
        plt.plot([0, 1], [dataframe[0], dataframe[-1]], label = stock_label)
        plt.text(1, dataframe[-1], ('$' + str(round(dataframe[-1]))))
        # plt.xlabel('Presidency Length')
        plt.legend()

    plt.show()

graph_generator("Before Covid: < 2020-03-13", '2009-01-20', '2020-03-13')
graph_generator("During Covid: 2020-03-13 Through 2022-08-01", '2020-03-13', '2022-08-01')
graph_generator("After Covid: > 2022-08-01", '2022-08-01', dt.datetime.now())

# graph_generator("Obama's Presidency", '2009-01-20', '2017-01-20')
# graph_generator("Trump's Presidency", '2017-01-20', '2021-01-20')
# graph_generator("Bidens's Presidency", '2021-01-20', dt.datetime.now())

# Creates a dictionary

# database = {}
# database_nomenclature = [' Mean', ' High', ' Low']
# for i in range(len(database_nomenclature)):
#     stock_name = stock + database_nomenclature[i]
#     database[stock_name] = dataframe[i]
#     stock_name = ''
