class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)
        print(f"Added contact: {new_contact}")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Removed contact: {contact}")
                return
        print(f"Contact with name {name} not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Found contact: {contact}")
                return
        print(f"Contact with name {name} not found.")

    def display_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(contact)


# Example usage of the ContactBook class
if __name__ == "__main__":
    my_contact_book = ContactBook()

    # Adding contacts
    my_contact_book.add_contact("Alice", "555-1234", "alice@example.com")
    my_contact_book.add_contact("Bob", "555-5678", "bob@example.com")
    my_contact_book.add_contact("Charlie", "555-8765", "charlie@example.com")

    # Displaying all contacts
    my_contact_book.display_contacts()

    # Searching for a contact
    my_contact_book.search_contact("Bob")

    # Removing a contact
    my_contact_book.remove_contact("Alice")

    # Displaying all contacts again
    my_contact_book.display_contacts()
