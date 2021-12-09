from components import vars
from PIL import Image

hulk = Image.open("hulk.jpeg")
spider = Image.open("spiderman.jpeg")
iron = Image.open("ironman.jpeg")
pool = Image.open("deadpool.jpeg")
storm = Image.open("storm.jpeg")

def total(value):
    # do some logic to see which character you selected
    if value < 41:
        vars.character = vars.characters[0]
        hulk.show()
        print("It's " + vars.character)

    elif value < 51:
        vars.character = vars.characters[2]
        iron.show()
        print("It's " + vars.character)
    
    elif value < 61:
        vars.character = vars.characters[3]
        pool.show()
        print("It's " + vars.character)
    
    elif value < 100:
        vars.character = vars.characters[1]
        spider.show()
        print("It's " + vars.character)
    
    elif value > 1000:
        vars.character = vars.characters[4]
        storm.show()
        print("It's " + vars.character)
    
    elif value <= 39:
        print("Your selection doesnt match any of our characters")
    
    else:
        print("Couldn't generate a result")
   
   
        
    