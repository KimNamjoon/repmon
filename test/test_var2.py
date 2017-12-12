print("Task 1\n")
with open("Ozhegov.txt", "r", encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
for line in text:
    part = line.split("|")#разбиваю строку на куски текста между разделителями, т.к. нам нужная информация в пределах одной части строки
    if len(part[0]) >= 20:
            print(part[0], "|", part[1], "|", part[2], "|", part[3])#сделать так. чтобы не выводились пробелы не получились, возможно, я плохо прогуглила служебные символы
print("\nTask 2\n")
c = 0; #c - counter
with open("Ozhegov.txt", "r", encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
for line in text:
    part = line.split("|")
    if part[2] != "":
        c = c + 1;
print(c)
    
