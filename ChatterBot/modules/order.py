import json


def linkOrder(my_bot):
    order = str(my_bot.get_response('confirm_order'))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    file.close()
    data = data[len(data) - 1]
    order = order.replace('!product!', data['product'])
    order = order.replace('!name!', data['name'])
    order = order.replace('!phone!', str(data['phone']))
    order = order.replace('!address!', data['address'])
    return order


def changePersonal():
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    if len(data) > 0:
        change = data[len(data) - 1]
        for e in change:
            if e != 'product':
                data[len(data) - 1][e] = ''
        file = open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'w', encoding='utf-8-sig')
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()

    return customerInfo(checkOrderInfo())


def newOrder():
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    new = {
        "product": "",
        "name": "",
        "phone": "",
        "address": ""
    }
    if len(data) > 0:
        new = {
            "product": "",
            "name": data[len(data) - 1]['name'],
            "phone": data[len(data) - 1]['phone'],
            "address": data[len(data) - 1]['address']
        }
    data.append(new)
    print(data)
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'w', encoding='utf-8-sig') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()

    return customerInfo(checkOrderInfo())


def customerInfo(info):
    key = info
    if info == 'name':
        key = 'save_name'
    elif info == 'phone':
        key = 'save_phone'
    elif info == 'address':
        key = 'save_address'
    elif info == 'product':
        key = 'save_product_link'
    return key


def checkOrderInfo():
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    file.close()
    data = data[len(data) - 1]
    for e in data:
        if str(data[e]) == '':
            return e
    return 'confirm_order'


def cancelOrder():
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    if len(data) > 0:
        del data[len(data) - 1]
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//orderInfo.json', 'w', encoding='utf-8-sig') as file:
            json.dump(data, file, indent=2)
        file.close()

    return 'order_canceled'


def proccessOrder(userText):
    output = 'unknown'
    if userText == '1':
        output = 'order_confirmed'
    elif userText == '2':
        output = cancelOrder()
    elif userText == '0':
        output = changePersonal()
    elif userText == '5':
        output = newOrder()
    elif userText == '7':
        output = 'order_end'

    return output
