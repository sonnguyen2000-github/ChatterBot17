import json
import time
from datetime import date


def Write_dataJson(output, value, userText):
    with open('data/reader_user.json', 'r',
              encoding="utf8") as user_dumped:
        reader_loader = json.load(user_dumped)
        entry = {output: userText}
        reader_loader["value"].append(entry)

    with open('data/reader_user.json', 'w', encoding="utf8") as user_dumped2:
        json.dump(reader_loader, user_dumped2, ensure_ascii=False, indent=1)

    with open('data/reader_user.json', 'r', encoding="utf8") as user_dumped3:
        reader_loader2 = json.load(user_dumped3)
        print(reader_loader2)


def check_warranty(str):
    today = date.today()
    today = today.strftime('%d/%m/%Y')
    list_today = today.split('/')

    list2 = str.split(' ')
    listDateWarranty = [int(s) for s in str.split() if s.isdigit()]
    lengthWarranty = len(listDateWarranty)
    if 'năm ngoái' in str or 'hôm qua' in str or 'hôm kia' in str or 'hôm trước' in str \
            or 'tuần trước' in str or 'tuần trước' in str or 'tháng trước' in str:
        return True
    elif lengthWarranty == 0:
        return False
    elif lengthWarranty == len(list_today):
        for i in range(0, lengthWarranty):
            if (int(listDateWarranty[lengthWarranty - 1 - i])) > (int(list_today[lengthWarranty - 1 - i])):
                return False
                break
    return True


def check_in(output, str):
    listStr = str.split(' ')
    for i in listStr:
        if output == i:
            return True
    return False


def get_warranty_response(my_bot, request):
    userText = request.args.get('msg')

    userText = str.lower(userText)
    SaveUserText = userText
    output = None

    if 'xin chào' in userText or 'chào' in userText:
        output = 'xin chào'
    elif 'bảo hành' in userText:
        output = 'bảo hành'
        if 'bao giờ' in userText or 'bao giờ hết hạn bảo hành' in userText or 'vẫn còn' in userText or 'check' in userText:
            output = 'kiểm tra'
        elif 'muốn' in userText or 'muốn bảo hành' in userText:
            output = 'muốn bảo hành'
        elif check_in("muốn", userText):
            return str(my_bot.get_response(output))
        elif 'sản phẩm này' in userText:
            output = 'thông tin bảo hành sản phẩm'
        elif 'bảo hành theo' in userText:
            output = 'bảo hành theo số serial'
    elif ('laptop' in userText and 'bị hỏng' in userText) or ('laptop bị hỏng' in userText) or ('liệt phím' in userText) \
            or ('màn hình' in userText) or ('đơ' in userText) or ('lag' in userText) or ('chậm' in userText) or (
            'màn hinh bị' in userText):
        output = 'laptop bị hỏng'
    elif 'laptop' in userText:
        if 'mang qua shop' in userText and 'bị hỏng' in userText:
            output = 'laptop vẫn bị hỏng dù đã sửa chữa'
    elif 'mình yêu nhau' in userText:
        output = 'mình yêu nhau đi'
    elif check_warranty(userText) == True:
        output = 'vẫn còn thời hạn bảo hành'
    elif check_warranty(userText) == False:
        output = 'hết thời hạn bảo hành'
    else:
        output = 'unknown'

    print(SaveUserText)
    print('output = ' + output)
    Write_dataJson(output, "value", SaveUserText)

    return {'output': str(my_bot.get_response(output)),
            'timeOut': {'msg': '', 'milisecond': 0}} if output else None
