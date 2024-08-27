"""
mohasebe ye zaribe movaffagiat
Mohammad_Ali_Aqooshani
"""
import math  # mohasebeye factorial
def mohasebe(b, r, v, t, h):
    """
    b = barname rizi
    r = regime ghazaie salem
    v = varzesh
    t = tafrih va esterahat
    h = honar
    """
    score = 0  # zakhire ye emtiaze karbar
    score += math.factorial(b) + math.factorial(r) + math.factorial(v) + math.factorial(t) + math.factorial(h)  # baraye tathire bishtare a'dade bozorg, az factorial estefade shode ast.
    return score
print('سلام. به حسابگر درصد موفقیت خوش آمدید. \n لطفا با دقت به سوالات پاسخ دهید \n سوالات به صورت پنج گزینه ای است و شما باید یک نمره بین 1 تا 5 به خود بدهید. \n 1:از آن بی زارم ، 2:آن را دوست ندارم ، 3:بی اطلاعم ، 4:کمی ، 5:کاملا علاقه مند و فعال')
barnameRizi = input('چقدر اهل برنامه ریزی هستید؟ \n')
regime = input('به رژیم غذایی خود چه نمره ای میدهید؟ \n')
varzesh = input('به ورزش و فعالیت بدنی خود چه نمره ای میدهید؟ \n')
tafrih = input('به استراحت و تفریح روزانه ی خود چه نمره ای میدهید؟ \n')
honar = input('به فعالیت هنری خود چه نمره ای میدهید؟ \n')
try:  # barresye adady bodane vorody ha
    barnameRizi, regime, varzesh, tafrih, honar = int(barnameRizi), int(regime), int(varzesh), int(tafrih), int(honar)  # tabdil kardane dade ha be dade ye adady
    if 1 <= barnameRizi <= 5 and 1 <= regime <= 5 and 1 <= varzesh <= 5 and 1 <= tafrih <= 5 and 1 <= honar <= 5:  # barresye sahih bodane voroodye karbar
        score = mohasebe(barnameRizi, regime, varzesh, tafrih, honar)
        if score != 0:  # jelogiri az errore ZeroDivision
            score = round(score/6)  # round kardan va tabdile zaribe 600 be 100
            print(f'امتیاز شما: \n {score}')
            if score <= 25:
                print('سعی کنید وضعیت خود را تغییر دهید. \nاز روانشناسان و افراد متخصص و با تجربه کمک بگیرید.')
            elif score <= 50:
                print('وضعیت شما نیاز به بهبود دارد. \n برای حفظ سلامتی جسمی و روحی خود، از روانشناسان، افراد با تجربه و وبسایت ها و مقالات آموزشی کمک بگیرید.')
            elif score <= 75:
                print('شما نسبتا فرد موفقی هستید؛ با اندکی تغییر و کوشش، میتوانید به اهداف خود برسید. \n در این زمینه میتوانید از روانشناسان و افراد موفق کمک بگیرید.')
            elif score <= 95:
                print('شما یک فرد موفق هستید. \n عادت ها و رفتار های درست خود را حفظ کنید، و از هر فرصتی برای تحقق خواسته هایتان استفاده کنید.')
            elif score <= 100:
                print('تبریک! شما واقعا یک انسان موفق هستید؛ \nطبق این تحلیل، شما دارای عملکرد خوبی در طول روز هستید، \n به سمت اهدافتان پیش بروید و از مشکلات نترسید.')
    else:
        print('اعداد باید بین 1 تا پنج باشند.')
except:
    print('لطفا پاسخ را فقط به صورت عدد وارد کنید.')