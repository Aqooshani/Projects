#hadse adad ~~~ MAA
import random as rand
import math

userSelect , victory = "" , ""
comSelect = rand.randint(1,50)
while(userSelect != "E") :
    userSelect = input("hads bezan(1 - 50). // payane bazy : 'E' \n")
    if userSelect != "E" :
        userInt = int(userSelect)
        if 0 <= userInt <= 50 :
            if userInt < comSelect :
                print("یکم پایین گفتی")
            elif userInt > comSelect :
                print("یکم بالا گفتی")
            elif userInt == comSelect :
                print("زدی تو خال!")
                victory = True
                break
        else :
            print("لطفا یک عدد بین صفر و پنجاه وارد کنید.")
if victory == True :
    print("پایان بازی، شما برنده شدید! \n    :)")
else :
    print("پایان بازی، شما انصراف دادید‌\n    :(")