class Notebook:
    def __init__(self):
        self.people = dict()
    
    def add_contact(self):
        pass
    def remove_contact(self):
        pass
    def search_contact(self):
        pass
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
        print("* 6 : Exit                                      *")
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
            exit()
        else:
            print("Wrong input")

        self.desplay_menu()
            
def main():
    my_notebook=Notebook()  
    my_notebook.desplay_menu()

if __name__ == '__main__':
    main()
    