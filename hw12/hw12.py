import re
import os

def list_files_folders():
    lff = os.listdir()
    return lff

def search(lff):
    no_num = [] ##сюда будем кидать названия фай
    c = 0 ##c - counter
    for file in lff:
        check = re.search('\.[A-Za-z]+', file)
        if check:
            check = re.search('\d', file)
            if not check:
                c = c + 1
                no_num.append(file)
    print('Кол-во файлов без цифр в названии: ', c)
    return no_num

def file_names(no_num):
    print(no_num) ##разделила функции, т. к. это два разных задания, но список делала в прошлой функции, чтобы просто не делать совсем уж лишние действия

def main():
    lff = list_files_folders()
    no_num = search(lff)
    file_names(no_num)

main()
