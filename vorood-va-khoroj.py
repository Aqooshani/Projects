#Mohammad Ali Aqooshani
#exam for: lists

import datetime as time
myNum = 0#
myN = 0#for line12 , 13
hazeran = []
sanad = []
openTime , clotTime = [] , []
didNtClose = ''
while(True):
    #------I want use the minute for houre; ...-----------
    myTime = time.datetime.now().minute
    if myTime > 48 :
        myTime -= 48
    elif myTime >24 :
        myTime -= 24;
    #--------------------------------------------------
    
    myN += 1 #      so the system knows is shoul say 'salam' to user? 
    if myN == 1:#       if the user is new for system...
        userSelect = input('سلام، این سیستم ثبت ورود و خروج کارمندان است. \n انتخاب کنید ورود/خروج/خروج از سیستم=(0) :\n')
    else :#     No! You should not greet an old user...
        userSelect = input('\t \t \t \t \t \t \t \t \t \t ************ \nانتخاب کنید ورود/خروج/خروج از سیستم=(0) :\n')

    if userSelect == 'ورود' :
        karmandFN = input('نام کارمند را وارد کنید:')#      new employee's first name
        karmandLN = input('نام خانوادگی کارمند را وارد کنید:')#     new employee's last name
        if [karmandFN , karmandLN] not in hazeran :#he may have aleardy been Entered...
            if len(karmandFN) > 2 and len(karmandFN) < 12 and len(karmandLN) > 3 and len(karmandLN) < 16 :#wait ; I should check your data!
                hazeran.append([karmandFN , karmandLN])#        save the employee's data in "hazeran" list.
                
                sanad.append([karmandFN , karmandLN])
                openTime.append([myTime])#i shold save the user data.
                
            else :#     i`m sorry; system found out that you are a liar! :0
                print('لطفا نام و نام خانوادگی را به درستی وارد کنید')
        else :
            print(karmandLN , 'قبلا وارد شده است.')
    elif userSelect == 'خروج':
        if len(hazeran) > 0 :#      is any employee in office?
            karmandFN = input('نام کارمند را وارد کنید:\n')
            karmandLN = input('نام خانوادگی کارمند را وارد کنید:\n')
            if [karmandFN , karmandLN] in hazeran :#        was he/she aleardy entered?
                hazeran.remove([karmandFN , karmandLN])
    #--------search for save his clothes time------------
                myNum = 0
                for i in hazeran :
                    if i == [karmandFN , karmandLN] :
                        break
                    myNum +=1
                openTime[myNum].append(myTime)
   #----------------------------------------------------
                print(karmandLN , 'با موفقیت خارج شد')
            else :
                print(f" کارمند {karmandFN , karmandLN}  قبلا وارد نشده است. \n اگر وارد شده بوده اید، به املای نام و نام خانوادگی دقت کنید.")
        else :#     No; how can close a person; while no one has entered?
            print('هنوز کسی وارد نشده است.')
    elif userSelect == '0' :
        print('پایان کار سیستم.\n ')
        break
    else :
        print('لطفا یکی از مقادیر گفته شده را وارد کنید.')
if len(hazeran) > 0 :
    for i in hazeran :
        didNtClose += i[1]
    print(f'خروج کارمندان زیر هنوز ثبت نشده است: \n {didNtClose}')
else :
    print('همه ی کارمندان خارج شدند.')
userSelect = input('آیا مایلید جدول زمانی را مشاهده کنید؟(بله/خیر):')
if userSelect == 'بله' or userSelect == 'آره' :
    myNum = 0
    for i in sanad:
        if len(openTime[myNum]) == 2:#are you have the time of his cloth?
            print(f'آقای {i[0]} {i[1]} در ساعت {openTime[myNum][0]} وارد و در ساعت {openTime[myNum][1]}خارج شد.')
        elif len(openTime[myNum]) == 1 :#-No; I haven't!
            print(f'آقای {i[0]} {i[1]} در ساعت {openTime[myNum][0]} وارد شده ولی خروجی برای او ثبت نشده است.')
        else :#if was any Error,:
            print(openTime[myNum])
        myNum += 1
print('خسته نباشید. \n (:')
            