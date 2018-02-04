def file_name():
    name = input("Введите название файла с текстом: ")
    return name

def preparing_text(name):
    with open (name, 'r', encoding='utf-8') as text:
        text = text.read().lower()
    for symbol in ['.', ',', ':', ';', '—', '!', '?', '"', '"']:
        if symbol in text:
            text = text.replace(symbol, '')
    words = text.split()
    return words

def vocabulary(words):
    voc = {}
    for word in words:
        if word.endswith('ness'): #нагуглила функцию, но, наверное, можно сделать также, только закодив проверку последних 4 элементов слова, но мне лень
            if word in voc:
                voc[word] += 1
            else:
                voc[word] = 1
    return voc

def counting(voc):
    c = 0
    for word in voc:
        c += voc[word]
    return c

def most_used_word(voc):
    words = sorted(voc, key = voc.get, reverse = True) #спасибо хабру и справочнику по питону за упрощение жихзни
    return words[0]

def summ_up():
    f = file_name()
    print('Кол-во слов на "-ness" в Вашем тексте: ', counting(vocabulary(preparing_text(f))))
    print('Существительное на "-ness", имеющее максимальную частотность: ', most_used_word(vocabulary(preparing_text(f))))

summ_up()
