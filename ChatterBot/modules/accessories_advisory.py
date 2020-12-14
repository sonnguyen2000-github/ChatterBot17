import json


def accessories_link(my_bot, type, model):
    file = open('data/accessories.json')
    data = json.load(file)
    file.close()
    if model == 'common':
        response = str(my_bot.get_response('loại_phụ_kiện'))
    else:
        response = str(my_bot.get_response('hãng_phụ_kiện'))
    response = response.replace('!type!', type.upper())
    link = '<a href="' + data[type][
        model] + '" target="_blank">' + type.upper() + ('' if model == 'common' else ' ' + model.upper()) + '</a>'
    response = response.replace('!link!', link)
    if '!model!' in response:
        response = response.replace('!model!', model.upper())
    if '!list' in response:
        list = str(data[type].keys()).replace("'", '')
        list = list.replace('dict_keys', '')
        list = list.replace('(', '')
        list = list.replace(')', '')
        list = list.replace('[', '')
        list = list.replace(']', '')
        list = list.replace('common,', '')
        response = response.replace('!list!', list.upper())
    print(response)
    return response


def accessories_analyze(my_bot, userText):
    file = open('data/accessories.json')
    data = json.load(file)
    file.close()
    model = 'common'
    if 'ram' in userText:
        type = 'ram'
    elif 'ssd' in userText:
        type = 'ssd'
    elif 'hdd' in userText:
        type = 'hdd'
    elif 'vga' in userText:
        type = 'vga'
    elif 'sạc' in userText or 'adapter' in userText:
        type = 'adapter'
    elif 'ổ cứng' in userText:
        type = 'hdd'
    elif 'cpu' in userText:
        type = 'cpu'
    for e in data[type]:
        if e in userText:
            model = e
            break
    return accessories_link(my_bot, type, model)


def accessories(my_bot, userText):
    msgAfterWait = ''
    miliseconds = 0
    output = None
    if 'ngu vcl' in userText:
        output = my_bot.get_response('ngu vcl')
    if 'phụ kiện' in userText:
        output = my_bot.get_response('phụ_kiện')
    if 'ram' in userText or 'cpu' in userText \
            or 'sạc' in userText or 'ổ cứng' in userText \
            or 'hdd' in userText or 'ssd' in userText or 'vga' in userText \
            or 'adapter' in userText:
        output = accessories_analyze(my_bot, userText)
    return {"output": str(output), 'timeOut': {'msg': msgAfterWait,
                                               'milisecond': miliseconds}} if output else None
