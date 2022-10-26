c = ['l','l','l','i','i','s','s','s','t']
print(c)
li = []
[li.append(x) for x in c if x not in li]
print(li)