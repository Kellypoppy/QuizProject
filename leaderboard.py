def leaderboard():
    file=open('leaderboard.txt','a')
    score_list=list(file)
    print("Top three score")
    score_list.sort(key=lambda x: x[1], reverse=True)
    for i in range(min(3,len(score_list))): # make sure index wont out of range
       print(f"{score_list[i][0]} {score_list[i][1]}")

