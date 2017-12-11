##int a == 0;
## print("!")

x = int(input('Введите число: '))
if (x % 2 == 0 and x != 0):
    print(str(x)+ ' - четное число')
if (x % 2 == 1):
    print(str(x) + ' - нечетное число')
if (x == 0):
    print('Введите другое число')

    with open("/Users/IM/Downloads/quotes.txt", "r", encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
    print("№1\n")
    for line in text:
        quote = line.split("—")
        words = quote[0].split(" ")
        if len(words) <= 9 and len(words[0]) < 5:
            print(quote[0], "–", quote[1])
    print("\n№2\n")
    i = 0
    for line in text:
        quote = line.split("—")
        
        if "разум " in quote[0] or "разум." in quote[0] or "разум," in quote[0] or "разум!" in quote[0] or "разум?" in quote[0]:
            i += 1
            print(quote[0])
    print("\nФраз с вхождением слова РАЗУМ –", i)
    print("\n№3\n")
    wordlist = []
    stream = "-"
    while stream != "":
        stream = input("Введите слово: ")
        wordlist.append(stream)
    for entry in wordlist[:-1]:
        flag = 0
        print("\n", entry, ": \n")
        for line in text:
            quote = line.split("—")
            if entry in quote[0]:
                flag = 1
                print(quote[1], "\t", quote[0])
        if flag == 0:
            print("Вхождения слова", entry, "не было")
