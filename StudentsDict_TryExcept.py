"""
students' dictionary

Mohammad Ali Aqooshani
"""
import random    # baraye sakhte code rahgiri
studentsDict = {'ali': {'score': [20, 19, 17, 20], 'data': {'address': 'qom,khiabane2,kooche3,p10', 'age': 14, 'fatherName': 'abbas', 'phone': 9192734187}, 'mored': []},
                'mohammad': {'score': [15, 17, 14, 18], 'data': {'address': 'qom,khiabane2,kooche3,p10', 'age': 14, 'fatherName': 'sadegh', 'phone': 9362917352}, 'mored': []},
                'hassan': {'score': [19, 18, 17, 20], 'data': {'address': 'qom,khiabane5,kooche5,p3', 'age': 14, 'fatherName': 'qasem', 'phone': 9124382716}, 'mored': [{'code': 11,'cont': 'ffff'}, {'code': 12, 'cont': 'ssss'}]},
                'hosein': {'score': [20, 19, 17, 18], 'data': {'address': 'qom,khiabane21,kooche2,p43', 'age': 14, 'fatherName': 'karim', 'phone': 9128237162}, 'mored': []}
                }
def scoreAdd(x, y):
    """
    in function mitavanad yek nomre ye jadid baraye har yek az danesh
    amoozan ezafe konad.
    """
    studentsDict[x]['score'].append(y)
    print(f"نمره جدید با موفقیت ثبت شد. \n نمرات دانش آموز: \n{studentsDict[x]['score']}")
def scoreMoaddel(x):
    n = 0
    for i in studentsDict[x]['score']:
        n += i
    if n != 0:#Jelo giri as errore "ZeroDivisionError"
        n = n/len(studentsDict[x]['score'])#ohasebe-ye moadel
    print(n)
def moredAdd(x, y):
    """
     in function yek mored jadid ba tozihate karbar va code peygirie random
     ezafe mikonad.
    """
    z = random.randint(10, 99)#sakhte code rahgirie do raqami
    studentsDict[x]['mored'].append({'code': z,'cont': y})
    return z
def moredDel(x, y):
    """
    hazf kardane yek morede enzebati ba daryaft name danesh Amooz va
    code peygiri
    """
    found = False  # baraye mavaqhei ke karbar code ra eshtebah vared karde ast
    for i in studentsDict[x]['mored']:
        if i['code'] == y:
            studentsDict[x]['mored'].remove(i)
            found = True
            found_object = i['cont']
    if found == True:
        return found_object
    else:
        return False
def moredSee(x):
    """
    moshahede ye mavarede enzebatie yek danesh Amooz
    """
    moredHa = ''  # zakhire ye mavarede peyda shode dar string
    if len(studentsDict[x]['mored']) != 0:  # tashkhise khali boodane mored ha
        for i in studentsDict[x]['mored']:
            moredHa += f'{i , }'
        return moredHa
    else:
        return 1  # baraye tashkhise khali boodane mored ha
def studentData(x, adr = False, age = False, ftn = False, pho = False):
    """
    in function mitavanad yek dataye khas ya hame ye ettelaAte danesh Amooz ra
    return konad.
    """
    if adr == age == ftn == pho == True:
        return studentsDict[x]['data']
    elif adr == True :
        return studentsDict[x]['data']['address']
    elif age == True :
        return studentsDict[x]['data']['age']
    elif ftn == True :
        return studentsDict[x]['data']['fatherName']
    elif pho == True :
        return studentsDict[x]['data']['phone']
    else:
        return 'error'
def studentList():
    stuTxt = ''
    for i in studentsDict.keys():
        stuTxt += f'{i} , '
    return stuTxt
def studentAdd(n, **kwargs):
    studentsDict.update({n : kwargs})
