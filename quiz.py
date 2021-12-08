from components.quizQuestions import questions
from components import vars, quizTally, gameRules
from colorama import Fore, Back, Style

print (Fore.RED + "=========================================")
print (Fore.RED + "= Welcome to HW3 a Marvel Python 3 quiz =")
print (Fore.RED + "=========================================")
print (Fore.RED + Back.WHITE + "==============Character list==============")
print (Fore.GREEN + Back.RESET + "================ The Hulk ================")
print (Fore.LIGHTCYAN_EX + "================ Iron Man ================")
print (Fore.RED+ "=============== Spider-Man ===============")
print (Fore.WHITE+ "================ Deadpool ================")
print (Fore.BLUE+ "================== Storm =================")
print (Fore.RED + Back.WHITE + "============== Instructions ==============")
print (Fore.WHITE + Back.RESET + "Think of one of the characters in the list")
print (Fore.WHITE  + "   and answer the questions Yes or No")
print (Fore.WHITE  + "  At the End You Should be givin your")
print (Fore.WHITE + "           character Enjoy!")
print (Fore.WHITE + "")
print (Fore.WHITE + "")


while vars.player is False:
    
    gameRules.gameRules()



    vars.player=False