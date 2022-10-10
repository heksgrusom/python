n = 7
a = [ [0]*n for i in range(n) ]
for i in range(0,7):
    for j in range(0,7):
        a[i][j]= n
    n-=1
for i in range(7):
    for j in range(7):
        print(a[i][j], end = " ")
    print()
