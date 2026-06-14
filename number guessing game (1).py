import random
print("===================================")
print("     NUMBER GUESSING GAME")
print("===================================")
print("I am thinking of a number between 1 and 100.")
print("Try to guess it!")
secret_number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it!")
        print("The number was:", secret_number) 
        print("Total attempts:", attempts)
        break
print("Game Over. Thanks for playing!") 
