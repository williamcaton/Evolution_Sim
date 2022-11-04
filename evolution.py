import random
creatures = [[1 for x in range(2)] for y in range(20)] 
count = 0
days = 100
totalfood = 10
alive = 20
for i in range(20):
    creatures[i][1] = 5
while count < days:
    print(creatures)
    for i in range(20):
        if creatures[i][0] > 0:
            if random.randint(0,10) > ((creatures[i][1]*(totalfood/alive))):
                creatures[i][0] = 0
                alive -= 1
            if random.randint(0,10) > 8 and creatures[i][1] > 4: #chance to reproduce
                for j in range(20):#scan for empty slots
                    if creatures[j][0] == 0:
                        creatures[j][0] = 1
                        alive += 1
                        creatures[j][1] = creatures[i][1] + random.randint(-2,2)
        if creatures[i][1] < 1: #no negatives
            creatures[i][1] = 1
        if creatures[i][0] < 1: #creature dead
            creatures[i][0] = 0
            creatures[i][1] = 0
        if creatures[i][1] > 9:
            creatures[i][1] = 9
    count += 1
print(creatures)
