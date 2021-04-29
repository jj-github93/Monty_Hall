from random import randint


class Doors:
    """
    This class holds information of the Door object
    """

    def __init__(self, door_number):
        self.door_number = door_number  # Assigns the door a number to be referenced
        self.winner = False  # Determines if the door is a winner/loser
        self.user_selection = False  # Determines if the user has selected this door
        self.reset()

    def reset(self):
        """
        Resets the attributes of the door objects.
        """
        self.winner = False
        self.user_selection = False

    @staticmethod
    def randomise_winner():
        """
        This function randomly selects a winning door
        winning_door is an int between 1 and 3 inclusive
        :return: winning_door
        """
        winning_door = randint(1, 3)
        return winning_door

    @staticmethod
    def door_selection():
        """User selects a door"""
        while True:
            try:
                user_choice = int(input("Choose a door 1-3: \n"))

            except ValueError:
                print("Your choice should be numeric. Try again")

            else:
                if user_choice not in range(1, 4):
                    print("Your should be from 1-3 inclusive. Try again")

                else:
                    print(f"You have chosen door {user_choice}")
                    return user_choice

    @staticmethod
    def monty_hall(list_of_doors):
        """
        This function is a text based Monty Hall Problem
        :param list_of_doors: list of doors within the problem
        :param winning_door: winning door number
        :param user_choice: users selected door
        """

        winning_door = Doors.randomise_winner()
        user_choice = Doors.door_selection()  # input function need to be created to be called

        # Assigns the selected door to the user
        list_of_doors[user_choice - 1].user_selection = True
        # Assigns the winning door
        list_of_doors[winning_door - 1].winner = True

        """Opens a losing door and removes it from the list"""
        for door in list_of_doors:
            if not door.user_selection and not door.winner:
                print(f"Door {door.door_number} was empty")
                break

        user_choice = Doors.switch_door(list_of_doors, user_choice)  # User may change their door
        Doors.tell_winner(winning_door, user_choice)

    @staticmethod
    def switch_door(list_of_doors, user_choice):
        """
        This functions allows the user to switch their selected door
        :param list_of_doors: list of doors within the problem
        :param user_choice: users selected door
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

    @staticmethod
    def tell_winner(winning_door, user_choice):
        """
          Function to determine if the user has won. Checking the user selected door with the winning door
        """
        if winning_door == user_choice:
            print(f"You have chosen door number {user_choice}. The winning door is {winning_door}. You Won!")

        else:
            print(f"You have chosen door number {user_choice}. The winning door is {winning_door}. You Lost!")

    @staticmethod
    def play_again():
        while True:
            play_again = input("Would you like to play again? \n").upper()
            if play_again == "Y" or play_again == "YES":
                door1.reset()
                door2.reset()
                door3.reset()
                return
            elif play_again == "NO" or play_again == "NO":
                exit()
            else:
                print("Unknown response, try again.")
                return play_again()


door1 = Doors(1)  # Create door objects
door2 = Doors(2)
door3 = Doors(3)

# Adds doors into list
list_of_doors = [door1, door2, door3]


def main():
    while True:
        Doors.monty_hall(list_of_doors)
        Doors.play_again()


if __name__ == "__main__":
    main()
