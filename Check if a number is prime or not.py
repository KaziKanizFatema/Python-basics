num = int(input("enter the number: "))

if num > 1:
    for i in range (2, num):
        
         if num%i == 0: 
           print("The number is not prime")
           break
         else: 
            print("The number is prime")
            break

elif num == 1: print("The number is 1 and also prime")
else: print("The number is prime")
