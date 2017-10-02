print("Enter word:")
s = str(input())
a = 'абвгдеёжзийклмнопрстуфхцчшщъьэюя'
if s:
    print(s)

else:
    while len(s)== 0:
        s = str(input())
        print(s)
