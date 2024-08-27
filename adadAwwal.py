#tashkhise adade awwal ~~~ MAA
userInp , isAwwal , shomar = "" , False , set()
while(userInp != "E") :
    userInp = input("**********\nیک عدد مثبت کوچکتر از ده هزار وارید کنید. \n پایان بازی : E \n")
    shomar = set()
    if userInp != "E" :
        userInp = int(userInp)
        if userInp == 1 :
            isAwwal = False
        elif 1 <=userInp <=10000 :
            isAwwal = False
            for n in range(1 , 100) :
                if (userInp % n) == 0 :
                    isAwwal = True
                    shomar.add(n)
        elif userInp > 10000 or userInp <1 :
            print("عدد باید بین یک و ده هزار باشد")
        if len(shomar) == 2 :
            print(f"عدد {userInp} یک عدد اول است.")
        elif len(shomar) > 2  :
            print(f"عدد {userInp} یک عدد اول نیست. \n شمارنده های زیر صد :  '{shomar}")
print("**********\n پایان بازی :)")