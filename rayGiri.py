#RayGiri ~~~ MAA
ray , persons , batele , raySefid , saydRay , sadeRay , masoRay , rayDahande = '' , set() , 0 , 0 , 0 , 0 , 0 , 0

while(True) :
    rayDade = False
    codeMelly = input('شماره شناسنامه را وارد کنید \\ خروج (0): \n')
    if codeMelly != '0' and codeMelly not in persons and len(codeMelly) == 4 :
        ray = input('به کدام نامزد رای میدهید؟ (محمود سعیدی ، باقر صادقی ، احمد مسعودی) \n در صورتی که بیش از یک نام بنویسید، فقط اولین نام محاسبه خواهد شد  \n')
        persons.add(codeMelly)
        rayDahande +=1
        for w in ray.split():
            if w == 'سعیدی':
                saydRay += 1
                rayDade = True
                break
            elif w == 'صادقی':
                sadeRay += 1
                rayDade = True
                break
            elif w == 'مسعودی':
                masoRay += 1
                rayDade = True
                break
        if rayDade == False and len(ray) >= 4 and ray != 'سفید':
            batele += 1
        elif rayDade == False and len(ray) < 4 or ray == "سفید":
            raySefid += 1
    elif codeMelly == '0':
        break
    elif len(codeMelly) != 4:
        print('شماره شناسنامه باید چهار  رقمی باشد')
    elif codeMelly in persons:
        print('این شماره شناسنامه قبلا وارد شده است')
print(f'پایان رای گیری \n نتایج : \n جناب آقای سعیدی : {saydRay} رای \n جناب آقای صادقی : {sadeRay} رای \n جناب آقای مسعودی : {masoRay} رای  \n آرای سفید : {raySefid} \n آرای باطله : {batele} \n تعداد کل رای دهندگان : {rayDahande}')
if saydRay > sadeRay and saydRay > masoRay:
    print('جناب آقای سعیدی بیشترین رای را کسب کردند')
elif sadeRay > saydRay and sadeRay > masoRay:
    print('جناب آقای صادقی بیشترین رای را کسب کردند')
elif masoRay > saydRay and masoRay > sadeRay:
    print('جناب آقای مسعودی بیشترین رای را کسب کردند')
else:
    print('رای گیری در دور اول بدون برنده به پایان رسید')