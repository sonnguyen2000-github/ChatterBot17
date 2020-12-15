import json

def Write_InforBuyLaptop():  
    with open('C://Users//Admin//Desktop//ChatterBot17/ChatterBot//data//demand_infor.json', 'r', encoding = 'utf-8-sig') as json_file :
         data = json.load(json_file)
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8-sig') as json_file :
         user = json.load(json_file)

    if user['laptop'] == 'asus' and user['purpose'] == 'học tập - văn phòng':
        data['demand_info'].append({"laptop_name": "asus", "purpose": "học tập - văn phòng"})
    if user['laptop'] == 'asus' and user['purpose'] == 'đồ họa - kĩ thuât':
        data['demand_info'].append({"laptop_name": "asus", "purpose": "đồ họa - kĩ thuât"})
    if user['laptop'] == 'asus' and user['purpose'] == 'gaming':
        data['demand_info'].append({"laptop_name": "asus", "purpose": "gaming"})

    if user['laptop'] == 'dell' and user['purpose'] == 'học tập - văn phòng':
        data['demand_info'].append({"laptop_name": "dell", "purpose": "học tập - văn phòng"})
    if user['laptop'] == 'dell' and user['purpose'] == 'đồ họa - kĩ thuât':
        data['demand_info'].append({"laptop_name": "dell", "purpose": "đồ họa - kĩ thuât"})
    if user['laptop'] == 'dell' and user['purpose'] == 'gaming':
        data['demand_info'].append({"laptop_name": "dell", "purpose": "gaming"})

    if user['laptop'] == 'macbook' and user['purpose'] == 'học tập - văn phòng':
        data['demand_info'].append({"laptop_name": "macbook", "purpose": "học tập - văn phòng"})
    if user['laptop'] == 'macbook' and user['purpose'] == 'đồ họa - kĩ thuât':
        data['demand_info'].append({"laptop_name": "macbook", "purpose": "đồ họa - kĩ thuât"})
    if user['laptop'] == 'macbook' and user['purpose'] == 'gaming':
        data['demand_info'].append({"laptop_name": "macbook", "purpose": "gaming"})
    
    if user['laptop'] == 'lenovo' and user['purpose'] == 'học tập - văn phòng':
        data['demand_info'].append({"laptop_name": "lenovo", "purpose": "học tập - văn phòng"})
    if user['laptop'] == 'lenovo' and user['purpose'] == 'đồ họa - kĩ thuât':
        data['demand_info'].append({"laptop_name": "lenovo", "purpose": "đồ họa - kĩ thuât"})
    if user['laptop'] == 'lenovo' and user['purpose'] == 'gaming':
        data['demand_info'].append({"laptop_name": "lenovo", "purpose": "gaming"})

    if user['laptop'] == 'hp' and user['purpose'] == 'học tập - văn phòng':
        data['demand_info'].append({"laptop_name": "hp", "purpose": "học tập - văn phòng"})
    if user['laptop'] == 'hp' and user['purpose'] == 'đồ họa - kĩ thuât':
        data['demand_info'].append({"laptop_name": "hp", "purpose": "đồ họa - kĩ thuât"})
    if user['laptop'] == 'hp' and user['purpose'] == 'gaming':
        data['demand_info'].append({"laptop_name": "hp", "purpose": "gaming"})

    if user['laptop'] == 'acer' and user['purpose'] == 'học tập - văn phòng':
        data['demand_info'].append({"laptop_name": "acer", "purpose": "học tập - văn phòng"})
    if user['laptop'] == 'acer' and user['purpose'] == 'đồ họa - kĩ thuât':
        data['demand_info'].append({"laptop_name": "acer", "purpose": "đồ họa - kĩ thuât"})
    if user['laptop'] == 'acer' and user['purpose'] == 'gaming':
        data['demand_info'].append({"laptop_name": "acer", "purpose": "gaming"})

    with open('C://Users//Admin//Desktop//ChatterBot17/ChatterBot//data//demand_infor.json','w', encoding = 'utf-8-sig') as file :
            json.dump(data, file, ensure_ascii = False) 

