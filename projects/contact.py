import json
import os

File_Name="contacts.json"

if os.path.exists(File_Name):
    with open(File_Name,"r") as f:
        contacts=json.load(f)
else:
    contacts={}

def save_contact():
    with open(File_Name,"w") as f:
        json.dump(contacts,f,indent=4)

def add_contact():
    name=input("Enter Your Name= ")
    phone=input("Enter Phone Number= ")
    email=input("Enter Email= ")
    contacts[name]={"phone":phone,"email":email}
    save_contact()
    print(f"Contacts {name} saved successfuly")

def view_contact():
       if not contacts:
           print("Contact Is Not Available")
       else:
           print("Contact  List ")
           for name,info in contacts.items():
               print(f"name={name} ,phone={info['phone']},email={info['email']}")
def search_contact():
    print()

def update_contact():
     print()

def delete_contact():
     print()


while True:
     print("1. Add Contact ")
     print("2. View Contacts ")
     print("3. search Contact ")
     print("4. Update Contact ")
     print("5. delete Contact ")
     print("6. Exit ")
     print()
     ch=int(input("Enter Your Choice = "))
     if ch==1:
         add_contact()
     elif ch==2:
         view_contact()
     elif ch==3:
         search_contact()
     elif ch==4:
         update_contact()
     elif ch==5:
         delete_contact()
     elif ch==6:
         print("Thank For Using Our System")
         break
     else:
         print("Invalid Input")

    
     