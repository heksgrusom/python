import math 

def function(n):
    y = 1
    for i in range(2,2*n+1,2):
        y = y * i
    return y
def Z(m):
    if (m == 3):
        print("Can't divide by zero")
    else:
        z = math.sqrt((m+3)/(m-3))
        return z

m = int(input("Enter m (for first function) : "))
n = int(input("Enter n (for second function) : "))

print("Z : " ,Z(m)) # перша функція 
print("function : " ,function(n)) # друга функція
