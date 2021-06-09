from random import randint
from Monty_Hall.database.data_management import User


class Doors:
    """
    This class holds information of the Door object
    """

    def __init__(self, door_number):
        self.door_number = door_number  # Assigns the door a number to be referenced
        self.winner = False  # Determines if the door is a winner/loser
        self.user_selection = False  # Determines if the user has selected this door
        self.door_open = False
        self.reset()

    def reset(self):
        """
        Resets the attributes of the door objects.
        """
        self.winner = False
        self.user_selection = False
        self.door_open = False


class MontyHall(Doors):
    """
        This Class hold information of the game.
        Also encapsulates all the methods for the game.
    """

    def __init__(self):
        self.wins = 0
        self.games = 0
        self.losses = 0
        self.win_loss = 0.0

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
        """
            Function allowing the user to select a door between 1-3
            :return: user_choice
        """
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

    def monty_hall(self, list_of_doors):
        """
        This function is a text based Monty Hall Problem
        :param list_of_doors: list of doors within the problem
        """

        # Adds to the attribute games (played)
        self.games += 1

        # function randomly assigns a winner
        winning_door = MontyHall.randomise_winner()

        # input function need to be created to be called
        user_choice = MontyHall.door_selection()

        # Assigns the selected door to the user
        list_of_doors[user_choice - 1].user_selection = True

        # Assigns the winning door
        list_of_doors[winning_door - 1].winner = True

        """Opens a losing door and removes it from the list"""
        for door in list_of_doors:
            if not door.user_selection and not door.winner:
                print(f"Door {door.door_number} was empty")
                door.door_open = True  # Sets the open parameter to true
                break

        user_choice = MontyHall.switch_door(list_of_doors, user_choice)  # User may change their door
        self.tell_winner(winning_door, user_choice)

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
                    if not door.user_selection and not door.door_open:
                        door.user_selection = True  # Assigns other door to the user
                        list_of_doors[user_choice - 1].user_selection = False  # Retract users previous selection
                        user_choice = door.door_number  # Changes user_choice value to new selection
                        break

                return user_choice
            #
            elif switch_choice == "NO" or switch_choice == "N":
                return user_choice

            else:
                print("Invalid selection, try again.")

    def tell_winner(self, winning_door, user_choice):
        """
          Function to determine if the user has won.
          Checking the user selected door with the winning door
        """
        if winning_door == user_choice:
            print(f"You have chosen door number {user_choice}. \nThe winning door is {winning_door}. You Won!")
            self.wins += 1

        else:
            print(f"You have chosen door number {user_choice}. \nThe winning door is {winning_door}. You Lost!")
            self.losses += 1

    @staticmethod
    def play_again(playing, door1, door2, door3):
        """
            Give the user the option to play the game again.
            Resets the objects parameter or exits the program.
        """
        while True:
            play_again = input("Would you like to play again? \n").upper()
            if play_again == "Y" or play_again == "YES":
                # Resets the attributes to original status
                door1.reset()
                door2.reset()
                door3.reset()
                return playing
            elif play_again == "N" or play_again == "NO":
                playing = False
                return playing
            else:
                print("Unknown response, try again.")

    def scoreboard(self):
        """
            Function calculate the users win/loss.
            Prints a scoreboard of the users game statistics.
        """
        self.win_loss = float("{:.3f}".format(self.wins / self.games))

        print("\n{0:<10}{1:>5}\n{2:<10}{3:>5}\n{4:<10}{5:>5}\n{6:<10}{7:^10}\n"
              .format("Games:", self.games, "Wins:", self.wins, "Losses:",
                      self.losses, "Win/Loss:", self.win_loss))


def main():
    db = "sqlite:///database/users.db"

    User.init_db(db)

    user_name = User.add_user(db)

    # Create playing variable
    playing = True

    # Create door objects
    door1 = Doors(1)
    door2 = Doors(2)
    door3 = Doors(3)

    # Adds doors into list
    doors_list = [door1, door2, door3]

    # Create MontyHall Object
    game = MontyHall()

    while playing:
        game.monty_hall(doors_list)
        game.scoreboard()
        playing = MontyHall.play_again(playing, door1, door2, door3)

    User.update_user(user_name, game.games, game.wins, game.losses, game.win_loss, db)



if __name__ == "__main__":
    main()
