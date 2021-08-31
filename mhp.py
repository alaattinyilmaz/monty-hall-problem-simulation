import random

# Number of trials
N = 100000

not_change_success = 0
change_success = 0

for trial in range(N):

	# Creating doors
	doors = [0 for k in range(3)]
	fill_car_door = random.randint(0,2)

	# Marking one door as car
	doors[fill_car_door] = 1

	# Choosing a door randomly
	choice = random.randint(0,2)

	# Opening a goat door

	for gd, door in enumerate(doors):
		if(gd != choice and door == 0):
			goat_door = gd
			break;

	doors[goat_door] = "opened"

	# CASE1: Do not change door

	if(doors[choice] == 1):
		not_change_success += 1

	# CASE2: change door

	if(goat_door == 0):
		choice = 3 - choice
	elif(goat_door == 1):
		choice = 2 - choice
	elif(goat_door == 2):
		choice = 1 - choice

	if(doors[choice] == 1):
		change_success = change_success + 1

print("Do not change door success probability: ",not_change_success / N)
print("Change door success probability: ",change_success / N)
