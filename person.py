import re
from time import sleep
from colortype import prCyan, prRed
from valiedInput import *

class Person():
     
    def __init__(self,first_name,last_name,email) :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_numbers = list()
    def add_phone_numbers(self):
        print("How many numbers do you want to add for your contact : ")
        count = valiedInput()
        for i in range(count):
            while True:
                phone = input(f"Number {i+1} : ")
                if re.search("09\d{9}",phone) and len(phone)==11:
                    self.phone_numbers.append(phone)
                    break
                else:
                    prRed("Wrong input!\n the length of phone number is 11 and start with 09")
        
        prCyan("Contact Saved ")
        sleep(2)
        clear()
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
    
    def get_phone_numbers(self):
        return self.phone_numbers
    

