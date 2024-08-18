# contact_manager.py
import csv

class ContactManager:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename

    def add_contact(self, contact):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([contact.name, contact.phone, contact.email])
        print(f"Contact {contact.name} added.")

    def delete_contact(self, name):
        contacts = self.get_all_contacts()
        contacts = [c for c in contacts if c[0].lower() != name.lower()]

        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print(f"Contact {name} deleted if it existed.")

    def search_contacts(self, search_term):
        contacts = self.get_all_contacts()
        found_contacts = [c for c in contacts if search_term.lower() in c[0].lower()]

        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
        else:
            print("No contacts found.")

    def get_all_contacts(self):
        contacts = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                contacts = list(reader)
        except FileNotFoundError:
            print("Contacts file not found. Starting a new one.")
        return contacts
