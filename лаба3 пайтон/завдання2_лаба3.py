def fff(str1,str2):
    for elem in str1:
        k = 0
        l = 0
        l = str1.count(elem)
        for elem1 in str2:
            if elem == elem1:
                k+=1
        if (l == 1 and k == 1):
            print(elem," ")
        
 
 
s1 = input("Enter s1 : ")
s2 = input("Enter s2 : ")

fff(s1,s2)


