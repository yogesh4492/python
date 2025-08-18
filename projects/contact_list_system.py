import json
import os

FILE_NAME = "contacts.txt"

# Load contacts from file (if exists)
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        contacts = json.load(f)
else:
    contacts = {}

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts()
    print(f" Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("⚠️ No contacts found!")
    else:
        print("\n📋 Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = input("Enter Name to Search: ")
    if name in contacts:
        info = contacts[name]
        print(f"🔍 Found: {name} | Phone: {info['phone']} | Email: {info['email']}")
    else:
        print("❌ Contact not found!")

def update_contact():
    name = input("Enter Name to Update: ")
    if name in contacts:
        phone = input("Enter New Phone Number: ")
        email = input("Enter New Email: ")
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        print(f"✅ Contact '{name}' updated successfully!")
    else:
        print("❌ Contact not found!")

def delete_contact():
    name = input("Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found!")


while True:
        print("\n===== Contact List Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

# Run the program
