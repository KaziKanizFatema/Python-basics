'''
1. The password should be at least 8 characters
2. It should contain at least one uppercase and one lowercase
3. It should contain at least one digit
4. It should contain at least one special character(@ or $)

'''

pw = input("Enter password: ")
j,k,l,m = 0,0,0,0
digit = "123456789"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"
special = "@$"

if len(pw) >= 8:
    for i in pw:
       if i in digit:
           j += 1
    
       if i in capital:
           k += 1

       if i in small:
           l += 1
    
       if i in special:
           m += 1

if(j >= 1 and k >= 1 and l >= 1 and m >= 1): print("The password is strong")

else: print("invalid")
