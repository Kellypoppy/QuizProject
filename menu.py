# ************************************************************************* 
# Program: menu.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL2L 
# Trimester: 2430 
# Names: YAP LI XUAN | ERYNE CHUAH EE WEN
# IDs: 242FC242JW | 242FC2432F
# Emails: YAP.LI.XUAN@student.mmu.edu.my | ERYNE.CHUAH.EE@student.mmu.edu.my
# ************************************************************************* 

from leaderboard import leaderboard
from quiz import displayquestion

def quiz_menu(userID):
    #userID: The ID of the user taking the quiz.
    while True:
        print("\nWhich subject do you want to try?\n")
        print("MATH (1) ENGLISH (2) Exit (0)")
        
        try:
            # Get user input and convert to an integer
            number = int(input("Enter number: "))
        except ValueError:
            # Handle non-integer inputs
            print("Invalid input! Please enter a number.")
            continue

        if number == 0:
            print("Exiting quiz menu.")
            from restart_exit import restart_or_exit
            if not restart_or_exit():
                break   # Exit the quiz menu and go restart function
        elif 0 < number < 3:
            displayquestion(number, userID)  # Takes subject and userID as arguments

            while True:
              print("Do you want to check leaderboard?\n")  # Ask if user wants to check the leaderboard
              user_input = input("Yes or No?\n").upper()

              if user_input == "YES":
                  leaderboard(number) # Go to leaderboard function
                  break  
              elif user_input == "NO":
                 # Return to quiz selection if user does not want to check leaderboard
                 print("Going back to quiz selection...")
                 break
              else:
                 # Handle invalid input for leaderboard choice
                  print("Please enter a valid input.")

        else:
            # Handle invalid subject selection
            print("Please enter a number between 0-2.")