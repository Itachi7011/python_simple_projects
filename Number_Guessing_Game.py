print("Welcome to the Guessing Game!")

# Set the number to be guessed
number_to_guess = 42

# Set the number of attempts
attempts = 0

# Set the maximum number of attempts
max_attempts = 5


while attempts < max_attempts:

    # Get user input for the guess

    guess = input("Guess a number between 1 and 100 (Max. Attemps = 6): ")

    # Check if the input is a valid number

    try:

        guess = int(guess)

    except ValueError:

        print("Error: Invalid input! Please enter a number.")

        continue

    # Check if the guess is in the correct range

    if guess < 1 or guess > 100:

        print("Error: Number out of range! Please enter a number between 1 and 100.")

        continue

    # Increment the number of attempts

    attempts += 1

    # Check if the guess is correct

    if guess == number_to_guess:

        print(f"Congratulations! You guessed the number in {attempts} attempts.")

        break

    elif guess < number_to_guess:

        print("Too low! Try again.")

    else:

        print("Too high! Try again.")


# Check if the user ran out of attempts

if attempts == max_attempts:

    print(f"Sorry, you didn't guess the number. The number was {number_to_guess}.")
