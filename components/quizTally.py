from colorama.ansi import Fore
from components import vars
from PIL import Image
from colorama import Fore, Back

hulk = Image.open("hulk.jpeg")
spider = Image.open("spiderman.jpeg")
iron = Image.open("ironman.jpeg")
pool = Image.open("deadpool.jpeg")
storm = Image.open("storm.jpeg")

def total(value):
    if value < 41:
        vars.character = vars.characters[0]
        hulk.show()
        print (Fore.GREEN + Back.BLACK)
        print("It's " + vars.character)

    elif value < 51:
        vars.character = vars.characters[2]
        iron.show()
        print (Fore.LIGHTCYAN_EX + Back.BLACK)
        print("It's " + vars.character)
    
    elif value < 61:
        vars.character = vars.characters[3]
        pool.show()
        print (Fore.WHITE + Back.BLACK)
        print("It's " + vars.character)
    
    elif value < 100:
        vars.character = vars.characters[1]
        spider.show()
        print (Fore.RED + Back.BLACK)
        print("It's " + vars.character)
    
    elif value > 1000:
        vars.character = vars.characters[4]
        storm.show()
        print (Fore.BLUE + Back.BLACK)
        print("It's " + vars.character)
    
    elif value <= 39:
        print (Fore.RESET + Back.RESET)
        print("Your selection doesnt match any of our characters")
    
    else:
        print("Couldn't generate a result")
   
   
        
    