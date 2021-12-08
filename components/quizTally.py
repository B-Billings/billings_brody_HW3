from components import vars
from PIL import Image
hulk = Image.open("hulk.jpeg")
spider = Image.open("spiderman.jpeg")
iron = Image.open("ironman.jpeg")
pool = Image.open("deadpool.jpeg")
def total(value):
    # do some logic to see which character you selected
    if value <= 40:
        vars.character = vars.characters[0]
        hulk.show()
        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

    if value == 80:
        vars.character = vars.characters[1]
        spider.show()
        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

    if value == 50:
        vars.character = vars.characters[2]
        iron.show()
        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package 
    
    if value == 51:
        vars.character = vars.characters[3]
        pool.show()
        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package   
        
    