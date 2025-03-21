contact = {}

while True:
    print("\nContact Book")
    print("1.Create contact")
    print("2.View contact")
    print("3.Delete contact")
    print("4.Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        name = input("Enter your name: ")
        if name in contact:
            print("Already exists")
        else:
            age = int(input("Enter age: "))
            phone = int(input("Enter phone number: "))
            email = input("Enter email: ")
            contact[name] = {'age':age,'phone':phone,'email':email}
            print(f"Contact name {name} has been created")
    elif choice == 2:
        name = input("Enter name of contact: ")
        if name in contact:
            contact = contact[name]
            print(f"Name:{name}, Age:{age} and phone number:{phone}")
        else: 
            print("Contact not found")
    elif choice == 3:
        name = input("Enter name of contact: ")
        if name in contact:
            del contact[name]
            print(f"Contact name {name} has been deleted")
        else:
            print("Contact not found")
    elif choice == 4:
        print("Goodbye, thanks for using contact book")
        break
    else: 
        print("Invalid Input")
        continue