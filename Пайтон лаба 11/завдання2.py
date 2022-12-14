import matplotlib.pyplot as plt
import numpy as np
import math
import csv
import pandas as pd

myDataFrame = pd.read_csv('comptagevelo2013.csv', parse_dates=['Date'], dayfirst=True)
myDataFrame = myDataFrame.loc[:, ~myDataFrame.columns.str.contains('^Unnamed')]


mostPopularMonthDataFrame = myDataFrame.copy()
mostPopularMonthDataFrame["year_month"] = mostPopularMonthDataFrame["Date"].dt.to_period("M")
mostPopularMonthDataFrame['sum_stats'] = mostPopularMonthDataFrame.sum (axis = 1)
resultMonth = pd.Series(pd.to_datetime(str(pd.DataFrame(mostPopularMonthDataFrame.groupby(["year_month"])["sum_stats"].sum()).sort_values("sum_stats", ascending=True).iloc[0].name))).dt.month_name()[0]
print("The most popular month among cyclists is", resultMonth)

print('\n')

newDataFrame = pd.DataFrame(myDataFrame[["Date", "Maisonneuve_1"]])
print("New dataframe with 1 road:\n", newDataFrame)

mostPopularDayInJanuaryDataFrame = myDataFrame.copy()
mostPopularDayInJanuaryDataFrame["year_month"] = mostPopularDayInJanuaryDataFrame["Date"].dt.to_period("M")
mostPopularDayInJanuaryDataFrame = mostPopularDayInJanuaryDataFrame[mostPopularDayInJanuaryDataFrame.year_month == "2013-01"].set_index("Date").drop("year_month", axis = 1)
mostPopularDayInJanuaryDataFrame['sum_stats'] = mostPopularDayInJanuaryDataFrame.sum (axis = 1)
mostPopularDayInJanuaryDataFrame = mostPopularDayInJanuaryDataFrame.sort_values("sum_stats")
resultDay = mostPopularDayInJanuaryDataFrame.index[len(mostPopularDayInJanuaryDataFrame-1)-1].day
resultDayOfWeek = mostPopularDayInJanuaryDataFrame.index[len(mostPopularDayInJanuaryDataFrame-1)-1].day_name()
print("most popular day in January is", resultDayOfWeek, resultDay)


myPlot1 = pd.read_csv('comptagevelo2013.csv', parse_dates=['Date'], dayfirst=True, index_col='Date')
myPlot1.plot(figsize=(15, 8))
plt.show()
