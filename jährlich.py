import pandas as pd




inputpath = r"D:\privat_neu\finanz\ausgaben\Exoprte\Toshl export Jan 1, 2020 - Dec 31, 2023.csv"
outputpath = r""
data = pd.read_csv(inputpath)
data = data.rename(columns={'Income amount':'Income', 'Expense amount':'Expense'})



resultstring = ""

data.Date =pd.to_datetime(data.Date)

year = data.Date.dt.year.max()

resultstring += '<h1>Report for year '+str(year) + '<h1>\n'
resultstring += '<h2>Income<h2>\n'

print('bla')

data[['Date', 'income']].groupby(by=[data.Date.dt.year, data.Date.dt.month], as_index=False).income.sum()

