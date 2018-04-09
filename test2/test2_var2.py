import re
import collections

##variant_2

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

##def find_nouns(txt):
##    first_match_n = re.search('<w lemma="[a-zA-z]" type="n[kvhx][ef][noþe][g]?[s]?"', txt)
##    n_group = first_match_n.group(1)
##    print(n_group)

def find_them(txt):
    they = re.findall('lemma=".*" type="(.*)"', txt)
    return they

def count_them_2(they):
    count = {}
    c = collections.Counter(they)
    count.update(c)
    return count

##def write_in_dictionary(count):
##    with open('dictionary.txt', 'w', encoding='utf-8') as f2

##def task2():
##    name = file_name()
##    txt = preparing_text(name)
##    they = find_them(txt)
##    count = count_them_2(they)
##    write_in_dictionary(count)
##
        
task1()




    
    
