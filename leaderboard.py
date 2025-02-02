def leaderboard():
    # Open leaderboard file
    with open('leaderboard.txt', 'r') as file:
        score_list = [line.strip().split(",") for line in file]  # Split each line by comma and remove trailing newlines
    
    # Ensure there are at least three values in each line before processing
    score_list = [[score[0], int(score[2])] for score in score_list if len(score) > 2]

    if not score_list:
        print("No valid scores found in the leaderboard.")
        return
    
    print("Top three scores")
    
    # Sort the score_list by the score in descending order
    score_list.sort(key=lambda x: x[1], reverse=True)
    
    # Display top three scores
    for i in range(min(3, len(score_list))):  # Ensure index won't go out of range
        print(f"{score_list[i][0]} {score_list[i][1]}")




