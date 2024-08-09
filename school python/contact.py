contacts = []


def add_contact():
    """Add a new contact to the list."""
    print("Adding a new contact:")
    name = input("Name:").strip()
    phone = input("Phone:").strip()
    email = input("Email:").strip()
    age = input("Age:").strip()
    city = input("City:").strip()
   
    Contact = {
        "Name": "Ramey",
        "Phone": "773-606-2874",
        "Email": "rameyisamazeballs.com",
        "Age": 15,
        "City": "Chicago"
    }
    contacts.append(Contact)
    print("Contact added successfully.")


def view_contacts():
    "View all contacts in the list."
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts list:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"Contact {idx}:")
            print(f"  Name: {contact['Name']}")
            print(f"  Phone: {contact['Phone']}")
            print(f"  Email: {contact['Email']}")
            print(f"  Age: {contact['Age']}")
            print(f"  City: {contact['City']}")
            print("-" * 20)


def search_contact():
    "Search for a contact by name."
    name_to_search = input("Enter the name to search: ").strip().lower()
    found = False
   
    for contact in contacts:
        if name_to_search in contact['Name'].lower():
            print(f"Found contact:")
            print(f"  Name: {contact['Name']}")
            print(f"  Phone: {contact['Phone']}")
            print(f"  Email: {contact['Email']}")
            print(f"  Age: {contact['Age']}")
            print(f"  City: {contact['City']}")
            print("-" * 20)
            found = True
   
    if not found:
        print("Contact not found.")


def delete_contact():
    "Delete a contact by exact name."
    name_to_delete = input("Enter the exact name of the contact to delete: ").strip()
    global contacts
    new_contacts = [contact for contact in contacts if contact['Name'] != name_to_delete]
   
    if len(new_contacts) < len(contacts):
        contacts = new_contacts
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    "Main function to run the menu-driven interface."
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
       
        choice = input("Enter your choice (1-5): ").strip()
       
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
