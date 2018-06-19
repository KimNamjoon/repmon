import os
import re
import csv

def file_names():
    path = '.\\news'
    names = os.listdir(path)
    return names

def reading(names):
    path = '.\\news'
    os.chdir(path)
    t = ''
    for name in names:
        with open(name, 'r', encoding='windows-1251') as f:
            t += f.read()
    return t
##
##def task1(t):
##   ## with open('names.csv', 'w', newline='') as csvfile:
##   ##     fieldnames = ['doc_id\t', 'title\t',  ]
##    t = t.split("\n")
##    with open("result.txt", "w", encoding="utf-8") as f:
##        f.write ("doc_id\ttitle\tauthor\tcreated\ttopic\ttagging\n")

def task2(t):
    short = re.findall('lex=\"[А-Я][А-Я\-]+', t)
    short = collections.Counter(short)
    with open('result_task2.txt', 'w', encoding='utf-8') as f:
        for key, value in short.items():
            f.write(key[5:])
            f.write('\t')
            f.write(str(value))
            f.write ('\n')
            
def main():
    names = file_names()
    t = reading(names)
    task2(t)

main()

