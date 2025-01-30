# ************************************************************************* 
# Program: main.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL2L 
# Trimester: 2430 
# Names: YAP LI XUAN | ERYNE CHUAH EE WEN
# IDs: 242FC242JW | 242FC2432F
# Emails: YAP.LI.XUAN@student.mmu.edu.my | ERYNE.CHUAH.EE@student.mmu.edu.my
# ************************************************************************* 

with open('database_testing.txt', 'r') as text_file:
    content = text_file.read()
    print(content)

def register():
    userID = input("Enter user ID: ")
    password = input("Enter password: ")
    with open('database_testing.txt', 'a') as text_file:
        add_user = text_file.write(userID + "\n")
        add_pass = text_file.write(password +  "\n")
    
register()