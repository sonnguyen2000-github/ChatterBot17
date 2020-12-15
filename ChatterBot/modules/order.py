import json


def order(my_bot):
    if checkCustomerInfo():
        return customerInfo(my_bot, checkCustomerInfo())
    return productInfo(my_bot)


def productInfo(my_bot):
    return str(my_bot.get_response('lưu_thông_tin_sp'))


def customerInfo(my_bot, info):
    key = ''
    if info == 'name':
        key = 'lưu_thông_tin_hoten'
    elif info == 'phone':
        key = 'lưu_thông_tin_sdt'
    elif info == 'address':
        key = 'lưu_thông_tin_diachi'
    return str(my_bot.get_response(key))


def checkCustomerInfo():
    file = open('data/orderInfo.json', encoding='utf-8')
    data = json.load(file)
    file.close()
    for e in data:
        if e != 'product' and str(data[e]) == '':
            return e
    return None


def confirmOrder(my_bot):
    return my_bot.get_response('confirm_order')


def changeOrder(my_bot):
    file = open('data/orderInfo.json', 'r+', encoding='utf-8')
    data = json.load(file)
    for e in data:
        data[e] = ''
    json.dump(data, file)
    file.close()

    return order(my_bot)


def cancelOrder():
    file = open('data/orderInfo.json', 'r+', encoding='utf-8')
    data = json.load(file)
    data['product'] = ''
    json.dump(data, file)
    file.close()

    return 'ĐƠn hàng đã được huỷ'


def proccessOrder(my_bot, userText):
    msgAfterWait = ''
    miliseconds = 0
    output = None
    key = ''
    if 'rồi' in userText or 'chọn được' in userText:
        key = 'chọn_được'
    if ('mua' in userText and 'online' in userText) or 'đặt' in userText:
        output = order(my_bot)
    if userText == '1':
        output = confirmOrder(my_bot)
    if userText == '0':
        output = changeOrder(my_bot)
    if 'huỷ' in userText:
        output = 'cancel_order'
    if userText == '2':
        output = cancelOrder()

    return {"output": str(output), 'timeOut': {'msg': msgAfterWait,
                                               'milisecond': miliseconds}} if output else None
