import re

def prepare():
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
    parts = re.split('[.!?…]+', text)
    clean_parts = [re.sub('[,:;—–­()&“”«»/*\"\'\n]', '', part) for part in parts]
    return clean_parts

def searching(clean_parts):
    for clean_part in clean_parts:
        words = clean_part.split()
        length = len(words)
        result = []
        if length > 10:
            searching = [result.append(word) for word in words if word.istitle()] #гугл - сила, а я ленивый человек
            print(', '.join(result))

def main():
    clean_parts = prepare()
    searching(clean_parts)

main()

