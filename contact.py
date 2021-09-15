from person import Person   
from os import stat, system, name
import time

def clear():
      
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

class Notebook:

    def __init__(self):
        self.people = dict()

################################################################            
################################################################  SHOW CONTACTS        
################################################################        
        
    def show_notebook(self):
        countr = 1
        for key , value in self.people.items():
            print (f"{countr} --> name : {key} , email : {value[0]} , phone(phones) : {value[1]} ")
            countr+=1
        if len(self.people) == 0 :
            print("the note book is empty")
        time.sleep(3)
        
        

################################################################            
################################################################  ADD CONTACT        
################################################################                    
            
    def add_contact(self):

        first_name = input("please enter your first name : ").title()
        clear()
        last_name = input("please enter your last name : ").title()
        clear()
        yes_no = "n"
        email = "______"
        while(yes_no != "n" or yes_no != "y"):
            yes_no = input("Do you want to add email? (y/n) : ")
        
            if (yes_no == "y"):
                email = input("please enter your email : ")
                if "@" not in email:
                    print("Sorry, the email is invalid !!!")
                    continue
                
            break
                    
        my_person = Person(first_name , last_name , email) 

        my_person.add_phone_numbers()

        key = my_person.get_first_name()+ " " + my_person.get_last_name()
        value = [my_person.get_email(),my_person.get_phone_numbers()]
        self.people[key] = value
        
################################################################            
################################################################  MENU OF SORT
################################################################                

    def display_sort_menu(self):
        print("      Sort menu\n")
        print("***1 : Sort by name")
        print("***2 : Back")
        print("***3 : Exit")
        
        number = int(input("Enter your choice ? "))
        clear()
        if number == 1:
            self.sort_by_name()

        elif number == 2:
            return

        elif number == 3:
            exit()

        else:
            print("Wrong input ")

        self.display_sort_menu()
        
################################################################            
################################################################  SORT CONTACTS
################################################################      
  
    def sort_by_name(self):
        countr = 1
        for key in sorted(self.people.keys()):
            print (f"{countr} : \nname : {key} \nemail : {self.people[key][0]}\nphone : {self.people[key][1]}")
            countr+=1
            
            
    def search_contact(self):
        self.display_search_menu()    
        
################################################################            
################################################################  MENU OF SEARCH 
################################################################        

    def display_search_menu(self):
        print("      Search menu\n")
        print("***1 : Search by first name")
        print("***2 : Search by last name")
        print("***3 : Search by whole name")
        print("***4 : Search by email")
        print("***5 : Search by number")
        print("***6 : Back")
        print("***7 : Exit")

        number = int(input("Enter your choice ? "))
        clear()
        
        if number == 1:
            self.search_by_first_name()

        elif number == 2:
            self.search_by_last_name()

        elif number == 3:
            self.search_by_whole_name()

        elif number == 4:
            self.search_by_email()

        elif number == 5:
            self.search_by_phone_number()

        elif number == 6:
            return

        elif number == 7:
            exit()
        else:
            print("Wrong input ")

        self.display_search_menu()
        
