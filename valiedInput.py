from os import system, name
from cmath import inf
import os
from colortype import *
from time import sleep

def valiedInput(number=inf):
    while(True):
        try :
            if number != inf:
                choice = int(input("Enter your choice : "))
                if choice > number or choice < 0:
                    prRed("Wrong Range of input ")
                    continue
                os.system('clear')
                return choice
            else :
                choice = int(input())
                os.system('clear')
                return choice
        
        except ValueError:  
            prRed("Wrong input ")
            sleep(1)
        

def clear():
    os.system('clear')
def clear():
      
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

