import re
try:
    f1 = open('TF10_1.txt','w')
    f1.write('line 113241241' + '\n' + ' 31li424line 242123' + '\n' + ' line141252line241line 3' + '452')
    f1.close()
except FileExistsError:
    print("file already exist")
try:
    f1 = open('TF10_1.txt', 'r')
    s = [line.strip() for line in f1]
    x = ""
    for line in s:
        s = re.sub("\D", "", line)
        x+=s
    f1.close()
except FileNotFoundError:
    print("File not found")
try:
    f2 = open('TF10_2.txt','w')
    i = 0
    for str in x:
        if (i == 10):
            i = 0
            f2.write('\n')
        i+=1
        f2.write(str)
    f2.close()
except FileExistsError:
    print("file already exist")
try:
    f2 = open('TF10_2.txt','r')
    s = [line.strip() for line in f2]
    print(s)            
except FileNotFoundError:
    print("File not found")
          

