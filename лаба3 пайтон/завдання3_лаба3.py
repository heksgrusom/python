s = input("Enter s : ")
lst = s.split()
for elem in lst:
    if ("o" or "O") in elem:
        print(elem)
