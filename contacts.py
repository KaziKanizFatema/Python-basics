contacts = {"Kaniz" : "12345",
            "Fatema" : "98765",
            "Kazi" : "65749"}

print(contacts.items())
  


while True:
    x = input("""
1. delete contact number
2. create or edit contacts
3. Access any contact
4. Exit
: """)

    if x == "1":
        n = input("Enter the contact name you want to delete: ")
        contacts.pop(n)
        print(contacts)

    elif x == "2":
        a = input("Enter the contact name you want to add or edit: ")
        b = input("Enter the mobile number: ")
        contacts.update({a : b})
        print(contacts)

    elif x == "3":
        c = input("Enter name: ")
        print(contacts[c])

    elif x == "4":
     break

    else: print("OOPS!! Invalid choice")
