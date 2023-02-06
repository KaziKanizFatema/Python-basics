#Fahrenheit to Celcius: C = (F-32) (5/9)
#Celsius to Fahrenheit: F = C(9/5) + 32

n = input("for converting fahrenheit to celcius write 1 \nfor converting celcius to fahrenheit write 2\n: ")


def f2c(ft):
     
     c = (ft - 32) * (5 /9)
     print(f"{c} degree celcius")
    
def c2f(cs):
     
     F = cs * (9 / 5) + 32
     print(f"{F} degree fahrenheit")
     
if n == "1":
     ft = int(input("Enter temperature in fahrenheit: "))
     f2c(ft)
     
      
elif n == "2":
     cs = int(input("Enter temperature in celcius: "))
     c2f(cs)
     
      
else:
    print("invalid")

