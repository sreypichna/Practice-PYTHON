scores = {"falcon": 180, "comet": 205, "nova": 160}
 
scores["star"] = 140                # a new team just finished their run
scores["comet"] += 15             # bonus points awarded to comet
 
best_team = None
best_score = -1
 
for team, points in scores.items():
    if points > best_score:
        best_score = points
        best_team = team
 
print(f"Leader: {best_team} with {best_score} points")