print('سلام، به سیستم مدیریت مدرسه خوش آمدید.')
while(True):
    userInp = input('*********************\nمیخواهید چه کاری انجام دهید؟ \n(افزودن نمره/مشاهده معدل/افزودن مورد انظباطی/مشاهده موارد انظباطی/مشاهده اطلاعات دانش آموز/حذف کردن مورد انظباطی/افزودن دانش آموز جدید)\n')
    if ('افزودن' in userInp or 'اضافه کردن' in userInp or 'add' in userInp) and ('نمره' in userInp or 'امتیاز' in userInp or 'score' in userInp):
        name = input('نام دانش آموز را وارد کنید \n')
        score = input("نمره را وارد کنید. \n")
        try:
            if 0 < int(score) <= 20:
                scoreAdd(name.lower(), int(score))
            else:
                print('نمره نا معتبر است')
        except KeyError:
            print('نام دانش آموز مورد نظر یافت نشد.')
        except:
            print("لطفا نمره را به صورت عددی وارد کنید.")
    elif 'معدل' in userInp or 'میانگین' in userInp:
        name = input('نام دانش آموز مورد نظر را وارد کنید \n')
        try:
            scoreMoaddel(name.lower())
        except:
            print("نام دانش آموز مورد نظر در لیست یافت نشد.")
    elif ('افزودن' in userInp or 'اضافه کردن' in userInp) and 'مورد' in userInp:
        name = input('نام دانش آموز مورد نظر را وارد کنید. \n')
        try:
            cont = input('توضیح مختصری از مورد انظباطی را بنویسید. \n')
            if 5 <= len(cont) <= 40:
                z = moredAdd(name.lower(), cont)
                print(f'مورد انظباطی با موفقیت ثبت شد. \n کد پیگیری: {z}')
            else:
                print('توضیح مختصر باید بین پنج تا چهل کاراکتر باشد.')
        except:
            print('دانش آموز مورد نظر در سیستم پیدا نشد.')
    elif ('حذف' in userInp or 'پاک کردن' in userInp) and 'مورد' in userInp:
        name = (input('نام دانش آموز مورد نظر را وارد کنید. \n')).lower()
        try:
            if len(studentsDict[name]['mored']) != 0:
                code = input('کد پیگیری را وارد کنید.')
                try:
                    if 10 <= int(code) < 100:
                        fun = moredDel(name, int(code))
                        if fun != False:
                            print(f'مورد انظباطی دانش آموز "{name}" با توضیحات "{fun}" با موفقیت حذف شد.')
                        else:
                            print('عملیات ناموفق')
                    else:
                        print('کد پیگیری مورد انظباطی باید یک عدد دو رقمی باشد.')
                except:
                    print('کد پیگیری باید عددی باشد.')
            else:
                print('برای این دانش آموز هیچ مورد انظباطی ثبت نشده است.')
        except:
            print('نام دانش آموز مورد نظر در لیست یافت نشد.')
    elif ('اطلاعات' in userInp or 'داده' in userInp) and 'دانش آموز' in userInp:
        name = input('نام دانش آموز مورد نظر را وارد کنید.').lower()
        try:
            userWant = input('آیا اطلاعات خاصی از دانش آموز را می خواهید؟ (نام پدر/شماره تلفن/آدرس/سن) \n')
            if 'تلفن' in userWant or 'شماره' in userWant:
                phone = studentData(name, False, False, False, True)
                print(f'شماره تلفن دانش آموز: \n {phone}')
            if 'نام پدر' in userWant:
                ftN = studentData(name, False, False, True)
                print(f'نام پدر دانش آموز: \n {ftN}')
            if 'آدرس' in userWant:
                address = studentData(name, True)
                print(f'آدرس دانش آموز: \n {address}')
            if 'سن' in userWant:
                age = studentData(name, False, True)
                print(f'سن دانش آموز: \n {age}')
            else:
                data = studentData(name, True, True, True, True)
                print(f'آدرس دانش آموز: {data["address"]} \nسن دانش آموز : {data["age"]} \nنام پدر دانش آموز : {data["fatherName"]} \nشماره همراه : {data["phone"]}')
        except:
            print('دانش آموز مورد نظر در لیست موجود نمی باشد. \n درصورتی که اطمینان دارید، به املای حروف دقت کنید.')
    elif ('لیست' in userInp or 'اسامی' in userInp) or userInp == 'دانش آموزان':
        sList = studentList()
        print(f'اسامی دانش آموزان : \n {sList}')
    elif (('افزودن' in userInp or 'اضافه کردن' in userInp) and ('دانش آموز' in userInp)) or userInp == 'دانش آموز جدید':
        newSt = input('نام دانش آموز جدید را وارد کنید.')
        if 1 < len(newSt) < 25:
            newStAddr = input('آدرس دانش آموز را به صورت متنی کوچکتر از صد کاراکتر وارد کنید. \n')
            if len(newStAddr) < 100:
                newStAge = input('سن دانش آموز را به صورت عددی وارد کنید. \n')
                try:
                    newStAge = int(newStAge)
                    if 12 <= newStAge <= 18:
                        newStFtN = input('نام پدر دانش آموز را وارد کنید. \n')
                        if len(newStFtN) < 30:
                            newStPhone = input('لطفا یک شماره ی همراه مربوط به دانش آموز وارد کنید. \n')
                            try:
                                newStPhone = int(newStPhone)
                                if 9000000000 <= newStPhone <= 9999999999:
                                    studentAdd(newSt, **{'score': [], 'data': {'address': newStAddr, 'age': newStAge, 'fatherName': newStFtN, 'phone': newStPhone}, 'mored': []})
                                    print('دانش آموز مورد نظر به لیست افزوده شد. \nجهت ویرایش اطلاعات، میتوانید از همین سامانه اقدام کنید.')
                                else:
                                    print('شماره تلفن نادرست')
                            except:
                                print('شماره تلفن باید کاملا عددی باشد.')
                        else:
                            print('نام پدر دانش آموز بیش از حد طولانی است.')
                    else:
                        print('طبق قوانین این مدرسه، فقط دانش آموزان بازه سنی 12 تا 18 سال پذیرفته میشوند.')
                except:
                    print('لطفا سن دانش آموز را به صورت عددی وارد کنید.')
            else:
                print('محدودیت تعداد کاراکتر آدرس.')
        else:
            print('محدیدیت تعداد کاراکتر نام دانش آموز')
    elif ('مشاهده' in userInp or 'لیست' in userInp) and 'موارد' in userInp:
        name = input('نام دانش آموز مورد نظر را وارد کنید. \n')
        if name in studentsDict.keys():
            returnSave = moredSee(name)
            if returnSave != 1:
                print(f'موارد انظباطی دانش آموز: \n{returnSave}')
            else:
                print('هیچ مورد انظباطی برای این دانش آموز یافت نشد.')
    else:
        print('******************************\nپایان کار سیستم \n خسته نباشید :)')
        break