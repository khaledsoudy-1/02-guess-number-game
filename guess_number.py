import random

# Generate a random number between 1 and 3 (inclusive)
computer_number = random.randint(1, 3)

# Ask the player to guess the number
player_number = int(input("Guess which number I'm thinking of .. 1, 2 or 3:\n"))

# Check if the player's guess matches the computer's number
if computer_number == player_number:
    print("🎉🎉 You win!")
else:
    print("😢 You Lose!")
