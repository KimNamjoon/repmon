s = input()
for i, letter in enumerate(s): #Нумеруем буквы в слове
    if i % 2 == 0 and letter in 'опе' :#Остаток от деления на два нужен, т.к. нумерация идет с нуля в строке
        print(letter)
