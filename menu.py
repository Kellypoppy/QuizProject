# ************************************************************************* 
# Program: main.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL2L 
# Trimester: 2430 
# Names: YAP LI XUAN | ERYNE CHUAH EE WEN
# IDs: 242FC242JW | 242FC2432F
# Emails: YAP.LI.XUAN@student.mmu.edu.my | ERYNE.CHUAH.EE@student.mmu.edu.my
# ************************************************************************* 

from leaderboard import leaderboard
from quiz import displayquestion
from testing import login, register


def menu():
  print("Welcome to the quiz")
  print("1.Register")
  print("2.login")
  choice=int(input("Enter: "))
  if choice == 1:
     print("Register")
     userID=register()
     menu()
  elif choice == 2:
     print("Login")
     userID=login()
  else:
     print("Invalid number please try again")
     menu()
   # Only proceed if login was successful
  if userID:
     print("Which subject do you want to try?")
     print("EXIT(0) MATH(1) ENGLISH(2) Leaderboard(3)")
     number=int(input("Enter number: "))
     if number !=0:
        if number < 3:
          displayquestion(number,userID)

        else:
          leaderboard()
     else:
       return
  
menu()