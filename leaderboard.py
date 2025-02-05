def leaderboard(number):
    # Enter code that might raise errors
    try:
        # Open leaderboard file and read data
        with open('leaderboard.txt', 'r') as file:
            score_list = [
                # Split each line by comma and remove empty lines & whitespace by looping through every line of the leaderboard.txt
                line.strip().split(",") 
                for line in file 
                if line.strip()
                ]
              
        # Convert the number into a subject name for comparison
        category = "Math" if number == 1 else "English"

        score_list = [
            # Arranging the data to be the format (userID, subject, score)
            [score[0], score[1], int(score[2])] 

            # Loops through every line
            for score in score_list 

            # Makes sure the total elements per line is 3 and 1st index is the subject
            if len(score) == 3 and score[1] == category
        ]

        # Prints statement if score_list is invalid
        if not score_list:
            print(f"No valid scores found for {category}.")
            return
        
        # Prints the leaderboard
        print(f"Top three scores for {category}:")

        # Sort the score_list by the score in descending order
        # key=lambda x: x[2] => assigns the value of the 3rd element in score_list list to the variable 'key'
        score_list.sort(key=lambda x: x[2], reverse=True)
        
        # Display top three scores
        for i in range(min(3, len(score_list))):  # Ensure index won't go out of range
            print(f"UserID: {score_list[i][0]}, Score: {score_list[i][2]}")

    # Prints the error encountered
    except Exception as e:
        print(f"An error occurred: {e}")

input()