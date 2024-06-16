class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {"Phone Number": phone_number, "Email": email}

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone Number: {details['Phone Number']}")
                print(f"Email: {details['Email']}")
                print("--------------------")
        else:
            print("No contacts available.")

    def search_contact(self, name):
        if name in self.contacts:
            details = self.contacts[name]
            print(f"Name: {name}")
            print(f"Phone Number: {details['Phone Number']}")
            print(f"Email: {details['Email']}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def update_contact(self, name, phone_number, email):
        if name in self.contacts:
            self.contacts[name] = {"Phone Number": phone_number, "Email": email}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            name = input("Enter name to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contact_book.update_contact(name, phone_number, email)

        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
