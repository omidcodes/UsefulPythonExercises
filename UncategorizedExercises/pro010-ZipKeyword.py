x = [1, 4, 3, 9, 14]
y = [6, 7, 8, 9, 10]

Scores = {"Team 1": 0, "Team 2": 0}
for i, j in zip(x, y):
    ekhtelaf = abs(i - j)
    if i < j:
        print('Winner is Team 2. tafazol = {0}'.format(ekhtelaf))
    elif i > j:
        print('Winner is Team 1. tafazol = {0}'.format(ekhtelaf))
    else:
        print('Equal')
    Scores["Team 1"] += i
    Scores["Team 2"] += j

print("-" * 30)
if Scores["Team 1"] > Scores["Team 2"]:
    print("Team 1 is winner with {0} Goals".format(Scores["Team 1"]))
elif Scores["Team 1"] < Scores["Team 2"]:
    print("Team 2 is winner with {0} Goals".format(Scores["Team 2"]))
else:
    print("Two teams are Equal.")