from components.quizQuestions import questions
from components import vars, quizTally
from PIL import Image

def gameRules():
    
    answer1 = questions["q1"][input(questions["q1"]["question"])]
    

    vars.quizTotal += answer1
    print("==========================================\n")

    answer2 = questions["q2"][input(questions["q2"]["question"])]
    

    vars.quizTotal += answer2
    print("==========================================\n")


    answer3 = questions["q3"][input(questions["q3"]["question"])]
    

    vars.quizTotal += answer3
    print("==========================================\n")

    answer4 = questions["q4"][input(questions["q4"]["question"])]

    vars.quizTotal += answer4
    print("==========================================\n") 

    answer5 = questions["q5"][input(questions["q5"]["question"])]
    

    vars.quizTotal += answer5
    print("==========================================\n")

    answer6 = questions["q6"][input(questions["q6"]["question"])]
    

    vars.quizTotal += answer6
    print("==========================================\n") 

    answer7 = questions["q7"][input(questions["q7"]["question"])]
    

    vars.quizTotal += answer7
    print("==========================================\n")

    answer8 = questions["q8"][input(questions["q8"]["question"])]
    

    vars.quizTotal += answer8
    print("==========================================\n")

    answer9 = questions["q9"][input(questions["q9"]["question"])]
    

    vars.quizTotal += answer9
    print("==========================================\n")


    quizTally.total(vars.quizTotal)

    vars.player = input("would you like to go again?")
        
    if vars.player  == "y":
        print("Here goes another round")
        vars.quizTotal = 0

    elif vars.player == "n":
        print("Thanks for playing see you again soon!")
        quit()

    print("==============================================================")


