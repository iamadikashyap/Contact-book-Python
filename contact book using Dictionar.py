contacts= {}
while True:
    print("\n1. Add Contact\n2. View All Contacts\n3. Search Contacts\n4. Delete Contact\n5. Exit")
    choice = input("Enter your choice:").strip()
    
    if choice == "1":
        name= input("Name:")
        phone= input("phone:")
        contacts[name]= phone
        print(f"Contact {name} has been added.")
    elif choice == "2":
        for name,phone in contacts.items():
            print(f"Name:{name}, Phone:{phone}")
    elif choice == "3":
        search_name= input("Enter the name to search:")
        if search_name in contacts:
            print(f"Name: {search_name}, Phone:{contacts[search_name]}")
        else:
            print(f"NO contact found with the name {search_name}")
    elif choice == "4":
        delete_name = input("Enter the name to delete:")
        if delete_name in contacts:
         del contacts[delete_name]
        print(f"Contact{delete_name}has been deleted.")
    elif choice == "5":
        print("Exiting the contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
