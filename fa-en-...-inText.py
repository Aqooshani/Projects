"""
darsade farsi va Englisy dar matn

Mohammad Ali Aqooshani
"""
print('salam, be hesabgare darsade anvae character ha khosh amadid.')
persian , faNum = 'ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی ئ' , '۱۲۳۴۵۶۷۸۹۰'
english , enNum = 'a b c d e f g h i j k l m n o p q r s t u v w x y z' , '1234567890'
numbers = ''
def myspliter(x):
    engInTxt = 0    # shomarande ye character haye englisy dar matn
    prsInTxt = 0    # shomarande ye character haye farsy dar matn
    wigInTxt = 0    # shomarande ye character haye digar dar matn
    for i in x:
        i = str(i)    # baraye jelogiry az error haye int
        if i in english or i in enNum:
            engInTxt += 1
        elif i in persian or i in faNum:
            prsInTxt += 1
        else:
            wigInTxt += 1
    magmoo = engInTxt + prsInTxt + wigInTxt
    adad = 100 / magmoo    # bedast avardane adady ke ba oon mishe darsad gereft
    if prsInTxt != 0:    # baraye jelogiri az errore "ZeroDivisionError"
        faDarsad = round(prsInTxt * adad)    # ba in ravesh darsade in no(farsy) be sorate round peyda mishe.
    else:
        faDarsad = 0
    if engInTxt != 0:
        enDarsad = round(engInTxt * adad)
    else:
        enDarsad = 0
    if wigInTxt != 0:
        wiDarsad = round(wigInTxt * adad)
    else:
        wiDarsad = 0
    return faDarsad, enDarsad, wiDarsad
fa , en , wi = myspliter(input('matn-e khod ra vared konid : \n'))#khoroojy gereftan va farakhanye function
print(f'******************** \n darsad ha: \n farsi: %{fa} \n english : %{en} \n alamat ha : %{wi}')
if en >= 70:#agar matn az no-e khassy bashe...
    print('in matn yek matne englisy ast.')
elif fa >= 70:
    print('in matn yek matne farsy ast.')
elif wi >= 70:
    print('bishtare matne dade shode az alamt hast.')
else:
    print('matne shoma yek matne makhloot ast.')
print('movaffagh bashid :)')