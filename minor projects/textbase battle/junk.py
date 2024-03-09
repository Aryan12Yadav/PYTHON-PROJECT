import re
uservarfying = input("Enter the email; :")
email_varfying = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
a = re.search(email_varfying,uservarfying)
print(a)