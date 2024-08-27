# Phone Number Search
# Mohammad Ali Aqooshani
#
isNum = False
numbers = []
def searchFn(x):
    global isNum
    for i in x.split():#bayad matno barresy konam.
        if i.isdigit():#int dar edame moshkel saz mishe...
            if 9000000000 <= int(i) <= 9999999999:# shomare bayad 11 raqamy va ba raqame avvale 9 bashad.
                isNum = True# man adad peyda kardam!...
                if int(i) not in numbers:# agar in shomare ro qablan peyda nakarde boody:
                    numbers.append(int(i))#bezar shomarato save konam! ...
    return isNum
voroody = input('payam ra vared conid : \n')
searchFn(voroody)
if isNum == True:#adady peyda shod?
    print(f'{len(numbers)} shomare peyda shod : \n {numbers}')
elif(isNum == False):#...peyda nashod?
    print('hich shomare ee peyda nashod.')
print('************************************')