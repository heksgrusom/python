a = int(input("Введіть число від 1 до 1000 "))
if (a > 1000 or a < 1):
    a = int(input("Неправильний ввод,введіть число ще раз "))
x = []
i = 0
while(a > i):
    x.append((i+1)*(i+1))
print(x)