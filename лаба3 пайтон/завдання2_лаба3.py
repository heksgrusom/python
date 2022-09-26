def num_symbol(st):
    sym = []
    used = []
    for elem in st:
        if elem in sym:
            sym.remove(elem)
            used.append(elem)
        elif elem not in used:
            sym.append(elem)
    return sym
 
 
s1 = input("Enter s1 : ")
s2 = input("Enter s2 : ")
s1+=s2
for elem in num_symbol(s1):
    print(elem, end=' ')
