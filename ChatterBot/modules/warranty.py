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

def getData_InforLaptop():
    with open('data/bill.json','r', encoding="utf8") as bill_file:   
        reader_loader = json.load(bill_file)
    size = len(reader_loader["value_bill"])
    listSerial = []
    listPrice = []
    listName = []
    listDateBuy = []
    listNameCustomer = []
    listAll = []
    for i in range(0, size):
        listSerial.append(reader_loader["value_bill"][i]["serial"])
        listPrice.append(reader_loader["value_bill"][i]["price"])
        listName.append(reader_loader["value_bill"][i]["nameLaptop"])
        listDateBuy.append(reader_loader["value_bill"][i]["dateBuy"])
        listNameCustomer.append(reader_loader["value_bill"][i]["nameCustomer"])

    listAll.append(listSerial)
    listAll.append(listPrice)
    listAll.append(listName)
    listAll.append(listDateBuy)
    listAll.append(listNameCustomer)

    return listAll

def check_Warranty_Serial(userText):
    listAll = getData_InforLaptop()
    listSerial = listAll[0]
    # listPrice = listAll[1]
    # listName = listAll[2]
    # listDateBuy = listAll[3]
    # listNameCustomer = listAll[4]

    size = len(listSerial)
    for i in range(0, size):
        if (listSerial[i] in userText):
            return True
            break
    return False

def get_InforLaptop_serial(userText):
    listAll = getData_InforLaptop()
    listSerial = listAll[0]
    listPrice = listAll[1]
    listName = listAll[2]
    listDateBuy = listAll[3]
    listNameCustomer = listAll[4]
    listInforLap = []

    size = len(listSerial)
    for i in range(0, size):
        if (listSerial[i] in userText):
            listInforLap.append(listSerial[i])
            listInforLap.append(listPrice[i])
            listInforLap.append(listName[i])
            listInforLap.append(listDateBuy[i])
            listInforLap.append(listNameCustomer[i])
            return listInforLap
            break
    return "ko cos gi ca"

def get_warranty_response(my_bot, request):
    userText = request.args.get('msg')

    userText = str.lower(userText)
    SaveUserText = userText
    output = 'unknown'

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
    elif check_Warranty_Serial(userText) == True:
        listInfor = []
        listInfor = get_InforLaptop_serial(userText)
        respon = "sản phẩm " + listInfor[2] + "(mã sản phẩm: " + listInfor[0] + ") " + "của khách hàng " + listInfor[4] + " được mua vào ngày " + listInfor[3]
        if (check_warranty_Date(listInfor[3])):
            return respon + "vẫn còn thời hạn bảo hành ạ"
        else:
            return respon + "đã hết hạn bảo hành ạ"
    elif ('laptop' in userText and 'bị hỏng' in userText) or ('laptop bị hỏng' in userText) or ('liệt phím' in userText) \
            or ('màn hình' in userText) or ('đơ' in userText) or ('lag' in userText) or ('chậm' in userText) or (
            'màn hinh bị' in userText):
        output = 'laptop bị hỏng'
    elif 'laptop' in userText:
        if 'mang qua shop' in userText and 'bị hỏng' in userText:
            output = 'laptop vẫn bị hỏng dù đã sửa chữa'
    elif 'mình yêu nhau' in userText:
        output = 'mình yêu nhau đi'
    elif 'mua' in userText and 'ngày' in userText:
        elif check_warranty_Date(userText) == True:
            output = 'vẫn còn thời hạn bảo hành'
        else:
            output = 'hết thời hạn bảo hành'
    else:
        output = 'unknown'

    print(SaveUserText)
    print('output = ' + output)
    Write_dataJson(output, "value", SaveUserText)

    respon_str = str(my_bot.get_response(output))
    return respon_str
