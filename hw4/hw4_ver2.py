with open("LY_text.txt", encoding='utf-8') as f:
	text = f.read()
lines = text.splitlines() ##список из строк, символы перевода строки отброшены - взято с пары
max = 0 
min = len(lines[0])
for i in enumerate(lines): ##заходим в цикл, чтобы начать проверять строчки
    if len(lines[i[0]]) > max:
        max = len(lines[i[0]])
    if len(lines[i[0]]) < min and len(lines[i[0]]) != 0:
        min = len(lines[i[0]])
a = max/min ## a - answer
print('Самая короткая строка текста меньше самой длинной в', round(a, 2), 'раз.')
