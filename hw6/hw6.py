# coding=utf-8
import random
# Эта программа генерирует стихотворение с соблюдением метрической схемы - трехстопный анапест

def adj():
    with open("adj.txt", encoding="utf-8") as f:
        adjective = f.read()
        adjective = adjective.split("\n")
        return random.choice(adjective)

def noun():
    with open("noun.txt", encoding="utf-8") as f:
        nouns = f.read()
        nouns = nouns.split("\n")
        return random.choice(nouns)

def verb_pl():
    with open("verb_pl.txt", encoding="utf-8") as f:
        verbs_pl = f.read()
        verbs_pl = verbs_pl.split("\n")
        return random.choice(verbs_pl)

def direct():
    with open("direction.txt", encoding="utf-8") as f:
        direction = f.read()
        direction = direction.split("\n")
        return random.choice(direction)

def verb_inf():
    with open("inf.txt", encoding="utf-8") as f:
        inf = f.read()
        inf = inf.split("\n")
        return random.choice(inf)

def punctuation():
    with open("punct.txt", encoding="utf-8") as f:
        punct = f.read()
        punct = punct.split("\n")
        return random.choice(punct)
def verse1():
    return adj() + ' ' + adj() + ' ' + noun()

def verse2():
    return verb_pl() + ' ' + direct() + ' ' + verb_inf() + punctuation()

def make_verse():
    print(verse1())
    print(verse2())
    print(verse1())
    print(verse2())

make_verse()



