"""
Program is the simulation of the monty hall problem.You specify the number of doors to be used and it chooses a  door to open randomly. Monty hall opens  a door with no prize. It randomly chooses whether to switch to another door or retain the same door.It calculates the chances of winning in retaining the door and the chances of winning in switching doors.
"""

from random import randint

number_of_doors = eval(input("Enter the number of doors"))
doors = []
switch = [True, False]

score1 = 0
score2 = 0


def choose_door(num_doors):
    return randint(0, num_doors)


for i in range(number_of_doors):
    doors.append("goat")


def monty_game():
    prize = randint(0, number_of_doors - 1)
    doors[prize] = "prize"
    global doorOpened
    doorOpened = choose_door(number_of_doors)

    closedDoors = []

    monty_hall = choose_door(number_of_doors)

    while monty_hall == prize or monty_hall == doorOpened:
        monty_hall = choose_door(number_of_doors)

    for j in range(number_of_doors):
        if j != monty_hall and j != doorOpened:
            closedDoors.append(j)

    switched = switch[randint(0, 1)]
    results = []
    if switched:
        index = randint(0, len(closedDoors)-1)
        new_door = closedDoors[index]

        results.append(True)

        if new_door == prize:
            results.append(True)
        else:
            results.append(False)
    else:
        results.append(False)
        if doorOpened == prize:
            results.append(True)
        else:
            results.append(False)

    return results


for i in range(10000):
    Results = monty_game()
    if Results[0] and Results[1]:
        score1 += 1
    elif not (Results[0]) and Results[1]:
        score2 += 1

Switching1= score1/10000 *100
Switching2= score2/10000 *100

print("Switched:", Switching1)
print("without switshing:", Switching2)
