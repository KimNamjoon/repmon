with open('C:/Users/student/Desktop/bts.txt', encoding='utf-8') as f:
    text = f.read()
lines = 0
words = 0
letters = 0
for line in open('C:/Users/student/Desktop/bts.txt'):
    lines += 1
    letters += len(line)
 
    pos = 'out' ##показатель того, в слове мы или же нет
    for letter in line:
        if letter != ' ' and pos == 'out': ##условие того, что мы находим новое слово
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
 
print("Lines:", lines)
print("Words:", words)



##    for line in f:    
##        if line.endswith("\n"):
##            print("Строка кончается на символ переноса строки")
##        else:
##            print("Строка не заканчивается на символ переноса строки")
##        line = line.strip()    # удаляем пробельные символы, в том числе перенос строки, сначала и сконца строки
##        if not line.endswith("\n"):
##            print("Теперь переноса строки точно нет")
##        if line.startswith("Давным-давно"):    # проверяем не начинается ли строка с данной строки
##            print("И жили они долго и счастливо")
##        print(line.count(" "))    # считаем число пробелов в строке
##        for word in line.split():
##            word = word.replace(".", "")
##            if word.isupper() and len(word) > 1:    # слово написано заглавными буквами, .islower() - наоборот
##                print(word, '- быть может аббревиатура?')
##            c=+1;
##        print(c)

##f.write("""Когда мы вернулись с моря, каждый был сам по себе. Словно сговорившись, мы не связывались друг с другом. Только по оставленным на стенах граффити, ярким огням заправочной станции и доносившемуся из старого здания звуку фортепьяно можно было предположить о существовании друг друга. В те времена образ той ночи заново возродился, словно иллюзия. Пламя, словно постепенно исчезающее из зрачков Тэхёна, взгляды, обращённые на меня, словно было сказано что-то невероятное, останавливающая Тэхёна рука Намджуна и я, который не сумел сдержаться и ударил Тэхёна.После провальных поисков сбежавшего Тэхёна, я вернулся в наш дом на берегу, но там никого не было. Разбитое стекло, засохшие пятна крови, разломанное на кусочки печенье напомнило мне о том, что произошло несколько часов назад. Среди всего этого валялась фотография. На ней были мы, улыбающиеся на фоне моря.""")
