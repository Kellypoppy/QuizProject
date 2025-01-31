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
    print(content)

# Register userID and password
def register():

    # User input
    userID = input("Enter user ID: ")
    password = input("Enter password: ")

    # Open the file in append mode to add the new user
    with open('database_testing.txt', 'a') as file:
        # Write the userID and password to the file, separated by a comma
        file.write(userID + "," + password + "\n")
    
    print("Registration successful!")

# Login verification
def login():
    i = 0
    max_attempts = 3

    # Loop for attempts
    while i < max_attempts:
        userID = input("Enter user ID: ")
        password = input("Enter password: ")

        # Open the file and check each line
        with open("database_testing.txt", "r") as file:
            # Loops through every line in the txt file
            for line in file:
                # Remove any extra spaces or newlines
                line = line.strip()
                # Ensure the line has the correct format (userID,password)  
                if ',' in line:  
                    # Only split at the first comma 
                    # (ex. if password is 456,23, the comma removed is the 2nd element between id and password in the array, not from the password)
                    stored_userID, stored_password = line.split(",", 1)  
                
                    # Check if the entered userID and password match the stored values
                    if userID == stored_userID and password == stored_password:
                        print("Login successful!")
                        # Exit the function on successful login
                        return  

        # Increment attempts if no match is found
        i += 1
        print(f"Login unsuccessful. Attempts remaining: {max_attempts - i}")

    # If 3 failed attempts, deny access
    print("Access denied.")  

register()

login()
