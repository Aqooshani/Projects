#kholase email ~~~MAA
citySet , univerSet , fNameSet , lNameSet , city , univercity , fName , lName , resomSet , resome = set(("تهران" , "قم" , "اصفهان" , "شیراز" , "مشهد" , "اهواز" , "تبریز")) , set(('شریف' , 'امیرکبیر' , 'فردوسی' , 'قم' , 'تهران')) , set(('محمد' , 'علی' , 'باقر' , 'صادق' , 'محمدجواد' , 'محمدعلی' , 'حسن' , 'حسین')) , set(('آقوشانی' , 'محمدی' , 'موسوی' , 'حسینی' , 'باقری' , 'حسنی' , 'صادقی')) , set() , set() , set() , set() , set(('c#','c++','js','javascript','react','python','front')) , set()
email = input('پیام خود را وارد کنید \n (اگر نام دانشگاه شما هم نام یک شهر است، حتما ابتدا نام شهر و بعد نام دانشگاهتان را وارد کنید.): \n')
isCity = False
isUniver = False
for w in email.split() :
    if w in citySet and isCity == False:
        city.add(w)
        isCity = True
    elif w in univerSet and isCity == True:
        if isUniver == False:
            univercity.add(w)
            isUniver = True
        else :
            city.add(w)
    elif w in univerSet and isCity == True:
        if isUniver == False :
            univercity.add(w)
            isUniver = True
        else :
            city.add(w)
    elif w in citySet and w not in univerSet :
        city.add(w)
    elif w in fNameSet :
        fName.add(w)
    elif w in lNameSet :
        lName.add(w)
    elif w.lower() in resomSet :
        resome.add(w)
    else :
        pass
if fName == set():
    fName = 'پیدا نشد'
if lName == set():
    lName = 'پیدا نشد'
if city == set():
    city = 'پیدا نشد'
if univercity == set():
    univercity = 'پیدا نشد'
if resome == set() :
    resome = 'پیدا نشد'
print(f'نام {fName} \n نام خانوادگی {lName} \n دانشگاه {univercity} \n شهر {city} \n رزومه : {resome}')
        