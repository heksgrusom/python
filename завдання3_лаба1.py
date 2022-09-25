rows = int(input("Please enter number "))
if(rows > 9 or rows < 1):
    rows = int(input("Please re enter number "))
b = 1
n = 0
for i in range(rows, n, -1):
    n+=1
    b = n
    for j in range(1, i + 1):
        print(b, end=' ')
        b += 1
    print('\r')
