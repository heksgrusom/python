import math 

m = int(input("Enter m : "))

if (m == 3):
    print("Can't divide by zero")
else:
    z = math.sqrt((m+3)/(m-3))
print("Z : " ,z)