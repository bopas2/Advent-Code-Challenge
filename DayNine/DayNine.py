num_of_players = 424  
num_of_marbles = 71482 * 100
scoreboard = {}
circle = []
cursor = 0
for i in range(num_of_players):
    scoreboard[i] = 0
for marble_id in range(num_of_marbles + 1):
    if marble_id == 0:
        circle.append(marble_id)
    elif marble_id % 23 == 0:
        scoreboard[(marble_id % num_of_players)] += marble_id + circle[cursor - 7]
        cursor -= 7
        if cursor < 0:
            cursor = len(circle) + cursor
        del circle[cursor]
    else:
        if cursor + 2 == len(ccircle): 
            circle.append(marble_id)
            cursor += 2
        elif cursor + 2 < len(circle):
            new_circle = circle[:cursor + 2]
            new_circle.append(marble_id)
            new_circle += circle[cursor + 2:]
            circle = new_circle
            cursor += 2
        else:
            new_circle = circle[:len(circle) - cursor]
            new_circle.append(marble_id)
            new_circle += circle[len(circle) - cursor:]
            cursor = len(circle) - cursor
            circle = new_circle

bestID = 0
bestScore = 0
for x in scoreboard:
    if scoreboard[x] >= bestScore:
        bestScore = scoreboard[x]
        bestID = x
print(bestScore)
