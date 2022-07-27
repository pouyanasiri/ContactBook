from person import Person   
import time
from valiedInput import *
from colortype import *
import re

class Notebook:

    def __init__(self):
        self.people = dict()

################################################################            
################################################################  SHOW CONTACTS        
################################################################        
        
    def show_notebook(self):        
        
        countr = 1
        for key , value in self.people.items():
            prCyan (f"{countr} --> name : {key} , email : {value[0]} , phone(phones) : {value[1]} ")
            countr+=1
        if len(self.people) == 0 :
            prRed("The Note Book is Empty")
            time.sleep(3)
            clear()
            return 0
        time.sleep(3)
        
        

################################################################            
################################################################  ADD CONTACT        
################################################################                    
            
    def add_contact(self):

        first_name = input("please enter your first name : ").title()
        clear()
        last_name = input("please enter your last name : ").title()
        clear()
        yes_no = "N"
        email = "______"
        while(yes_no != "N" or yes_no != "Y"):
            yes_no = input("Do you want to add email? (y/n) : ").capitalize()[0]
            
            while yes_no == "Y" :
                if (yes_no == "Y"):
                    email = input("please enter your email : ")
                    if not re.search("^[a-zA-Z0-9]{5,}@(gmail|yahoo|email)\.com$",email):
                        prRed("Sorry, the email is invalid !!!")
                        continue
                    else:
                        break    
            if(yes_no != "Y" and yes_no != "N"):
                prRed("Wrong Input!")
                continue
            break        
        
        my_person = Person(first_name , last_name , email) 
        clear()
        my_person.add_phone_numbers()

        key = my_person.get_first_name()+ " " + my_person.get_last_name()
        value = [my_person.get_email(),my_person.get_phone_numbers()]
        self.people[key] = value
        
################################################################            
################################################################  MENU OF SORT
################################################################                

    def display_sort_menu(self):
        prGreen("      Sort menu\n")
        prGreen("***1 : Sort by name")
        prGreen("***2 : Back")
        prGreen("***3 : Exit")
        
        number = valiedInput(3)
        clear()
        if number == 1:
            self.sort_by_name()

        elif number == 2:
            return

        elif number == 3:
            exit()
        input("Enter Any key to Return Previous page : ")
        clear()
        self.display_sort_menu()
        
        
