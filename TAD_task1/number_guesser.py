import random

print("Welcome to number guesser game! \n")
print("Guess number between 1 to 10")
max_tries = int(input("Enter the maximum number of tries: "))
guess = int(input("Enter your guess: "))
c = 1
ans = random.randint(1,10)
#looping to check if the guess is correct
while(guess!=ans):
    guess = int(input("Oops! Wrong guess. Try again: "))
    c += 1 #incrementing the number of tries
    if(c>=max_tries):
        print("You have exceeded the maximum number of tries. Game over!\nThe answer was", ans)
        break
if(guess==ans):
    print("Yay! The answer was indeed", ans)
    print("You guessed the number in", c, "tries")
