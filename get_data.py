import os
import sys
import json
import urllib.request
import pandas as pd
import datetime as dt

api_key = ''
ticker = sys.argv[1]
url_string = 'https://www.alphavantage.co/query?function=' \
             + 'TIME_SERIES_DAILY_ADJUSTED&' \
             + 'symbol=%s&outputsize=full&apikey=%s' % (ticker, api_key)

intraday = 'https://www.alphavantage.co/query?function=' \
    + 'TIME_SERIES_INTRADAY&symbol=%s&outputsize=full&interval=1min&apikey=%s' % (ticker, api_key)

file_to_save = '%s.csv' % (ticker)
with urllib.request.urlopen(url_string) as url:
    data = json.loads(url.read().decode())
    data = data[list(data.keys())[1]]
    df = pd.DataFrame(columns=['Date', 'Open', 'High',
                               'Low', 'Close', 'Adj Close',
                               'Volume', 'Dividend Amount',
                               'Split Coefficient'])
    for k, v in data.items():
        date = dt.datetime.strptime(k, '%Y-%m-%d')
        data_row = [date.date(),
                    float(v['1. open']),
                    float(v['2. high']),
                    float(v['3. low']),
                    float(v['4. close']),
                    float(v['5. adjusted close']),
                    int(v['6. volume']),
                    float(v['7. dividend amount']),
                    float(v['8. split coefficient'])]
        df.loc[-1, :] = data_row
        df.index = df.index + 1
print('Data saved to : %s' % file_to_save)
df.to_csv(file_to_save)
