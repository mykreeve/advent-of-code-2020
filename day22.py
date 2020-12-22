from datetime import datetime
import copy

filename="input/day22input.txt"
file=open(filename,"r")
file=file.readlines()

player1 = []
player2 = []
player = 1

now = datetime.now()
for n1,f in enumerate(file):
    f = f.replace('\n','')
    if 'Player' in f:
        pass
    elif f == '':
        player = 2
    elif player == 1:
        player1.append(int(f))
    elif player == 2:
        player2.append(int(f))

play1store = copy.deepcopy(player1)
play2store = copy.deepcopy(player2)

while len(player1) > 0 and len(player2) > 0:
    p1card = player1.pop(0)
    p2card = player2.pop(0)
    if p2card > p1card:
        player2.append(p2card)
        player2.append(p1card)
    else:
        player1.append(p1card)
        player1.append(p2card)

merged = player1 + player2
val = 0
for x in range(len(merged)):
    val += (len(merged)-x)*merged[x]

done = datetime.now()
print ("Answer to part one:", val)
print ("Time taken:", done - now)

time = datetime.now()
player1 = play1store
player2 = play2store
depth = 0

def play_recursive(player1, player2, depth):
    seen = []
    # print (depth, player1, player2)
    while len(player1) > 0 and len(player2) > 0:
        p1 = copy.deepcopy(player1)
        p2 = copy.deepcopy(player2)
        if (p1,p2) in seen:
            return (['winner'], [])
        else:
            seen.append((p1,p2))
        p1card = player1.pop(0)
        p2card = player2.pop(0)
        if len(player1) >= p1card and len(player2) >= p2card:
            p1 = copy.deepcopy(player1[0:p1card])
            p2 = copy.deepcopy(player2[0:p2card])
            outcome = play_recursive(p1,p2,depth+1)
            if len(outcome[1]) == 0:
                # print ("Player 1 wins subgame")
                player1.append(p1card)
                player1.append(p2card)
                # print (player1)
            else:
                # print ("Player 2 wins subgame")
                player2.append(p2card)
                player2.append(p1card)
        elif p2card > p1card:
            player2.append(p2card)
            player2.append(p1card)
        else:
            player1.append(p1card)
            player1.append(p2card)
    return [player1,player2]

play_recursive(player1,player2,depth)

merged = player1 + player2
val = 0
for x in range(len(merged)):
    val += (len(merged)-x)*merged[x]

done = datetime.now()
print ("Answer to part two:", val)
print ("Time taken:", done - now)