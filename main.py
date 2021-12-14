#Using the random module to createe random numbers in the guessing game
import random, sys, os, math

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
print("You have 6 guesses to find the secret number.")

for guessTaken in range(1,7): #range start at 1 and end at 6
    print("Take a guess.")
    guess = int(input()) #input take in a user response

    if guess < secretNumber: #if statment is a condition that must be met to end with different results
      print("Your guess is too low.")
    elif guess > secretNumber:
      print("your guess is too high")
    else:
      break
if guess == secretNumber:
    print(f"Good job! You guess my number in {str(guessTaken)}")
else:
  print(f"Nope. The number I was thinking of was {secretNumber}")