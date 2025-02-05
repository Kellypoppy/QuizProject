# Register userID and password
def register():

    # User input
    print("Commas are not allowed")
    userID = str(input("Enter user ID: "))
    password = input("Enter password: ")

    # Open the file in append mode to add the new user
    with open('database_testing.txt', 'a') as file:
        # Write the userID and password to the file, separated by a comma
        file.write(userID + "," + password + "\n")
    
    print("Registration successful! Please login.")