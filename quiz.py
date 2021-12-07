from components.quizQuestions import questions
from components import vars, quizTally
from PIL import Image

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("+++++++++++++++++++++++++++++++\n")

answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("+++++++++++++++++++++++++++++++\n")

print("total so far: " + str(vars.quizTotal) + "\n")

answer3 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer3
print("+++++++++++++++++++++++++++++++\n")

answer4 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer4
print("+++++++++++++++++++++++++++++++\n")

print("total so far: " + str(vars.quizTotal) + "\n")

answer5 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer5
print("+++++++++++++++++++++++++++++++\n")

answer6 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer6
print("+++++++++++++++++++++++++++++++\n")

print("total so far: " + str(vars.quizTotal) + "\n")

answer7 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer7
print("+++++++++++++++++++++++++++++++\n")

answer8 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer8
print("+++++++++++++++++++++++++++++++\n")

print("total so far: " + str(vars.quizTotal) + "\n")

answer9 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer9
print("+++++++++++++++++++++++++++++++\n")

answer10 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer10
print("+++++++++++++++++++++++++++++++\n")

print("total so far: " + str(vars.quizTotal) + "\n")



# after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)


