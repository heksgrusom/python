a = []
n = int(input("Enter N : "))
print("Enter {} elements of mass a ".format(n))
for i in range(n):
    a.append(int(input()))
print("positive elements of mass : ")
for i in range(n):
    if (a[i] > 0):
        print(a[i])