def get_laptop_response(my_bot, request):
    check = False
    timeOut = 10000
    msgAfterWait = 'Bạn đã chọn được mẫu nào chưa ạ?'
    userText = request.args.get('msg')
    output = None
    userText = str.lower(userText)
    number = []
    
    Write_InforBuyLaptop()

    if 'asus' in userText:
       user = { 'laptop': 'asus',
                'price': 0,
                'purpose': ''
       }
       with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user,user_dumped,ensure_ascii = False) 
 
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
    
    if n != 0 and 'triệu' in userText:
        user_loaded.update({ 'price': number[0] })
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if int(user_loaded['price']) > 0 and int(user_loaded['price']) < 10 and user_loaded['laptop']== 'asus':
            output = 'asus_10_triệu'
            check = True
        elif int(user_loaded['price']) >= 10 and int(user_loaded['price']) <= 15 and user_loaded['laptop']== 'asus':
            output = 'asus_15_triệu'
            check = True
        elif int(user_loaded['price']) > 15 and int(user_loaded['price']) <= 20 and user_loaded['laptop']== 'asus':
            output = 'asus_20_triệu'
            check = True
        elif int(user_loaded['price']) > 20 and int(user_loaded['price']) <= 25 and user_loaded['laptop']== 'asus':
            output = 'asus_25_triệu'
            check = True
    
    if 'dell' in userText:
       
       user = { 'laptop': 'dell',
                'price': 0,
                'purpose': ''
       }
       with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user,user_dumped,ensure_ascii = False)             
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
    if n != 0 and 'triệu' in userText:
        user_loaded.update({ 'price': number[0] })
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if int(user_loaded['price']) >= 10 and int(user_loaded['price']) <= 15 and user_loaded['laptop']== 'dell':
            output = 'dell1'
            check = True
        elif int(user_loaded['price']) > 15 and int(user_loaded['price']) <= 20 and user_loaded['laptop']== 'dell':
            output = 'dell2'
            check = True
        elif int(user_loaded['price']) > 20 and int(user_loaded['price']) <= 25 and user_loaded['laptop']== 'dell':
            output = 'dell3'
            check = True
        elif int(user_loaded['price']) > 25 and user_loaded['laptop']== 'dell':
            output = 'dell4'
            check = True
    
    if 'hp' in userText:
       
       user = { 'laptop': 'hp',
                'price': 0,
                'purpose': ''
       }
       with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user,user_dumped,ensure_ascii = False)             
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
    if n != 0 and 'triệu' in userText:
        user_loaded.update({ 'price': number[0] })
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if int(user_loaded['price']) >= 10 and int(user_loaded['price']) <= 15 and user_loaded['laptop']== 'hp':
            output = 'hp1 15 triệu'
            check = True
        elif int(user_loaded['price']) > 15 and int(user_loaded['price']) <= 20 and user_loaded['laptop']== 'hp':
            output = 'hp2 20 triệu'
            check = True
        elif int(user_loaded['price']) > 20 and int(user_loaded['price']) <= 25 and user_loaded['laptop']== 'hp':
            output = 'hp3 25 triệu'
            check = True
        elif int(user_loaded['price']) > 25 and user_loaded['laptop']== 'hp':
            output = 'hp4 26 triệu'
            check = True
    
    if 'acer' in userText:
       
       user = { 'laptop': 'acer',
                'price': 0,
                'purpose': ''
       }
       with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user,user_dumped,ensure_ascii = False)             
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
    if n != 0 and 'triệu' in userText:
        user_loaded.update({ 'price': number[0] })
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if int(user_loaded['price']) >= 10 and int(user_loaded['price']) <= 15 and user_loaded['laptop']== 'acer':
            output = 'acer1'
            check = True
        elif int(user_loaded['price']) > 15 and int(user_loaded['price']) <= 20 and user_loaded['laptop']== 'acer':
            output = 'acer2'
            check = True
        elif int(user_loaded['price']) > 20 and int(user_loaded['price']) <= 25 and user_loaded['laptop']== 'acer':
            output = 'acer3'
            check = True
        elif int(user_loaded['price']) > 25 and user_loaded['laptop']== 'acer':
            output = 'acer4'
            check = True

    if 'lenovo' in userText:
       
       user = { 'laptop': 'lenovo',
                'price': 0,
                'purpose': ''
       }
       with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user,user_dumped,ensure_ascii = False)             
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
    if n != 0 and 'triệu' in userText:
        user_loaded.update({ 'price': number[0] })
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if int(user_loaded['price']) >= 10 and int(user_loaded['price']) <= 15 and user_loaded['laptop']== 'lenovo':
            output = 'lenovo1'
            check = True
        elif int(user_loaded['price']) > 15 and int(user_loaded['price']) <= 20 and user_loaded['laptop']== 'lenovo':
            output = 'lenovo2'
            check = True
        elif int(user_loaded['price']) > 20 and int(user_loaded['price']) <= 25 and user_loaded['laptop']== 'lenovo':
            output = 'lenovo3'
            check = True
        elif int(user_loaded['price']) > 25 and user_loaded['laptop']== 'lenovo':
            output = 'lenovo4'
            check = True

    if 'macbook' in userText:
       
       user = { 'laptop': 'macbook',
                'price': 0,
                'purpose': ''
       }
       with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user,user_dumped,ensure_ascii = False)             
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))
    with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
    if n != 0 and 'triệu' in userText:
        user_loaded.update({ 'price': number[0] })
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if int(user_loaded['price']) > 20 and int(user_loaded['price']) <= 25 and user_loaded['laptop']== 'macbook':
            output = 'macbook1 25 triệu'
            check = True
        elif int(user_loaded['price']) > 25 and user_loaded['laptop']== 'macbook':
            output = 'macbook2 26 triệu'
            check = True

    if 'học tập' in userText or 'văn phòng' in userText or 'sinh viên' in userText or 'học sinh' in userText or 'kế toán' in userText or 'đi học' in userText:
        user_loaded.update({'purpose': 'học tập - văn phòng'})
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if (user_loaded['laptop']) == 'asus':
            output = 'asus_học_tập'
            check = True
        elif (user_loaded['laptop']) == 'dell':
            output = 'dell_học_tập'
            check = True
        elif (user_loaded['laptop']) == 'macbook':
            output = 'macbook_học_tập'
            check = True
        elif (user_loaded['laptop']) == 'hp':
            output = 'hp_học_tập'
            check = True
        elif 'kế toán' in userText or 'văn phòng' in userText  :        
            output = 'văn phòng'
            check = True
        elif 'đi học' in userText or 'sinh viên' in userText or 'học sinh' in userText or 'học tập' in userText:
            output = 'học tập'
            check = True
    
    if 'đồ họa' in userText or 'kĩ thuật' in userText or 'kỹ thuật' in userText or 'công nghệ thông tin' in userText or 'lập trình' in userText or 'thiết kế' in userText:
        user_loaded.update({'purpose': 'đồ họa - kĩ thuật'})
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if (user_loaded['laptop']) == 'asus':
            output = 'asus_đồ_họa_kĩ_thuật'
            check = True
        elif (user_loaded['laptop']) == 'dell':
            output = 'dell_đồ_họa_kĩ_thuật'
            check = True
        elif (user_loaded['laptop']) == 'macbook':
            output = 'macbook_đồ_họa_kĩ_thuật'
            check = True
        elif (user_loaded['laptop']) == 'hp':
            output = 'hp_đồ_họa_kĩ_thuật'
            check = True
        elif 'đồ họa' in userText or 'thiết kế' in userText:
            output = 'thiết kế đồ họa'
            check = True
        elif 'lập trình' in userText or 'công nghệ thông tin' in userText:
            output = 'lập trình'
            check = True

    if 'game' in userText or 'gaming' in userText:
        user_loaded.update({'purpose': 'gaming'})
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if (user_loaded['laptop']) == 'asus':
            output = 'asus_gaming'
            check = True
        elif (user_loaded['laptop']) == 'dell':
            output = 'dell_gaming'
            check = True
        elif (user_loaded['laptop']) == 'hp':
            output = 'hp_gaming'
            check = True
        else:
            output = 'chơi game'
            check = True

    if 'mỏng nhẹ' in userText or 'gọn nhẹ ' in userText:
        user_loaded.update({'purpose': 'mỏng nhẹ'})
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json','w', encoding='utf-8') as user_dumped :
            json.dump(user_loaded,user_dumped,ensure_ascii = False)
        with open('C://Users//Admin//Desktop//ChatterBot17//ChatterBot//data//ReadUser.json', 'r', encoding='utf-8') as json_file :
            user_loaded = json.load(json_file)
        if (user_loaded['laptop']) == 'asus':
            output = 'asus_mỏng_nhẹ'
            check = True
        elif (user_loaded['laptop']) == 'macbook':
            output = 'macbook_mỏng_nhẹ'
            check = True
        else:
            output = 'mỏng nhẹ'
            check = True

    if (check == True):
       return {'output': str(my_bot.get_response(str(output))), 'timeOut': { 'msg': msgAfterWait, 'milisecond': timeOut }}        
    
    
    number = []
    number = [int(s) for s in userText.split() if s.isdigit()]   
    n = (len(number))

    if n != 0:
        if number[0] < 10 and 'triệu' in userText: 
           if 'asus' in userText:
               output = 'asus_10_triệu'
               check = True
           else:
               output = 'dưới 10 triệu'
               check = True
        elif number[0] >= 10 and number[0] <= 15 and 'triệu' in userText:
           if 'asus' in userText:
               output = 'asus2 15 triệu'
               check = True
           elif 'hp' in userText:
               output = 'hp1 15 triệu'
               check = True
           elif 'lenovo' in userText:
               output = 'lenovo1'
               check = True
           elif 'acer' in userText:
               output = 'acer1'
               check = True
           elif 'dell' in userText:
               print('huhu')
               output = 'dell1'
               check = True
           else:
               output = '15 triệu'
               check = True
        elif number[0] > 15 and number[0] <= 20 and 'triệu' in userText:
           if 'asus' in userText:
               output = 'asus3 20 triệu'
               check = True
           elif 'hp' in userText:
               output = 'hp2 20 triệu'
               check = True
           elif 'lenovo' in userText:
               output = 'lenovo2'
               check = True
           elif 'acer' in userText:
               output = 'acer2'
               check = True
           elif 'dell' in userText:
               output = 'dell2'
               check = True
           else:
               output = '20 triệu'
               check = True
        elif number[0] > 20 and number[0] <= 25 and 'triệu' in userText:
           if 'asus' in userText:
               output = 'asus4 25 triệu'
               check = True
           elif 'macbook' in userText:
               output = 'macbook1 25 triệu'
               check = True
           elif 'hp' in userText:
               output = 'hp3 25 triệu'
               check = True
           elif 'lenovo' in userText:
               output = 'lenovo3'
               check = True
           elif 'acer' in userText:
               output = 'acer3'
               check = True
           elif 'dell' in userText:
               output = 'dell3'
               check = True
           else:
               output = '25 triệu'
               check = True
        elif number[0] > 25 and 'triệu' in userText:                  
           if 'macbook' in userText:
               output = 'macbook2 26 triệu'
               check = True
           elif 'hp' in userText:
               output = 'hp4 26 triệu'
               check = True
           elif 'lenovo' in userText:
               output = 'lenovo4'
               check = True
           elif 'acer' in userText:
               output = 'acer4'
               check = True
           elif 'dell' in userText:
               output = 'dell4'
               check = True
           else:
               output = 'từ 26 triệu'
               check = True
    else:
        if 'dell' in userText:
            output = 'dell'
            check = True
        elif 'asus' in userText:
            output = 'asus'
            check = True
        elif 'macbook' in userText:
            output = 'macbook'
            check = True
        elif 'lenovo' in userText:
            output = 'lenovo'
            check = True
        elif 'hp' in userText:
            output = 'hp'
            check = True
        elif 'acer' in userText:
            output = 'acer'
            check = True
   
    if 'bán chạy' in userText or 'hot' in userText:
        output = 'bán chạy'
        check = True
    if 'pin' in userText or 'trâu' in userText or 'khỏe' in userText:
            output = 'pin khỏe'
            check = True  
     
    if (check == True):
       return {'output': str(my_bot.get_response(str(output))), 'timeOut': { 'msg': msgAfterWait, 'milisecond': timeOut }}        
    
    if 'mua laptop' in userText or 'mua máy tính' in userText:
        output = 'mua laptop'
    if 'cảm ơn' in userText or 'cám ơn' in userText:
        output = 'cảm ơn'
    if 'xin chào' in userText or 'hello' in userText or 'chào' in userText or 'ơi' in userText:
        output = 'xin chào'
    if 'mẫu nào' in userText or 'hãng nào' in userText or 'mẫu gì' in userText or 'hãng gì' in userText or ('tham khảo' in userText and 'laptop' in userText) or 'loại gì' in userText or 'loại nào' in userText:
        output = 'mẫu nào'
    if 'tư vấn' in userText or 'lời khuyên' in userText:
        output = 'tư vấn'
    if 'chưa chọn' in userText or 'không biết' in userText or 'chưa ạ' in userText or 'vâng ạ' in userText or 'chưa biết chọn' in userText:
        output = 'tư vấn thêm'
    if 'địa chỉ' in userText or 'ở đâu' in userText or 'chỗ nào' in userText:
        output = 'địa chỉ'
    if 'ưu đãi' in userText or 'khuyến mãi' in userText or 'khuyến mại' in userText or 'giảm giá' in userText or 'sale' in userText or'chương trình' in userText:
        output= 'ưu đãi'
    return {'output': str(my_bot.get_response(str(output))), 'timeOut': { 'msg': msgAfterWait, 'milisecond': 0 }}\
        if output else None
