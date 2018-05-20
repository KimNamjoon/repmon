##воспринимаю формулировку задания как: "название должно быть написано кириллицей, но другие символы допустимы")
import os
import re

def main():
    start_path = '.'
    c = 0 # c - counter
    for dirs in os.walk(start_path):
        directions = dirs[1]
        for item in directions:
            if re.search(r'[A-Za-z]', item) == None:
                c += 1
    print('Кол-во папок с полностью кириллическим названием: ', c)

main()
