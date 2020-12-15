import json


def linkOrder(my_bot):
    order = str(my_bot.get_response('confirm_order'))
    file = open('data/orderInfo.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    data = data[len(data) - 1]
    order = order.replace('!product!', data['product'])
    order = order.replace('!name!', data['name'])
    order = order.replace('!phone!', str(data['phone']))
    order = order.replace('!address!', data['address'])
    return order


def order():
    file = open('data/orderInfo.json', 'r', encoding='utf-8')
    data = json.load(file)
    new = {
        "product": "",
        "name": "",
        "phone": "",
        "address": ""
    }
    data.append(new)
    print(data)
    file = open('data/orderInfo.json', 'w', encoding='utf-8')
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
    file = open('data/orderInfo.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    data = data[len(data) - 1]
    for e in data:
        if str(data[e]) == '':
            return e
    return 'confirm_order'


def cancelOrder():
    file = open('data/orderInfo.json', 'r', encoding='utf-8')
    data = json.load(file)
    del data[len(data) - 1]
    file = open('data/orderInfo.json', 'w', encoding='utf-8')
    json.dump(data, file, indent=2)
    file.close()

    return 'order_canceled'


def proccessOrder(userText):
    output = None
    if userText == '1':
        output = 'order_confirmed'
    elif userText == '2':
        output = cancelOrder()
    elif userText == '5':
        output = order()
    elif userText == '7':
        output = 'order_end'

    return output
