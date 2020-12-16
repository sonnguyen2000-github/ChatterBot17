import json

file = open('data/orderInfo.json', 'r', encoding='utf-8')
data = json.load(file)
new = {
    "id":"0",
    "product": "",
    "name": "",
    "phone": "",
    "address": ""
}
data.append(new)
print(data)
file = open('data/orderInfo.json', 'w', encoding='utf-8')
json.dump(data, file, indent=2, ensure_ascii=False)