################################################################            
################################################################  SORT CONTACTS
################################################################      
  
    def sort_by_name(self):
        if len(self.people.keys()) == 0:
            prRed("Note Book is Empty")
            return
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
        prGreen("      Search menu\n")
        prGreen("***1 : Search by first name")
        prGreen("***2 : Search by last name")
        prGreen("***3 : Search by whole name")
        prGreen("***4 : Search by email")
        prGreen("***5 : Search by number")
        prGreen("***6 : Back")
        prGreen("***7 : Exit")

        number = valiedInput(7)
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
            
        input("Enter Any key to Return Previous page : ")
        clear()
        
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
            prRed("Not found")

    def search_by_last_name(self):
        last_name = input("Enter the last name of your contact : ").title()
        find = 0 
        for key  in self.people.keys():
            if key.split(" ")[1] == last_name :
                print(f"\n\tE-mail : {self.people[key][0]}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            prRed("Not found")


    def search_by_whole_name(self):
        name = input("Enter the name of your contact : ").title()
        find = 0 
        for key in self.people.keys():
            if key == name :
                print(f"\n\tE-mail : {self.people[key][0]}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            prRed("Not found")

    def search_by_email(self):
        email = input("Enter the Email of your contact : ")
        find=0
        for key in self.people:
            if self.people[key][0] == email :
                print(f"\n\tname : {key}  phone numbers : {self.people[key][1]}\n")
                find=1
        if find == 0:
            prRed("Not found")


    def search_by_phone_number(self):
        phine_number = input("Enter the number of phone of your contact : ")
        find=0
        for key in self.people:
            if phine_number in self.people[key][1]  :
                find=1
                print(f"\n\tname : {key}  email : {self.people[key][0]}\n")
        if find == 0:
            prRed("Not found")

################################################################            
################################################################  REMOVE CONTACT
################################################################   
     
    def remove_contact(self):
        if self.show_notebook() == 0:
            return
        prRed("Are You Sure ? \nYou Can Enter 0 to Cancel This")
        number = valiedInput(len(self.people))
        if number == 0:
            return
        countr = 1
        clear()
        for key in self.people:
            if countr == int(number) :
                del self.people[key]
                print("the contact is deleted !")
                time.sleep(2)
                break
            countr+=1
        time.sleep(3)
        clear()
            


    def edit_contact(self):
        self.display_edit_menu()
    
    
    
    def display_edit_menu(self):
        prGreen("      Edit menu\n")
        prGreen("*** 1 : Edit first name")
        prGreen("*** 2 : Edit last name")
        prGreen("*** 3 : Edit email")
        prGreen("*** 4 : Edit phone number")
        prGreen("*** 5 : Back ")
        prGreen("*** 6 : Exit ")
        
        number = valiedInput(6)
        clear()
        if number == 1 :
            self.edit_first_name()
        
        elif number == 2 :
            self.edit_last_name()
            
        elif number == 3 :
            self.edit_email()
        
        elif number == 4 :
            self.edit_phone_numbers()
            
        elif number == 5 :
            return

        elif number == 6 :
            exit()
        else :
            print("Incorrect input !\ntry again")
            time.sleep(2)
            self.display_edit_menu()
        
        
    def edit_first_name(self):
        if self.show_notebook() == 0:
            return
        prRed("Are You Sure ? \nYou Can Enter 0 to Cancel This")
        number = valiedInput(len(self.people))
        if number == 0:
            return
        countr = 1
        clear()
        for key in self.people:
            if countr == number :
                new_name = input("please enter the new first name : ").title()
                new_name = new_name + " "+ key[key.find(" ") + 1 :]
                temp = self.people[key]  
                del self.people[key]
                self.people[new_name] = temp
                print("the contact is edited !")
                time.sleep(2)
                break
            countr+=1
        time.sleep(3)
        clear()
        
    def edit_last_name(self):
        if self.show_notebook() == 0:
            return
        prRed("Are You Sure ? \nYou Can Enter 0 to Cancel This")
        number = valiedInput(len(self.people))
        if number == 0:
            return
        countr = 1
        clear()
        for key in self.people:
            if countr == int(number) :
                new_name = input("please enter the new last name : ").title()
                new_name = key[0 : key.find(" ")] + " "+new_name
                temp = self.people[key]  
                del self.people[key]
                self.people[new_name] = temp
                print("the contact is edited !")
                time.sleep(2)
                break
            countr+=1
        time.sleep(3)
        clear()
        
            
    def edit_email(self):
        
        if self.show_notebook() == 0:
            return
        prRed("Are You Sure ? \nYou Can Enter 0 to Cancel This")
        number = valiedInput(len(self.people))
        if number == 0:
            return
        countr = 1
        clear()
        for key in self.people:
            
            while True and countr == number:
                new_email = input("please enter the new email : ")
                if not re.search("^[a-zA-Z0-9]{5,}@(gmail|yahoo|email)\.com$",new_email):
                    prRed("Sorry, the email is invalid !!!")
                    continue
                self.people[key] = [new_email,self.people[key][1]]
                print("email edited")
                time.sleep(3)
                break
            countr+=1
        clear()
    
    def edit_phone_numbers(self):
        if self.show_notebook() == 0:
            return
        prRed("Are You Sure ? \nYou Can Enter 0 to Cancel This")
        number = valiedInput(len(self.people))
        if number == 0:
            return
        countr = 1
        clear()
        for key in self.people:
            if countr == int(number) :
                print("How many number do you want to add : ")
                number_phone = valiedInput()
                    
                list_phone = []
                for i in range(number_phone):
                    while True:
                        phone = input(f"New Number {i+1} : ")
                        if re.search("09\d{9}",phone) and len(phone)==11:
                            list_phone.append(phone)
                            break
                        else:
                            prRed("Wrong input!\n the length of phone number is 11 and start with 09")
            
            countr+=1
        self.people[key] = [self.people[key][0],list_phone]                
        print("phone number edited") 
        time.sleep(3)
        clear()
    ########################################################################
    ########################################################################  SORT CAONTACTS
    ########################################################################
    
    def sort(self):
        self.display_sort_menu()
    
    def getfile(self):
        with open(f"Contacts/notebook.txt" , "a") as myfile :
            countr = 1
            for key , value in self.people.items():
                myfile.write(f"{countr} --> name : {key} , email : {value[0]} , phone(phones) : {value[1]} \n")
                countr+=1
            if len(self.people) == 0:
                myfile.write("EMPTY!\n")
        prCyan("Note Book is Ready!")
        time.sleep(2)
        clear()
        
################################################################            
################################################################  MAIN MENU
################################################################        

    def desplay_menu(self):

        prGreen("*************************************************")
        prGreen("* \tWelcome to your contact notebook         *")
        prGreen("* 1 : Add contact                               *")
        prGreen("* 2 : Edit contact                              *")
        prGreen("* 3 : Delete contact                            *")
        prGreen("* 4 : Sort your notebook                        *")
        prGreen("* 5 : Search to find your contact               *")
        prGreen("* 6 : Show your notebook                        *")
        prGreen("* 7 : Get File Of Contacts                      *")
        prGreen("* 8 : Exit                                      *")
        prGreen("*************************************************")

        number = valiedInput(8)

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
            input("Enter Any key to Return Previous page : ")
            clear()
            
        elif number == 7:
            self.getfile()
        
        elif number == 8:
            exit()
            
        self.desplay_menu()