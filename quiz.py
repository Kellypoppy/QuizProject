import random

#Storing question
questions = {
    "Math": [
        {"question": "What is 5 + 7?", "options": ["10", "12", "14", "16"], "answer": "12"},
        {"question": "What is 5*9+4?", "options": ["27", "24", "30", "49"], "answer": "49"},
        {"question": "What is 50/25*15?", "options": ["20", "30", "34", "27"], "answer": "30"},
        {"question": "What is 3^2 + 9 * 80?", "options": ["729", "509", "690", "1080"], "answer": "729"},
        {"question": "What is (300+300)/500?", "options": ["0.8", "0.2", "1.9", "1.2"], "answer": "1.2"}
    ],
    "English": [
        {"question": "You need a passport if you want to go ______", "options": ["by plane", "on vacation", "abroad"], "answer": "abroad"},
        {"question": "The food at the restaurant was", "options": ["comfortable", "delicious", "crowded"], "answer": "delicious"},
        {"question": "I __ most of my time at the beach when I'm on a vacation", "options": ["buy", "spend", "go"], "answer": "spend"},
        {"question": "Kylie forgot to ___ the dishes, so there aren't any clean cups", "options": ["shop", "make", "wash"], "answer": "wash"},
        {"question": "Istanbul is an old city with lots of ___ buildings", "options": ["noisy", "modern", "interesting"], "answer": "interesting"}
    ]
}

mark = 0

def calculate(answer, correct, mark):
    if answer == correct:
        mark += 100
        print("+100 mark")
    else:
        print("Incorrect answer")
    return mark

def displayquestion(number, userID):  # Ensure userID is passed as an argument
    global mark 
    
    # Finding out which subject the user wants
    if int(number) == 1:
        category = "Math"
    elif int(number) == 2:
        category = "English"
    else:
        print("Invalid category number")
        return

    # Retrieve the list of questions for the given category from the 'questions' dictionary
    question_list = questions[category]

    # Randomizes the order of the list
    random.shuffle(question_list)

    # Loops through the list
    for question_data in question_list:
        print("Please enter a number:")

        # Prints the questions
        print(f"Question: {question_data['question']}")

        # Loop through the list of options and print each option with its corresponding index starting from 1
        for i, option in enumerate(question_data['options'], 1):
            print(f"{i}. {option}")

        while True:
            try:    
                UserInput = int(input("Answer: "))

                if number == 1 and 1 <= UserInput <= 4:

                    # Stores the user answer, correct answer and marks
                    UserAnswer = question_data['options'][UserInput - 1]
                    CorrectAnswer = question_data["answer"]
                    mark = calculate(UserAnswer, CorrectAnswer, mark)
                    break
                elif number == 2 and 1 <= UserInput <= 3:
                    UserAnswer = question_data['options'][UserInput - 1]
                    CorrectAnswer = question_data["answer"]
                    mark = calculate(UserAnswer, CorrectAnswer, mark)
                    break
                else:
                    print("Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"Your total score is: {mark}")
    # Ensure the userID is valid and correctly passed
    if userID is not None:
        with open('leaderboard.txt', 'a') as file:
            file.write(f"{userID},{category},{mark}\n")
    else:
        print("Invalid user ID. Cannot record score.")
