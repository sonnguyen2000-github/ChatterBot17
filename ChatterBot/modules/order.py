import json


def orderInfo(my_bot, userText):
    if not checkCustomerInfo(my_bot, userText):
        return customerInfo(my_bot, userText)
    return productInfo(my_bot, userText)


def productInfo(my_bot, userText):


def customerInfo(my_bot, userText):


def checkCustomerInfo(my_bot, userText):
    file = open('data/orderInfo.json', encoding='utf-8')
    data = json.load(file)
    if data['']


def confirmOrder(my_bot, userText):


def changeOrder(my_bot, userText):


def cancelOrder(my_bot, userText):


def proccessOrder(my_bot, userText):
    msgAfterWait = ''
    miliseconds = 0
    output = None
    key = ''
    if 'rồi' in userText or 'chọn được' in userText:
        key = 'chọn_được'
    if ('mua' in userText and 'online' in userText) or 'đặt' in userText:
        output = orderInfo(my_bot, userText)
    if userText == '1':
        output = confirmOrder(my_bot, userText)
    if userText == '0':
        output = changeOrder(my_bot, userText)
    if userText == '2':
        output = cancelOrder(my_bot, userText)

    return {"output": str(output), 'timeOut': {'msg': msgAfterWait,
                                               'milisecond': miliseconds}} if output else None
