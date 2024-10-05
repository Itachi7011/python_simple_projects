import random


def game():

    while True:

        user_choice = input("Enter a choice ( 1(rock), 2(paper), 3(scissors) ): ")

        possible_choices = ["rock", "paper", "scissors"]

        computer_choice = random.choice(possible_choices)

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:

            print(f"Both players selected {user_choice}. It's a tie!")

        elif user_choice == "1" or 1:

            if computer_choice == "scissors":

                print("Rock smashes scissors! You win!")

            else:

                print("Paper covers rock! You lose.")

        elif user_choice == "2" or 2:

            if computer_choice == "rock":

                print("Paper covers rock! You win!")

            else:

                print("Scissors cuts paper! You lose.")

        elif user_choice == "3" or 3:

            if computer_choice == "paper":

                print("Scissors cuts paper! You win!")

            else:

                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (yes (y) /no (n)): ").lower()

        while play_again not in ["yes", "no", "y", "n"]:

            play_again = input("Invalid input. Play again? (yes/no): ").lower()

        if play_again in ["no", "n"]:

            break


if __name__ == "__main__":

    game()
