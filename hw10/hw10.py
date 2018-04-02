##опиралась на статью с хабра, т.к. на паре не была, а из конспекта ничего не поняла - https://habrahabr.ru/post/349860/

import re

def file_name():
    name = input("Введите название файла: ") ##разрешение файла тоже надо вводить, т.е. вводимое название должно выглядеть как, например, "filename.txt"
    return name

def preparing_text(name):
    with open (name, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def searching(text):
    matching = re.search(r'Часовой пояс[^\n]+\n([^\n]+\n)', text)
    time_zone_group = matching.group(1)
    return time_zone_group

def timezone(time_zone_group):
    findall = re.findall('>([^<>]+)<', time_zone_group)
    time_zone = ''.join(findall)
    return time_zone

def write_in_file(time_zone):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(time_zone)

def main_func():
    name = file_name()
    text = preparing_text(name)
    time_zone_group = searching(text)
    time_zone = timezone(time_zone_group)
    write_in_file(time_zone)

main_func()
