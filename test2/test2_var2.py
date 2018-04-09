import re

def file_name():
    name = input('Введите название файла с расширением: ')
    return name

def count_them(name):
    i = 0
    with open (name, 'r', encoding='utf-8') as f:
        text = f.read().split("\n")
    for line in text:
        i += 1
    return i

def write_in_file(i):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(str(i))

def task1():
    name = file_name()
    i = count_them(name)
    write_in_file(i)

def preparing_text(name):
    with open (name, 'r', encoding='utf-8') as f:
        txt = f.read()
return txt

def find_nouns(txt):
    first_match_n = re.search('<w lemma="[a-zA-z]" type="n[kvhx][ef][noþe][g]?[s]?"', txt)
    n_group = first_match_n.group(1)
    print(n_group)


task1()

    
    
