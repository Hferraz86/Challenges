#!/usr/bin/python3

# Step 1: Assign a list of ten string elements representing Benfica players to a variable
benfica_players = [
    "Turbin", "Otamendi", "Bah", "Antonio Silva", "Di Maria", 
    "Rafa", "Arthur Cabral", "Neres", "João Neves", "Tiago Gouveia"
]

# Step 2: Print the fourth player from the list 
# In Python, indexing starts at 0, so the fourth player has index 3 in the list.
print("Fourth player from the list:", benfica_players[3])

# Step 3: Print players from the sixth to the tenth position of the list
print("Players from the sixth to the tenth position of the list:", benfica_players[5:10])

# Step 4: Change the value of the seventh element of the list to "Oscar Cardozo"
benfica_players[6] = "Oscar Cardozo"
print("If the world were fair, this change would happen:", benfica_players)
