def register():
    userID = input("Enter user ID: ")
    password = input("Enter password: ")

    # Open the file in append mode to add the new user
    with open('database_testing.txt', 'a') as file:
        # Write the userID and password to the file, separated by a comma
        file.write(userID + "," + password + "\n")
    
    print("Registration successful!")

def login():
    i = 0
    max_attempts = 3
    
    while i < max_attempts:
        userID = input("Enter user ID: ")
        password = input("Enter password: ")

        # Open the file and check each line
        with open("database_testing.txt", "r") as file:
            for line in file:
                # Strip leading/trailing spaces and split by comma
                line = line.strip()  # Remove any extra spaces or newlines
                if ',' in line:  # Ensure the line has the correct format (userID,password)
                    stored_userID, stored_password = line.split(",", 1)  # Only split at the first comma
                
                    # Check if the entered userID and password match the stored values
                    if userID == stored_userID and password == stored_password:
                        print("Login successful!")
                        return userID # Exit the function on successful login

        # Increment attempts if no match is found
        i += 1
        print(f"Login unsuccessful. Attempts remaining: {max_attempts - i}")

    print("Access denied.")  # If 3 failed attempts, deny access


