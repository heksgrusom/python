import pandas as pd
import matplotlib.pyplot as plt
import sys
import calendar

plt.style.use('ggplot')
plt.rcParams['figure.figsize']=(15,5)

try:
    df = pd.read_csv('comptagevelo2013.csv', delimiter=',',encoding='latin1', parse_dates=['Date'],     dayfirst=True, index_col='Date')
    df[:3]
    df.plot(figsize=(15,10))
except:
    print("Такого файлу не існує!")
    sys.exit()
    
b=pd.read_csv('comptagevelo2013.csv', delimiter=',', encoding='latin1',parse_dates=['Date'],dayfirst=True, index_col='Date')
b['Parc'].plot()

Parc = pd.DataFrame(df["Parc"])
Parc.loc[:,'month'] = Parc.index.month

month = Parc.groupby('month').sum()
month.index=['January','February','March','April','May','June','July','August','September','October','November','December']
month.plot(kind='bar',color='blue')

all_by_month=df.resample('M').sum()


sum_all_by_month = all_by_month.sum(axis=1,skipna = True)
print("Найбільш популярний місяць у велосипедистів у 2013 році це - ", calendar.month_name[sum_all_by_month.idxmax().month])

date = Parc.loc['2013-Jan']
print("У січні найбільша кількість велосипедистів у: ", calendar.day_name[date["Parc"].idxmax().weekday()])

plt.show()
