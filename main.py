# main.py
from contact import Contact
from contact_manager import ContactManager

def main():
    manager = ContactManager()

    while True:
        print("\nContactMaster Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            contact = Contact(name, phone, email)
            manager.add_contact(contact)
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '3':
            search_term = input("Enter the name to search: ")
            manager.search_contacts(search_term)
        elif choice == '4':
            print("Exiting ContactMaster. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
