pass1 = input("Enter your password here : ")
pass2 = ""
if 5 < len(pass1) < 20 :
   while(pass1 != pass2):
       pass2 = input("Enter your password again : ")
   print("login succesful! \n : )")
else :
   print("password len should be between 5 - 20 corracters.")
