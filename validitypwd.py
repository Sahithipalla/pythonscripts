import re
p=input("Enter password:")
x=True
while x:
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[@#$]",p):
        break 
    else:
        print("password is valid")
        x=False
        break
if x:
    print("password is invalid")
