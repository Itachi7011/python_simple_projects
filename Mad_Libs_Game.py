# Mad Libs Game in Python


print("Welcome to the Mad Libs Game!")


# Get user input for the story

name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")


# The story with placeholders

story = f"Once upon a time, in a land far, far away, there lived a {adjective1} person named {name}. "

story += f"They had a {adjective2} {animal} as a pet and loved to eat {food}. "

story += f"One day, they stumbled upon a {adjective3} {noun1} in the forest. "

story += f"It was filled with {noun2} and treasures beyond their wildest dreams."


# Print the completed story

print("Here is your Mad Libs story:")

print(story)