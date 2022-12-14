import numpy as np
import pandas as pd

mylist = dict()
mylist = {"Day 1" : -10, "Day 2" : 3, "Day 3" : 5, "Day 4" : -5, "Day 5" : 7, "Day 6" : -15}
myDataFrame = pd.DataFrame(mylist, index = ['AverageTempreture', 'Form'])
print(myDataFrame.iloc[0].sum()/6)