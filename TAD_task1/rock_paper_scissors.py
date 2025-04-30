import random
#function to get user choice
def user_choice():
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1-3): ")
        
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice! Please enter 1, 2, or 3.")

#function to get computer choice
def computer_choice():
    return random.randint(1, 3)

#function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "user"
    else:
        return "computer"

#function to print the choices
def print_choices(user_choice, computer_choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

#main function
def main():
    print("Welcome to Rock Paper Scissors!")
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = user_choice()
        computer_choice = computer_choice()
        
        print_choices(user_choice, computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        
        ch = input("\nDo you want to play again? (y/n): ").lower()
        if ch != 'y':
            print("\nThanks for playing!")
            break
#calling the main function
main()





