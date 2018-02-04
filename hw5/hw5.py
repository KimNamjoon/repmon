w = 'слово' #w - word
while len(w) < 0:
    w = input ('Введите слово: ')
    if len(w) > 5:
        with open("file.txt", "a", encoding="utf-8") as f:
            f.write(w)
            f.write("\n")
