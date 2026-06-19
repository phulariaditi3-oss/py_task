print("--------GAME SCORE CALCULATOR-------------")
no=int(input("enter how many players play:"))
scores={}
for i in range(no):
    name=input(f"Enter name of player {i+1}: ")
    score=input(f"enter score of {name} :")
    scores[name]=score
print("-----------players Board---------")
for name,score in scores.items():
    print(name ,":",score)
print("------scoreboard--------")
winner=max(scores,key=scores.get)
print("winner:",winner)
print("scoes:",scores[winner])
print(f"Congratulations {winner}")

   




