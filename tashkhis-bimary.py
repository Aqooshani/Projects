#tashkhise Bimary ~~~ MAA
userSpe = input("درد در کدام ناحیه است؟ \n سینه , شکم , گلو , هیچکدام  \n") #Saves the user's speech
if userSpe == "شکم" :
    print("آپاندیس")
elif userSpe == "سینه" :
    print("بیماری قلبی یا ریوی")
elif userSpe == "گلو" :
    userSpe = input("آیا تب دارید؟")
    if userSpe == "بله" or userSpe == "آره" :
        print("بیماری باکتریایی")
    elif userSpe == "خیر" or userSpe == "نه" :
        print("بیماری ویروسی")
elif userSpe == "هیچکدام" or userSpe == "هیچ کدام" :
    userSpe = input("آیا سرفه دارید؟ \n")
    if userSpe == "بله" or userSpe == "آره" :
        userSpe = input("آیا تب دارید؟ \n")
        if userSpe == "بله" or userSpe == "آره" :
            print("احتمالا شما مبتلا به آنفولانزا هستید.")
        elif userSpe == "خیر" or userSpe == "نه" :
            print("احتمالا سرما خورده اید.")
    elif userSpe == "خیر" or userSpe == "نه" :
        print("شما به نظر سالم هستید.")
else :
    print("لطفا یکی از مقادیر گفته شده را وارد کنید.")