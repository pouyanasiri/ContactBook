class Person():
     
    def __init__(self,first_name,last_name,email) :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_numbers = list()
    def add_phone_numbers(self):
        count = int(input("How many numbers do you want to add for your contact : "))
        for i in range(1,count+1):
            self.phone_numbers.append(input(f"Number {i} : "))
        
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
    
    def get_phone_numbers(self):
        return self.phone_numbers
    

