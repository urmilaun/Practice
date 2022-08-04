import os
from collections import OrderedDict

phone_book_dict = dict({})

google_drive = dict({})

def show_menu():

    os.system("clear")
    print("** Phone Book Application **")
    print("0. Exit Phone Book Application")
    print("1. Add a New Number")
    print("2. Display Phone Book")
    print("3. Search by Name")
    print("4. Search by Phone Number: PENDING")
    print("5. Delete a Phone Number")
    print("6. Edit a Phone Number")
    print("7. Sort Phone Book: PENDING")
    print("8. Copy Contacts to Google Drive")

    choice = int( input("Enter your choice: "))

    return choice



def add_new_number():

    new_name = input("Enter Name: ")

    if new_name in phone_book_dict.keys():
        print("Record of ", new_name, " already exists!")
        print("Phone Number of ",new_name," is:", phone_book_dict[new_name])
    else:
        phone_number = input("Enter Number: ")

        phone_book_dict[new_name] = phone_number

        print("\nNew Number Added Successfully !!!")
    

def display_phone_book():

    if len(phone_book_dict)==0:
        print("\nPhone Book is currently Empty !!!")

    else:
        print("\nName\tPhone Number")
        for name, phone_number in phone_book_dict.items():
            print(name,"\t",phone_number)
        
        print("")


def search_by_name():

    if len(phone_book_dict)==0:
        print("Phone Book currently empty. Cannot Search!")
    else:
        search_name = input("Enter Name to Search: ")

        if search_name in phone_book_dict.keys():
            print("Phone Number of ",search_name," is:", phone_book_dict[search_name])
        else:
            print("Phone Number of ",search_name," is not found")




def search_by_phone_number():

    if len(phone_book_dict)==0:
        print("Phone Book currently empty. Cannot Search!")
    else:
        search_phone_number = input("Enter Phone Number to Search: ")

        if search_phone_number in phone_book_dict.values():
            pass # pending


def delete_phone_number():

    if len(phone_book_dict)==0:
        print("Phone Book currently empty. Cannot Delete Anything!")
    else:

        delete_name = input("Enter Name to Delete: ")

        if delete_name in phone_book_dict.keys():
            phone_book_dict.pop(delete_name)

            print("Deleted ", delete_name, " Record Successfully!")
        
        else:
            print(delete_name," record not found!")
            
            

def edit_phone_number():
    
    if len(phone_book_dict)==0:
        print("Phone Book currently empty. Cannot Edit Anything!")
    else:
        edit_name = input("Enter Name to Edit: ")

        if edit_name in phone_book_dict.keys():

            print("Current Phone Number is:", phone_book_dict[edit_name])

            new_phone_number = input("Enter New Phone Number: ")
            phone_book_dict[edit_name] = new_phone_number
            print("Edited ", edit_name, " Record Successfully!")
        else:
            print(edit_name," record not found!")

def sort_phone_book(phone_book_dict):

    phone_book_dict = OrderedDict(sorted(phone_book_dict.items))

    print("Sorted Successfully !")


def copy_to_google_drive():

    google_drive = phone_book_dict.copy()

    print("Phone Book copied to google drive")

while True:

    choice = show_menu()

    if choice==0:
        break

    elif choice==1:
        add_new_number()0
    
    elif choice==2:
        display_phone_book()
    
    elif choice==3:
        search_by_name()

    elif choice==4:
        search_by_phone_number()
    
    elif choice==5:
        delete_phone_number()

    elif choice==6:
        edit_phone_number()
    
    elif choice==7:
        sort_phone_book(phone_book_dict)
    
    elif choice==8:
        copy_to_google_drive()
    
    input()


print("\nPhone Book Application Exited Successfully !")