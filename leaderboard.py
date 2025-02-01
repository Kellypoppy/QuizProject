def leaderboard(score_list):
    list=[["242FC242JW",23],["242FC24203",56],["242FC543",78],["242FC453",89]]
    list.sort(key=lambda x: x[1], reverse=True)
    for i in range(0,3):
       print(f"{list[i][0]} {list[i][1]}")

