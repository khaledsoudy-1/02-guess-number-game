import random


def guess_number():
    # Ask user to think of a secret number.
    print("\nThink of a number between 1 and 100 .. and I will try to guess it.\n")
    input("Press Enter when you're ready...\n")
    
    # Initialize game limits
    low = 1
    high = 100
    
    while True:
        # Let the computer make a random guess.
        computer_guess = random.randint(low, high)
        print(f"My guess is: {computer_guess}")
        
        # Get Feedback from user.
        feedback = input(f"Is {computer_guess} Correct (C), Too Low (L), or Too High (H)?\n").strip().lower()
        
        while feedback not in ["c", "l", "h"]:
            print("\nYou must enter C, L or H.")
            feedback = input(f"Is {computer_guess} Correct (C), Too Low (L), or Too High (H)?\n").strip().lower()
        
        if feedback == "l":
            low = computer_guess + 1
        
        elif feedback == "h":
            high = computer_guess - 1
        
        else:
            print("\n🎉🎉 Yey! I guessed your number correctly.")
            break


if __name__ == '__main__':
    print("===== Welcome To The Guess Number Game 🎲 =====")
    guess_number()