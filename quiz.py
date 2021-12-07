from components.quizQuestions import questions
from components import vars, quizTally, gameRules
from PIL import Image

while vars.player is False:
    vars.player = input("Type Yes to begin the quiz")
   
    print("==============================================================")
    
    gameRules.gameRules()

    vars.player=False