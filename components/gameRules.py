from components.quizQuestions import questions
from components import vars, quizTally
from PIL import Image
from colorama.ansi import Fore, Back, Style
import emoji


def gameRules():
    print (Fore.RED)
    answer1= questions["q1"][input(questions["q1"]["question"])]

    vars.quizTotal += answer1
    print (Fore.WHITE + "==========================================\n")

    print (Fore.RED)
    answer2 = questions["q2"][input(questions["q2"]["question"])]
    

    vars.quizTotal += answer2
    print (Fore.WHITE + "==========================================\n")

    print (Fore.RED)
    answer3 = questions["q3"][input(questions["q3"]["question"])]
    
    vars.quizTotal += answer3
    print (Fore.WHITE + "==========================================\n")
    
    print (Fore.RED)
    answer4 = questions["q4"][input(questions["q4"]["question"])]

    vars.quizTotal += answer4
    print (Fore.WHITE + "==========================================\n") 
    print (Fore.RED)
    answer5 = questions["q5"][input(questions["q5"]["question"])]
    

    vars.quizTotal += answer5
    print (Fore.WHITE + "==========================================\n")
    print (Fore.RED)
    answer6 = questions["q6"][input(questions["q6"]["question"])]
    

    vars.quizTotal += answer6
    print (Fore.WHITE + "==========================================\n") 

    print (Fore.RED)
    answer7 = questions["q7"][input(questions["q7"]["question"])]
    

    vars.quizTotal += answer7
    print (Fore.WHITE + "==========================================\n")

    print (Fore.RED)
    answer8 = questions["q8"][input(questions["q8"]["question"])]
    

    vars.quizTotal += answer8
    print (Fore.WHITE + "==========================================\n")
    
    print (Fore.RED)
    answer9 = questions["q9"][input(questions["q9"]["question"])]
    

    vars.quizTotal += answer9
    print (Fore.WHITE + "==========================================\n")


    quizTally.total(vars.quizTotal)

    vars.player = input("would you like to go again?")
        
    if vars.player  == "y":
        print("Here goes another round")
        print(emoji.emojize(":thumbs_up:"))
        vars.quizTotal = 0

    elif vars.player == "n":
        print("Thanks for playing see you again soon!")
        print(emoji.emojize(":thumbs_down:"))
        quit()
    
    elif vars.player != "y, n":
        print("Invalid choice quitting the game")
        quit()

    print (Fore.WHITE + "==========================================\n")


