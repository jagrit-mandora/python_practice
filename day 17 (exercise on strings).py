#validate the user name on following:
#1. length maust be 12 or less
#2. username must not have any space
#3. username must not have any digits

username=input("enter username : ")

#if len(username)<=12:
 #   print(username)
#else:
 #   print("username cant be more than 12 characters please try again")

#if username.count(" ")<0:
 #   print(username)
#else:
 #   print("username cant have space")

if  len(username)>=12:
    print("username cant be more than 12 characters please try again")
elif username.find(" ") > 0:
     print("username cant have space")
elif not username.isalpha(): 
    print("username cant have digits")
else:
    print(username)
