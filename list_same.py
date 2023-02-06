list1 = []
n = int(input("enter the list's length: "))
for i in range(0, n):
    num = int(input(":"))
  
    list1.append(num)
print(list1)

if list1[0] == list1[-1]:
    print("The first and last number is same!!")
else:
    print("The first and last number is not same!!")
