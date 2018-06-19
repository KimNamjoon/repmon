import re
import collections

def read_file():
    f = open('karenina.xml', encoding='utf-8')
    text = f.read()
    return text

def counting(text):
    w = re.findall('<w>', text)
    ana = re.findall('ana', text)
    average = len(ana) / len(w)
    print("Среднее количество разборов на слово (не округлено): ", average)

def task_1():
    text = read_file()
    counting(text)

def frequency(text):
    freq = {}
    tag  = re.findall('gr="([A-Z]*)', text)
    for word in tag:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def voc(freq):
    txt = open("text.txt", "w", encoding = "utf-8")
    for key in sorted(freq, key=freq.get, reverse=True):
        written = "%s\t%s" % (key, freq[key])
        file = txt.write(written + '\n')
    print('Содержимое словаря распечатано в отдельный файл (не отсортировано по алфавиту)') ##если хотим по алфавиту, то используем for key in sorted(freq.keys())
    txt.close()

def task_2():
    text = read_file()
    freq = frequency(text)
    voc(freq)

def main():    
    task_1()
    task_2()

main()
