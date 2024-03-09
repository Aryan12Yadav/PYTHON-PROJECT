import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email  = ('Enter your valid email : ')
while user_email!='stop':
    user_email = input('Enter your the valid email : ')



    if re.search(email_condition,user_email):
        print(" right Email ")


    else:
        print("Wrong email ")



