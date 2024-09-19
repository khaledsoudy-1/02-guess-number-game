import random
import sys


def computer_guess_number():
    # Ask user to think of a secret number.
    print("\nThink of a number between 1 and 100 .. and I will try to guess it.\n")
    input("Press Enter when you're ready...\n")
    
    # Initialize a counter for attempts
    computer_attempts = 0
    
    # Initialize game limits
    low = 1
    high = 100
    
    while True:
        # Let the computer make a random guess.
        computer_guess = random.randint(low, high)
        print(f"My guess is: {computer_guess}")
        
        # Increment and display computer attempts each round.
        computer_attempts += 1
        print(f"\nAttempt #{computer_attempts}\n")
        
        # Get Feedback from user.
        feedback = input(f"Is {computer_guess} Correct (C), Too Low (L), or Too High (H)?\n").strip().lower()
        
        # Validate the feedback
        while feedback not in ["c", "l", "h"]:
            print("\nYou must enter C, L or H.")
            feedback = input(f"Is {computer_guess} Correct (C), Too Low (L), or Too High (H)?\n").strip().lower()
        
        # Adjust the range based on the feedback
        if feedback == "l":
            low = computer_guess + 1
        
        elif feedback == "h":
            high = computer_guess - 1
        
        else:
            print(f"\n🎉🎉 Yey! I guessed your number correctly in only {computer_attempts} attempts!!")
            break
            
        # Check for conflicts in the range
        if low > high:
            print("\nOops! Something went wrong with your inputs. The range is invalid.")
            print("Let's try again, but please be careful with your responses.")
            low, high = 1, 100  # Reset the range

    
    # Ask user if they want to play again.
    print("\nPlay again?!")
    playagain = input("Y for Yes\nQ to Quit\n").strip().lower()
    
    # Validate play again input.
    while playagain not in ["y", "q"]:
        playagain = input("Y for Yes\nQ to Quit\n").strip().lower()
        
    if playagain == "y":
        print("===== Welcome Back 😍 =====")
        return computer_guess_number()
    
    if playagain == "q":
        print("\n🎉🎉🎉🎉\nThank you for playing\nBye 👋")
        sys.exit()


if __name__ == '__main__':
    print("===== Welcome To The Guess Number Game 🎲 =====")
    computer_guess_number()