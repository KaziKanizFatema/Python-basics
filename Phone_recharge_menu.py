
def check():
    print(f"Your current balance is {bal} rupees.")

def recharge_bal(bal,n):
    bal = bal + n
    print(f"Your current balance is {bal} rupees.")
    return bal
def recharge_plan(bal):
    
    print("""
    1. 1GB per month 100 rs
    2. 2GB per month 200 rs
    3. 3GB per month 300 rs
    4. Exit
""")
    y = input("Enter choice: ")
    if y == "1":
        if bal >= 100:
            z = input("""
            1.Yes
            2.NO
            Enter choice: """)
            if z == "1":
                bal = bal - 100
                print("recharge successful!")
                print(f"Your current balance is {bal} rupees.")
            elif z == "2":
                pass
                    
        else: print("Insufficient balance!")
    


    elif y == "2":
            
            if bal >= 200:
                k = input("""
                1.Yes
                2.NO
                Enter choice: """)
                if k == "1":
                    bal = bal - 200
                    print("recharge successful!")
                    print(f"Your current balance is {bal} rupees.")
                elif k == "2":
                    pass
            else: print("Insufficient balance!")


    elif y == "3":
            
            if bal >= 300:
                l = input("""
                1.Yes
                2.NO
                Enter choice: """)
                if l == "1":
                    bal = bal - 300
                    print("recharge successful!")
                    print(f"Your current balance is {bal} rupees.")
                elif l == "2":
                    pass
            else: print("Insufficient balance!")


            
    elif y == "4":
        pass
    return bal

global bal
bal=0
while True:
    print("""
    1. Check balance
    2. Add balance
    3. Recharge plan
    4. Exit
    """)
    x = input("Enter choice: ")

    if x == "1":
        check()

    elif x == "2":
        n = int(input("Enter amount: "))
        bal= recharge_bal(bal,n)
    
    elif x == "3":
       bal= recharge_plan(bal)

    elif x == "4":
     break

    else: print("OOPS! Invalid choice!")

    
    
    
    
    
        
        
        

