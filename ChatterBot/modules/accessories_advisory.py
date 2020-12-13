import json

def accessories_link(my_bot, type, model):
    file = open('G:\Desktop\Document20201\AI\ChatterBot17\ChatterBot\data\accessories.json')
    data = json.load(file)
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
    print(response)
    return response


def accessories_analyze(my_bot, accessories):
    file = open('G:\Desktop\Document20201\AI\ChatterBot17\ChatterBot\data\accessories.json')
    data = json.load(file)
    model = 'common'
    if 'ram' in accessories:
        type = 'ram'
    elif 'ssd' in accessories:
        type = 'ssd'
    elif 'hdd' in accessories:
        type = 'hdd'
    elif 'vga' in accessories:
        type = 'vga'
    elif 'adapter' in accessories:
        type = 'adapter'
    elif 'cpu' in accessories:
        type = 'cpu'
    for e in data[type]:
        if e in accessories:
            model = e
            break
    return accessories_link(my_bot, type, model)


def accessories(my_bot, userText):
    msgAfterWait = ''
    miliseconds = 0
    output = my_bot.get_response('unknown')
    if 'ngu vcl' in userText:
        output = my_bot.get_response('ngu vcl')
    if 'phụ kiện' in userText:
        output = my_bot.get_response('phụ kiện')
    if 'ram' in userText or 'cpu' in userText \
            or 'sạc' in userText or 'ổ cứng' in userText \
            or 'hdd' in userText or 'ssd' in userText or 'vga' in userText:
        output = accessories_analyze(my_bot, userText)
    return {"output": str(output), 'timeOut': {'msg': msgAfterWait, 'miliseconds': miliseconds}}