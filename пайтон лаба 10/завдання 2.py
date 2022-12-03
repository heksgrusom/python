import matplotlib.pyplot as plt 
import numpy as np
import sys


year = list(range(1999,2005))
ua = [131003,450431,333135,385928,400233,441249]
us = [789203,698239,750923,826838,746243,923100]

np.array(year)
np.array(ua)
np.array(us)
    
while True:
    print('---------------')
    print('Натисніть 1 щоб вивести графік')
    print('Натисніть 2 щоб вивести діаграму')
    print('Натисніть 3 щоб вийти з програми')
    print('---------------')
    n = int(input('Введіть число: '))
    
    if n == 1:
        plt.plot(year, ua, label = 'UKR', color = 'orange')
        plt.plot(year, us, label = 'USA', color = 'black')
        plt.title('Counts of school', fontsize = 20)
        plt.xlabel('Year', fontsize = 15, color = 'green')
        plt.ylabel('Indicator', fontsize = 15, color = 'green')
        plt.legend()
        plt.grid(True)
        plt.show()
    elif n == 2:
        country = input('Введіть назву країни: ')
        if country == 'Україна':
            Fig, axes = plt.subplots()
            axes.set_title('School count of Ukraine')
            axes.grid(True)
            axes.bar(year, ua, color = "blue")
            plt.xlabel('Year', fontsize = 15, color = 'green')
            plt.ylabel('Indicator', fontsize = 15, color = 'green')
            plt.show()
        elif country == 'Америка':
            Fig, axes = plt.subplots()
            axes.set_title('School count of United States')
            axes.grid(True)
            axes.bar(year, us, color = "red")
            plt.xlabel('Year', fontsize = 15, color = 'green')
            plt.ylabel('Indicator', fontsize = 15, color = 'green')
            plt.show()
        else:
            print("Такої країни немає")
        
    elif n == 3:
        print('Кінець програми...')
        sys.exit()
    else:
        print("Такого пункту немає")