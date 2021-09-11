from person import Person


class Notebook:
    
    def __init__(self):
        self.people = dict()
        
    def show_notebook(self):
        print(self.people)
    
    def add_contact(self):

        first_name = input("please enter your first name : ").title()
        last_name = input("please enter your last name : ").title()
        email = input("please enter your email : ")

        my_person = Person(first_name , last_name , email) 

        my_person.add_phone_numbers()

        key = my_person.get_first_name()+ " " + my_person.get_last_name()
        value = [my_person.get_email(),my_person.get_phone_numbers()]
        self.people[key] = value


    def display_search_menu(self):
        print("      Search menu     ")
        print("* 1 : Search by first name*")
        print("* 2 : Search by last name*")
        print("* 3 : Search by whole name*")
        print("* 4 : Search by email*")
        print("* 5 : Search by number*")
        print("* 6 : Back*")
        print("* 7 : Exit*")

        number = int(input("Enter your choice ? "))

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

    def search_by_first_name():
        pass

    def search_by_last_name():
        pass

    def search_by_whole_name():
        pass

    def search_by_email():
        pass

    def search_by_phone_number():
        pass
    
    
    def remove_contact(self):
        pass

    def search_contact(self):
        self.display_search_menu()

    def edit_contact(self):
        pass

    def sort(self):
        pass

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
    