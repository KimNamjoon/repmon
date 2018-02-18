import random

filename = input("Введите название файла с данными ")
with open("/Users/IM/Desktop" + filename, 'r', encoding = 'utf-8') as f:
    a = f.read()
    b = a.split("\n")
    c = random.choice(b)
    d = c.split(" ")
    print(d [1], end = " ")
for k in d[0]:
    print (".",end = "")
    print("\n")
vocabulary = {d[0]: d[1]}
i = 2
word = input("попытка № 1: ")
while word not in vocabulary.keys():
    print("попытка №",i,end = "")
    word = input(": ")
    i+=1
print("Успех.")
