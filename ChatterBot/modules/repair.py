import json


def get_repair_response(my_bot, request):
    phuKien = None

    ## Đọc file json
    file = open('data/repair.json')
    data = json.load(file)

    timeOut = 0
    msgAfterWait = ''
    output = None

    userText = request.args.get('msg')
    userText = str.lower(userText)

    if ('hỏng' in userText or 'không nghe được' in userText) and ('âm thanh' in userText or 'tiếng' in userText) or (
            'lỗi loa' in userText):
        output = 'loi_loa'
        phuKien = "thay_the_loa"
    elif ('hỏng' in userText or 'không mở được' in userText or 'màn hình xanh' in userText) and (
            'ổ cứng' in userText or 'ssd' in userText or 'hdd' in userText):
        output = 'loi_o_cung'
        phuKien = "thay_the_o_cung"
    elif 'sửa chữa' in userText:
        output = 'sửa chữa'
    elif 'thay thế' in userText:
        if data["phu_kien"] == "thay_the_o_cung":
            output = 'thay_the_o_cung'
        else:
            output = 'thay_the'
    elif data["phu_kien"] == "thay_the_o_cung":
        if 'ssd' in userText:
            output = 'thay_the_ssd'
            phuKien = 'thay_the_ssd'
        elif 'hdd' in userText and data["phu_kien"]:
            output = 'thay_the_hdd'
            phuKien = 'thay_the_hdd'
    elif data["phu_kien"] == "thay_the_ssd":
        if '128' in userText:
            phuKien = 'ssd_128'
            output = 'thay_the'
        elif '256' in userText:
            phuKien = 'ssd_256'
            output = 'thay_the'
        else:
            output = 'not_have'
    elif data["phu_kien"] == "thay_the_hdd":
        if '500' in userText:
            phuKien = 'hdd_500'
            output = 'thay_the'
        elif '1' in userText and 'tb' in userText:
            phuKien = 'hdd_1000'
            output = 'thay_the'
        else:
            output = 'not_have'
    else:
        if 'hỏng' in userText or 'vấn đề' in userText:
            output = 'vấn đề'

    if phuKien:
        data.update({"phu_kien": phuKien})
        with open('data/repair.json', 'w',
                  encoding='utf-8') as user_dumped:
            json.dump(data, user_dumped, ensure_ascii=False)

    print(data["phu_kien"])
    print(data[data["phu_kien"]])

    if output:
        if output == 'thay_the':
            output = str(my_bot.get_response(str(output)))
            for i in data[data["phu_kien"]]["link"]:
                output = output + "</br>" + i
        else:
            output = str(my_bot.get_response(str(output)))

        return {'output': output, 'timeOut': {'msg': msgAfterWait, 'milisecond': timeOut}}
    else:
        return None
