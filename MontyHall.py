import random

class Doors:
    def __init__(self, door_number):
        self.door_number = door_number
        self.winner = False
        self.open = False
        self.user_selection = False

door1 = Doors(1)
door2 = Doors(2)
door3 = Doors(3)

doorList = [door1, door2, door3]

def randomise_winner(door_list):
    random.choice(door_list).winner = True

def monty_problem(door_list):
    for door in doorList:
        if door.winner == False and door.user_selection == False:
            door.open == True
            print(f"Door {door.door_number} was empty")
            break

















