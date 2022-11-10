import random

dict = {}

def addToDict(str):
    if str in dict.keys():
        print("There already this key in dict")
    else:
        dict[str]= random.randrange(-20,30)
def show(dictionary):
    for key,value in dictionary.items():
        if value > 0:
            print(key + " : Outside temperature was - {}.It was raining outside".format(value))
        else:
            print(key + " : Outside temperature was - {}.It was snowing outside".format(value))
for i in range(31):
    str = "Day {}".format(i+1)
    addToDict(str)
show(dict)
    

    
