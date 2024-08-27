"""
sakhte password-e random

Mohammad-Ali-Aqooshani
"""
import random
def PasswordJenerator(x):
    charList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numList = '1234567890'
    Password = ''  # baraqe zakhire sazie ramze dar hale sakht
    char = 0  # baraye fahmidane tedad charactere harfi
    num = 0  # rahe bargasht---age eshtebah shod dorostesh mikone(line24)
    for i in range(x):
        randSelect = random.randint(1, 2)  # entekhabe harf ya adad(random)
        if randSelect == 1 and char < x/2:
            randLen = random.randint(0, len(charList)-1)  # yek indexe tasadofi peyda mikonad
            Password += f'{charList[randLen]}'
            char += 1
        elif randSelect == 2 or char >= x/2:
            num += 1
            if num <= x/2:
                randLen = random.randint(0, len(numList) -1)
                Password += f'{numList[randLen]}'
            else:
                randLen = random.randint(0, len(charList)-1)
                Password += f'{charList[randLen]}'
    return Password
userNum = input('سلام. به سازنده ی رمز خوش آمدید. \n لطفا تعداد رقم مورد نظر را به عدد وارد کنید. \n')
if userNum.isdigit():
    x = PasswordJenerator(int(userNum))
    print(x)
else:
    print('لطفا مقدار را به عدد وارد کنید.')