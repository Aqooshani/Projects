#Sang-Kaghaz-Gheychy
import random
userSelect , comScore , userScore = "" , 0 , 0
while(userSelect != "E"):
    randNum = random.randint(1,3)
    if randNum == 1 :
        comSelect = "sang"
    elif randNum == 2 :
        comSelect = "kaghaz"
    elif randNum == 3 :
        comSelect = "gheychee"
    userSelect = input("sang , kaghaz , gheychee , payane bazy : E")
    
    if userSelect == comSelect :
        print(f"**** \nMosavi! :| \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
    elif userSelect == "sang" :
        if comSelect == "kaghaz" : 
            comScore += 1
            print(f"**** \nBakhti! :( \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
        elif comSelect == "gheychee" :
            userScore += 1
            print(f"**** \nBordy! :) \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
    elif userSelect == "kaghaz" :
        if comSelect == "sang" :
            userScore += 1
            print(f"**** \nBordi! :) \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
        elif comSelect == "gheychee" :
            comScore += 1
            print(f"**** \nBakhti! :( \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
    elif userSelect == "gheychee" :
        if comSelect == "sang" :
            comScore += 1
            print(f"**** \nBakhty! :( \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
        elif comSelect == "kaghaz" :
            comScore += 1
            print(f"**** \nBakhty! :( \n entekhabe shoma: {userSelect} , entekhabe CPU : {comSelect} \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
    elif userSelect == "E" :
        print("payane bazy. \n******")
        break
    else :
        print(f" '{userSelect}' meghdare motabary nist.")
if userScore == comScore :
    print(f"****** \nMosavi! :| \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
elif userScore > comScore :
    print(f"****** \nBORDY! :) \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
elif userScore < comScore :
    print(f"****** \nBAKHTY! :( \n emtiaze shoma: {userScore} , emtiaze CPU : {comScore}")
            
        
   