################################################################            
################################################################  SEARCH METHODS
################################################################        

    def search_by_first_name(self):
        first_name = input("Enter the first name of your contact : ").title()
        find = 0 
        for key  in self.people.keys():
            if key.split(" ")[0] == first_name :
                print(f"\n\tE-mail : {self.people[key][0]}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            print("Not found")

    def search_by_last_name(self):
        last_name = input("Enter the last name of your contact : ").title()
        find = 0 
        for key  in self.people.keys():
            if key.split(" ")[1] == last_name :
                print(f"\n\tE-mail : {self.people[key][0]}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            print("Not found")


    def search_by_whole_name(self):
        name = input("Enter the name of your contact : ").title()
        find = 0 
        for key in self.people.keys():
            if key == name :
                print(f"\n\tE-mail : {self.people[key][0]}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            print("Not found")

    def search_by_email(self):
        email = input("Enter the Email of your contact : ")
        find=0
        for key in self.people:
            if self.people[key][0] == email :
                print(f"\n\tname : {key}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            print("Not found")


    def search_by_phone_number(self):
        phine_number = input("Enter the number of phone of your contact : ")
        find=0
        for key in self.people:
            if phine_number in self.people[key][1]  :
                find=1
                print(f"\n\tname : {key}  email : {self.people[key][0]}\n")
        if find == 0:
            print("Not found")

################################################################            
################################################################  REMOVE CONTACT
################################################################   
     
    def remove_contact(self):
        self.show_notebook()
        number = input("Please enter the number of contact (Between the list above) :‌ ")
        check_correct_number = 0
        if not number.isnumeric():
            check_correct_number = 1
        elif not int(number) <= len(self.people):
            check_correct_number = 1
        
        if check_correct_number == 1:
            print("the number is incorrct!\n try again !!!")
            time.sleep(2)
            clear()
            self.remove_contact()
        
        else :
            countr = 1
            clear()
            for key in self.people:
                if countr == int(number) :
                    del self.people[key]
                    print("the contact is deleted !")
                    time.sleep(2)
                    break
                countr+=1
            self.show_notebook()
            time.sleep(3)
            


    def edit_contact(self):
        self.display_edit_menu()
    
    
    
    def display_edit_menu(self):
        print("      Edit menu\n")
        print("*** 1 : Edit first name")
        print("*** 2 : Edit last name")
        print("*** 3 : Edit email")
        print("*** 4 : Edit phone number")
        print("*** 5 : Back ")
        print("*** 6 : Exit ")
        
        number = input("Enter your choice ? ")
        clear()
        if number == "1" :
            self.edit_first_name()
        
        elif number == "2" :
            self.edit_last_name()
            
        elif number == "3" :
            self.edit_email()
        
        elif number == "4" :
            self.edit_phone_numbers()
            

        elif number == "5" :
            return

        elif number == "6" :
            exit()
        else :
            print("Incorrect input !\ntry again")
            time.sleep(2)
            self.display_edit_menu()
        
        
    def edit_first_name(self):
        self.show_notebook()
        number = input("Please enter the number of contact (Between the list above) :‌ ")
        check_correct_number = 0
        if not number.isnumeric():
            check_correct_number = 1
        elif not int(number) <= len(self.people):
            check_correct_number = 1
        
        if check_correct_number == 1:
            print("the number is incorrct!\n try again !!!")
            time.sleep(2)
            clear()
            self.edit_first_name()
        
        else :
            countr = 1
            clear()
            for key in self.people:
                if countr == int(number) :
                    new_name = input("please enter the new first name : ").title()
                    new_name = new_name + key[key.find(" ") + 1 :]
                    self.people[new_name] = self.people[key]
                    del self.people[key]
                    print("the contact is edited !")
                    time.sleep(2)
                    break
                countr+=1
            self.show_notebook()
            time.sleep(3)
        
    def edit_last_name(self):
        self.show_notebook()
        number = input("Please enter the number of contact (Between the list above) :‌ ")
        check_correct_number = 0
        if not number.isnumeric():
            check_correct_number = 1
        elif not int(number) <= len(self.people):
            check_correct_number = 1
        
        if check_correct_number == 1:
            print("the number is incorrct!\n try again !!!")
            time.sleep(2)
            clear()
            self.edit_last_name()
        
        else :
            countr = 1
            clear()
            for key in self.people:
                if countr == int(number) :
                    new_name = input("please enter the new last name : ").title()
                    new_name = key[0 : key.find(" ")] + new_name
                    self.people[new_name] = self.people[key]
                    del self.people[key]
                    print("the contact is edited !")
                    time.sleep(2)
                    break
                countr+=1
            self.show_notebook()
            time.sleep(3)
        
            
    def edit_email(self):
        self.show_notebook()
        number = input("Please enter the number of contact (Between the list above) :‌ ")
        check_correct_number = 0
        if not number.isnumeric():
            check_correct_number = 1
        elif not int(number) <= len(self.people):
            check_correct_number = 1
        
        if check_correct_number == 1:
            print("the number is incorrct!\n try again !!!")
            time.sleep(2)
            clear()
            self.edit_email()
        
        else :
            countr = 1
            clear()
            for key in self.people:
                if countr == int(number) :
                    while True:
                        new_email = input("please enter the new email : ")
                        if "@" in new_email:
                            break
                        print("Incorrect email !\ntry again")
                    self.people[key] = [new_email,self.people[key][1]]
                    print("email edited")
                    break
                countr+=1
            self.show_notebook()
            time.sleep(3)
        
    
    def edit_phone_numbers(self):
        self.show_notebook()
        number = input("Please enter the number of contact (Between the list above) :‌ ")
        check_correct_number = 0
        if not number.isnumeric():
            check_correct_number = 1
        elif not int(number) <= len(self.people):
            check_correct_number = 1
        
        if check_correct_number == 1:
            print("the number is incorrct!\n try again !!!")
            time.sleep(2)
            clear()
            self.edit_phone_numbers()
        
        else :
            countr = 1
            clear()
            for key in self.people:
                if countr == int(number) :
                    while True:
                        number_phone = input("How many number do you want to add : ")
                        if not number.isnumeric():
                            clear()
                            print("Incorrect input!\ntry again")
                            continue
                        break
                        
                    list_phone = []
                    for contr in range(int(number_phone)):
                        list_phone.append(input("please enter the new number : "))
                    self.people[key] = [self.people[key][0],list_phone]
                    
                    print("phone number edited")
                
                countr+=1
                
            self.show_notebook()
            time.sleep(3)
    
    
    def sort(self):
        self.display_sort_menu()
        
################################################################            
################################################################  MAIN MENU
################################################################        

   
    
    
    def desplay_menu(self):

        print("*************************************************")
        print("* \tWelcome to your contact notebook        *")
        print("* 1 : Add contact                               *")
        print("* 2 : Edit contact                              *")
        print("* 3 : Delete contact                            *")
        print("* 4 : Sort your notebook                        *")
        print("* 5 : Search to find your contact               *")
        print("* 6 : Show your notebook                        *")
        print("* 7 : Exit                                      *")
        print("*************************************************")

        number = int(input("Enter your choice ? "))

        if number == 1:
            self.add_contact()

        elif number == 2:
            self.edit_contact()

        elif number == 3:
            self.remove_contact()

        elif number == 4:
            self.sort()

        elif number == 5:
            self.search_contact()

        elif number == 6:
            self.show_notebook()

        elif number == 7:
            exit()
            
        else:
            print("Wrong input")

        self.desplay_menu()
            
def main():
    my_notebook=Notebook()  
    my_notebook.desplay_menu()

if __name__ == '__main__':
    main()
    