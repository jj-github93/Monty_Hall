from random import randint


class Doors:
    """
    This class holds information of the Door object
    """

    def __init__(self, door_number):
        self.door_number = door_number
        self.winner = False
        self.open = False
        self.user_selection = False


door1 = Doors(1)
door2 = Doors(2)
door3 = Doors(3)

# Adds doors into list
list_of_doors = [door1, door2, door3]


def randomise_winner():
    """
    This function randomly selects a winning door
    winning_door is an int between 1 and 3 inclusive
    :return: winning_door
    """
    winning_door = randint(1, 3)
    return winning_door


def door_selection():
    """
    This functions allows the user to select a door
    user_choice is an int between 1 and 3 inclusive
    :return: user_choice
    """
    # Checks the user entered a valid input
    while True:
        try:
            user_choice = int(input("Select a door 1-3: \n"))
        except ValueError:
            print("Invalid entry, select a door between 1 and 3 inclusive.")
        else:
            if user_choice not in range(1, 4):
                print("Invalid door selected, try again")
            else:
                return user_choice


def switch_door(list_of_doors, user_choice):
    """
    This functions allows the user to switch their selected door
    :param list_of_doors: list of doors within the problem
    :param user_choice: users previously selected door
    :return: user_choice
    """
    while True:
        switch_choice = input("Would you like to switch your door Y/N: \n").upper()
        if switch_choice == "YES" or switch_choice == "Y":
            for door in list_of_doors:
                if not door.user_selection:
                    door.user_selection = True  # Assigns other door to the user
                    list_of_doors[user_choice - 1].user_selection = False  # Retract users previous selection
                    user_choice = door.door_number  # Changes user_choice value to new selection

            print(f"You have chosen to switch to door number {user_choice} ")
            return user_choice
        #
        elif switch_choice == "NO" or switch_choice == "N":
            print(f"You have chosen to stay with door {user_choice}")
            return user_choice

        else:
            print("Invalid selection, try again.")


def monty_hall(list_of_doors):
    """
    This function is a text based Monty Hall Problem
    :param list_of_doors: list of doors within the problem
    """
    winning_door = randomise_winner()
    user_choice = door_selection()

    # Assigns the selected door to the user
    list_of_doors[user_choice - 1].user_selection = True
    # Assigns the winning door
    list_of_doors[winning_door - 1].winner = True

    print(f"You have chosen door number {list_of_doors[user_choice - 1].door_number}")

    """Opens a losing door and removes it from the list"""
    for door in list_of_doors:
        if not door.user_selection and not door.winner:
            print(f"Door {door.door_number} was empty")
            list_of_doors.pop(door.door_number - 1)
            break

    user_choice = switch_door(list_of_doors, user_choice)

    if user_choice == winning_door:
        print(f"You Win. You selected the winning door, door number {winning_door}")
    else:
        print(f"You Lose, the winning door was door number {winning_door}")


def main():
    while True:
        print(monty_hall(list_of_doors))


main()
