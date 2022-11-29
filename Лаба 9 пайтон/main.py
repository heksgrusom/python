import random
import json

dict = {}
def writeToJson():
    try:
        with open("info.json", "w") as write_file:
            json.dump(dict, write_file)
    except FileExistsError:
        print("file not exist")
def readFromJson():
    try:
        with open("info.json", "r") as read_file:
            dict = json.load(read_file)
    except FileNotFoundError:
        print("file not found")
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
for i in range(25):
    str = "Day {}".format(i+1)
    addToDict(str)
while(True):
    x = int(input("Enter number - (1 for show json info) (2 add info) (3 delete info) (4 search info about weather of day) (5 show result info) 6 exit\n"))
    if (x == 1):
        print(dict)
    elif (x == 2):
        readFromJson()
        print("Enter day and temperature : ")
        a = input("Enter day: ")
        b = int(input("Enter temperature: "))
        if a in dict.keys():
            print("There already this key in dict")
        else:
            dict[a] = b
            print("Day added successfully")
        writeToJson()
    elif (x == 3):
        readFromJson()
        a = input("Enter day: ")
        if (a in dict.keys()
        ):
            dict.pop(a)
            print("Day removed successfully")
        else:
            print("There no such")
        writeToJson()
    elif (x == 4):
        readFromJson()
        a = input("Enter day: ")
        if (dict[a] > 0):
            print(a + " : Outside temperature was - {}.It was raining outside".format(dict[a]))
        else:
            print(a + " : Outside temperature was - {}.It was snowing outside".format(dict[a]))
    elif (x == 5):
        readFromJson()
        try:
            with open("result.json", "w") as write_file:
                json.dump(dict, write_file)
        except FileExistsError:
            print("file not exist")
        try:
            with open("result.json", "r") as read_file:
                y = json.load(read_file)
        except FileNotFoundError:
            print("file not found")
        show(y)
    elif (x == 6):
        break
    else:
        print("Wrong number,please re enter")
    
    