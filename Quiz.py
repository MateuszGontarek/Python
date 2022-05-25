import os
import time
class question:
    def __init__(self, ValueQuestion, correctAnswer, index, answer):
        self.ValueQuestion = ValueQuestion
        self.correctAnswer = correctAnswer
        self.index = index
        self.Answer = answer
    def show(self):
        print("Numer pytania: " + str(self.index))
        for i in range(4):
            print(self.Answer[i])
        answer = input("Wprowadź Odpowiedź: ")
        if answer ==  self.correctAnswer:
            print("Poprawna Odpowiedź")
            return True
        else:
            print("Błędna Odpowiedź, poprawną była: " + str(self.Answer[i]))
            return False

score = 0
clear = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')
Question = [
    ["CONTENT OF THE QUESTION","CORRECT ANSWER",['ANSWER 1', 'ANSWER 2', 'ANSWER 3', 'ANSWER 4']]
    ["dfergg","B",["A","B","C","D"]],
    ["defwgeth","C",["A","B","C","D"]],
    ["nyjuk8uik8","A",["A","B","C","D"]],
    ["jikipluku","D",["A","B","C","D"]]
    ]

for i in range(len(Question)):
    Q = question(Question[i][0],Question[i][1], i, Question[i][2])
    clear()
    if Q.show() == True: score += 1
    time.sleep(1)
    del(Q)
    
print("Ilość procent poprawncyh odpowiedzi " + str(score / len(Question) * 100) + "%")

