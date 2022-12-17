import pandas as pd

Days={'Day 1':(-5,'Snowing'), 'Day 2': (10,'Raining'),'Day 3':( 1,'Raining'),'Day 4':(-7,'Snowing'),'Day 5':(-10,'Snowing'),'Day 6':(-2,'Snowing'),'Day 7':(4,'Raining'),'Day 8':(2,'Raining'),'Day 9':(-1,'Snowing'),'Day 10':(3,'Raining')}

daysTempreture = pd.DataFrame.from_dict(Days, orient='index', columns=['Tempreture','Fall-out'])
print('Tempreture')
print(daysTempreture)
daysTempreturemean=(daysTempreture.groupby('Fall-out').mean())
daysTempreturemean.rename(columns={'Tempreture':'Average Tempreture'}, inplace=True)
daysTempreturemean['Sum Tempreture']=True
daysTempreturemean['Sum Tempreture']=daysTempreture.groupby('Fall-out').sum()['Tempreture']
print('\nMean by Tempreture:')
print(daysTempreturemean)
