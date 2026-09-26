import re


s=True
while(s == True):
    x = input("enter your password : ")
    if len(x) < 8:
        print("password must be of 8 characters or long.","\n")
    elif not re.search("[A-Z]",x):
        print("password must contain an uppercase letter.","\n")
    elif not re.search("[a-z]",x):
        print("password must contain a lowercase letter.","\n")
    elif not re.search("[0-9]",x):
        print("password must contain a number.","\n")
    else:
        print("password is strong.")
        s = False
    