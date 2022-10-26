a = []

def f(x):
    if len(a) == 0:
        a.append(x)
    else:
        a.insert(0,x)
        a.append(x)
f(1)
f(2)
f(3)
print(a)