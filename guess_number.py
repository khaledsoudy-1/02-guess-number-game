import random


def guess_number():
    # Add some counters for a better game.
    game_counter = 0
    player_wins = 0
    computer_wins = 0
    
    while True:
        # Generate a random number between 1 and 3 (inclusive)
        computer_number = random.randint(1, 3)
        
        try:
            # Ask the player to guess the number
            player_number = int(input("Guess which number I'm thinking of .. 1, 2 or 3:\n"))
            
            # Validate player input.
            if player_number not in [1, 2, 3]:
                print("Please enter a number between 1 and 3.\n")
                continue
                
            # Display player and computer numbers.
            print(f"\nYou chose: {player_number}\nComputer chose: {computer_number}\n")
        
            def decide_winner(player, computer):
                nonlocal game_counter
                nonlocal player_wins
                nonlocal computer_wins
               
                # Check if the player's guess matches the computer's number
                if player == computer:
                    player_wins += 1
                    return "🎉🎉 You win!"
                else:
                    computer_wins += 1
                    return f"Sorry ... better luck next time. 😢"
        
            game_result = decide_winner(player_number, computer_number)
            print(game_result)
            game_counter += 1
        
        except ValueError:
            print("Invalid input!! Please enter a number.\n")
            continue
    
        # Display The counters
        print(f"\nGame Count: {game_counter}")
        print(f"Your wins: {player_wins}")
        print(f"Computer Wins: {computer_wins}")
    
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
    print("===== Welcome To The Guess Number Game 🎲 =====")
    guess_number()
