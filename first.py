import numpy
import pandas
import requests
import xlsxwriter
import math
from secret import IEX_CLOUD_API_TOKEN
import json

stocks = pandas.read_csv('sp_500_stocks.csv')

symbol='AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url)
print(data.json())