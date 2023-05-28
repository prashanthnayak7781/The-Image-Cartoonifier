Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import numpy as np
... 
... # Read in the CSV file and create a pandas dataframe
... df = pd.read_csv('stock_prices.csv')
... 
... # Convert the 'Date' column to a datetime datatype
... df['Date'] = pd.to_datetime(df['Date'])
... 
... # Set the 'Date' column as the index
... df.set_index('Date', inplace=True)
... 
... # Calculate the average closing price for each month using numpy
... avg_closing_price_monthly = df['Close'].resample('M').mean()
... 
... # Print the results
... print(avg_closing_price_monthly)
