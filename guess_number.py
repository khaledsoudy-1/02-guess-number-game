import random

def guess_number():
    while True:
        # Generate a random number between 1 and 3 (inclusive)
        computer_number = random.randint(1, 3)
        
        try:
            # Ask the player to guess the number
            player_number = int(input("Guess which number I'm thinking of .. 1, 2 or 3:\n"))
            
            # Check if the player's guess matches the computer's number
            if computer_number == player_number:
                print("\n🎉🎉 You win!")
            else:
                print("\n😢 You Lose!")

        except ValueError:
            print("Invalid input!! Please enter a number.\n")
            continue
        
        # Ask user if they want to play again.
        print("\nPlay again?!")
        playagain = input("Y for Yes\nQ to Quit\n").strip().lower()
        
        # Validate input.
        while playagain not in ["y", "q"]:
            playagain = input("Y for Yes\nQ to Quit\n").strip().lower()
            
        # Determine the winner.
        if playagain == "y":
            print("==== Welcome Back 😍 ====")
            continue
        else:
            print("\n🎉🎉🎉🎉\nThank you for playing\nBye 👋")
            break
        

if __name__ == '__main__':
    guess_number()