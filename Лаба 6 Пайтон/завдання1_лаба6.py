import random

dict = {}

for i in range(31):
    str = "Day {}".format(i+1)
    dict[str]= random.randrange(-20,30)
for key, value in dict.items():
    if value > 0:
        print(key + " : it was raining outside")
    else:
        print(key + " : it was snowing outside")
    