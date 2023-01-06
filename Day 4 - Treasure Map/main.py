#treasure map with nested if statements
#we want 3 rows and 3 columns
#we want to print a map with a treasure in a random location

import random

#generate random row and column
row = random.randint(0,2)
column = random.randint(0,2)

#generate map
map = [[0,0,0],[0,0,0],[0,0,0]]
map[row][column] = "X"

#user input
guess_row = int(input("Guess a row: "))
guess_column = int(input("Guess a column: "))
print(f"{guess_row}, {guess_column}")

#check if user is right
if guess_row == row and guess_column == column:
    print("You found the treasure!")
else:
    print("You didn't find the treasure.")
    if guess_row > row:
        print("You are too far down.")
    elif guess_row < row:
        print("You are too far up.")
    if guess_column > column:
        print("You are too far right.")
    elif guess_column < column:
        print("You are too far left.")

#check if user is close
if guess_row == row or guess_column == column:
    print("You are close.")
else:
    print("You are far away.")

#check if user is on the map
if guess_row > 2 or guess_row < 0 or guess_column > 2 or guess_column < 0:
    print("You are off the map.")

#show map
print(f"{map[0]}{map[1]}{map[2]}")