a = int(input("Please enter number a "))
b = int(input("Please enter number b "))
x = 0
while (a < 0):
    a = int(input("Please re enter number a "))
while (b < 0):
    b = int(input("Please re enter number b "))
if (a>b):
    x = 5*a+b
elif (a==b):
    x = -125
else:
    x = (a-5)/b
print("X : ", x)
