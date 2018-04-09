import re

def read_txt():
    with open('vikings.html', 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def replace_words(text):
    replacing = re.sub(r'([^А-Яа-я])викинг((?:а(?:м(?:и)))|((?:о)?в)?|у|и[^А-Яа-я])', r'\1бурундук\2', text)
    replaced = re.sub(r'([^А-Яа-я])Викинг((?:а(?:м(?:и)))|((?:о)?в)?|у|и[^А-Яа-я])', r'\1Бурундук\2', replacing)
    return replaced

def write_in_file(replaced):
    with open('chip_and_dale.txt', 'w', encoding='utf-8') as f:
        f.write(replaced)

def main_func():
    text = read_txt()
    replaced = replace_words(text)
    write_in_file(replaced)

main_func()
