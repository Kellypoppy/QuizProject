import random 
import calculate

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

def displayquestion(number):
    if number == 1:
        category = "Math"
    if number == 2:
        category  = "English"
    
    for i in questions[category]:
        question_data=random.choice(questions[category])
        print(f"Question: {question_data['question']}")
        for i, option in enumerate(question_data['options'], 1):
            print("Please enter number")
            print(f"{i}. {option}")
            
        UserInput=int(input("Answer: "))
        CorrectAnswer=question_data["answer"]
        if UserInput <= 4:
           calculate.calculate(UserInput,CorrectAnswer)
        else:
            print("Please enter correct number")
            
           
        
    

