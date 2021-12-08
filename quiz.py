from components.quizQuestions import questions
from components import vars, quizTally, gameRules
from colorama import Fore, Back, Style
print (Fore.RED + "=========================================")
print (Fore.RED + "= Welcome to HW3 a Marvel Python 3 quiz =")
print (Fore.RED + "=========================================")
print (Fore.WHITE + "")
while vars.player is False:
    
    gameRules.gameRules()



    vars.player=False