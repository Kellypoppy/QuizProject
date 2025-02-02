# ************************************************************************* 
# Program: mwnu.py 
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
     print("Registering...")
     register()
     menu()
  elif choice == 2:
     print("Login page")
     userID=login()
  else:
     print("Invalid number please try again")
     menu()
   # Only proceed if login was successful
  while userID:
      print("Which subject do you want to try?\n")
      print("MATH(1) ENGLISH(2) Leaderboard(3) Exit(0)")
      number=int(input("Enter number: "))
      if number == 0:
         return
      elif  0 < number < 3:
          displayquestion(number,userID)
          print("Do you want to check leaderboard?\n")
          UserInput=input("Yes or No?\n").upper()
          if UserInput == "YES":
             leaderboard()
          elif UserInput == "NO":
             print("Going back...")
             continue
          else:
             print("Please enter valid input")

      elif number == 3:
         leaderboard()
         continue
      else:
         print("Please enter between 0-3")

menu()