with open("text.txt", encoding="utf-8") as f:
    text = f.read()
    text.strip(',') 
    text = text.split()
    
a = text
d = {}
for word in a:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for 
