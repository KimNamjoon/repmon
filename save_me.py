##int a == 0;
## print("!")

x = int(input('Введите число: '))
if (x % 2 == 0 and x != 0):
    print(str(x)+ ' - четное число')
if (x % 2 == 1):
    print(str(x) + ' - нечетное число')
if (x == 0):
    print('Введите другое число')
