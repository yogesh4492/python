import json 
import os

File_Name="contacts.json"

if os.path.exists(File_Name):
    with open(File_Name,"r") as f:
        contacts=json.load(f)
else:
    contacts={}

def save_contacts():
    with open(File_Name,"w") as f:
        json.dump(contacts,f,indent=4)

def add_contacts():
    name=input("Enter name= ")
    phone=input("Enter phone= ")
    email=input("Enter email= ")
    contacts[name]={"phone":phone,"email":email}
    save_contacts()
    print(f"contact {name} saved successfully")

def view_contacts():
    if not contacts:
        print("No contacts")
    else:
        for name,info in contacts.items():
            print(f"Name= {name} \n Phone No:{info['phone']} \n Email Id:{info['email']}")
    
while True:
    print("1. Add Contact")
    print("2. view Contact")
    print("3. exit")
    ch=int(input("Enter Your Choice= "))
    if ch==1:
        add_contacts()
    elif ch==2:
        view_contacts()
    elif ch==3:
        break
    else:
        print("Invalid Input")