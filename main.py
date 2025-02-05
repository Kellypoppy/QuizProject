# ************************************************************************* 
# Program: main.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL2L 
# Trimester: 2430 
# Names: YAP LI XUAN | ERYNE CHUAH EE WEN
# IDs: 242FC242JW | 242FC2432F
# Emails: YAP.LI.XUAN@student.mmu.edu.my | ERYNE.CHUAH.EE@student.mmu.edu.my
# ************************************************************************* 

# Open the file as read mode
with open('database_testing.txt', 'r') as text_file:
    content = text_file.read()
    print("The data below shows the data added into the database. Feel free to create or login using one of them.")
    print(content)

def main():
    # Keep the menu running until the user exits
    while True:  
        print("Welcome to the quiz")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Enter choice: "))
        
        # Handles the error if user inputs other things
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            print("Register page")
            import register  # Go to register function
            register.register()  
        elif choice == 2:
            print("Login page")
            import login #Go to login function then menu if verified
            userID = login.login()
            import menu
            menu.quiz_menu(userID)
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            input()
            break  # Exit the loop and end the program
        else:
            print("Invalid number. Please try again.")
    
main()