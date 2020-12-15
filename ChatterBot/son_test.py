import json

file = open('data/learned/accessories_learned.json', 'r', encoding='utf-8')
data = json.load(file)
for e in data:
    for ee in data[e]:
        data[e][ee] = 0
file = open('data/learned/accessories_learned.json', 'w')
json.dump(data, file, indent=2, ensure_ascii=False)
print(data)
