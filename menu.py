from leaderboard import leaderboard
from leaderboard import displayquestion


score_list=[]

def menu():
 print("Which subject do you want to try?")
 print("EXIT(0) MATH(1) ENGLISH(2) Leaderboard(3)")
 number=int(input("Enter number: "))
 if number !=0:
     if number < 3:
        displayquestion.displayquestion(number)
     else:
       leaderboard.leaderboard(score_list)
 else:
    pass