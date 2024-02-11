import json

# Initialize an empty list to store contacts
contacts = []


# Function to save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)


# Function to load contacts from a file
def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize contacts as an empty list
        contacts = []


# Function to add a new contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contact = {
        "Name": name,
        "Phone Number": phone_number,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")


# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone Number']}")


# Function to search for a contact
def search_contact():
    query = input("Enter the name or phone number to search: ")
    found_contacts = []

    for contact in contacts:
        if query.lower() in contact["Name"].lower() or query in contact["Phone Number"]:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching contacts:")
        for i, contact in enumerate(found_contacts, 1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone Number']}")


# Function to update a contact
def update_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to update: ")) - 1

    if 0 <= index < len(contacts):
        field = input("Enter the field to update (Name/Phone Number/Email/Address): ")
        new_value = input(f"Enter the new {field}: ")

        contacts[index][field] = new_value
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")


# Function to delete a contact
def delete_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to delete: ")) - 1

    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Contact deleted: {deleted_contact['Name']}")
    else:
        print("Invalid contact number.")


# Main loop
if __name__ == "__main__":
    load_contacts()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
            save_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
            save_contacts()
        elif choice == "5":
            delete_contact()
            save_contacts()
        elif choice == "6":
            save_contacts()
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

