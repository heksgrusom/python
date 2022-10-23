import re

f1 = open('TF10_1.txt','w')
f1.write('line 1' + '\n' + ' lineline 2' + '\n' + ' linelineline 3' + '452')
f1.close()
f1 = open('TF10_1.txt', 'r')
s = [line.strip() for line in f1]
x = ""
for line in s:
    s = re.sub(r'[0-9]', '', line)
    x+=s
f2 = open('TF10_2.txt','w')
i = 0
for str in x:
    if (i == 10):
        i = 0
        f2.write('\n')
    i+=1
    f2.write(str)
f2.close()
f2 = open('TF10_2.txt','r')
s = [line.strip() for line in f2]
print(s)            
