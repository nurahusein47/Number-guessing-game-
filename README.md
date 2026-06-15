Number Guessing Game

A Python-based interactive game where the computer randomly selects a number between 1 and 100, and the user tries to guess it using helpful hints.

Objective

The goal of this project is to create a simple Python game where the computer randomly selects a number between 1 and 100, and the user tries to guess it using hints.

Description

This is a simple interactive game built using Python. The computer generates a random secret number, and the user repeatedly tries to guess it. After each guess, the program gives feedback by telling whether the number is too high or too low. The game continues until the correct number is guessed, while counting the number of attempts.

Features

· Random number generation between 1 and 100
· Interactive user input
· Hint system (Too high / Too low)
· Attempt counter
· Loop until correct answer is found

Tech Stack

· Python 3.x
· Command-line interface
· Random module

Installation

1. Make sure Python 3 is installed on your system.
2. Save the code file as number_guessing_game.py.
3. Run the script:
  
   python number_guessing_game.py
   
Usage

1. Launch the program.
2. The computer will randomly select a secret number between 1 and 100.
3. Enter your guess when prompted.
4. After each guess, you will receive a hint:
   · "Too low!" – Your guess is below the secret number
   · "Too high!" – Your guess is above the secret number
   · "Correct!" – You guessed the number
5. The game ends when you guess correctly, and your total attempts are displayed.

Sample Output

Example 1: Guessing in 3 attempts

========================================
     NUMBER GUESSING GAME
========================================

I am thinking of a number between 1 and 100.
Try to guess it!

Enter your guess: 38
Too low! Try again.

Enter your guess: 45
Too high! Try again.

Enter your guess: 40
Correct! You guessed it!
The number was: 40
Total attempts: 3

Game Over. Thanks for playing!
Example 2: Guessing in 5 attempts

I am thinking of a number between 1 and 100.
Try to guess it!

Enter your guess: 25
Too low! Try again.

Enter your guess: 56
Too high! Try again.

Enter your guess: 50
Too high! Try again.

Enter your guess: 40
Too low! Try again.

Enter your guess: 45
Correct! You guessed it!
The number was: 45
Total attempts: 5

Game Over. Thanks for playing!
Concepts Used

· Variables
· Conditional statements (if, elif, else)
· Loops (while loop)
· User input handling
· Random number generation
· Counters (attempt tracking)

Algorithm

1. Start the program
2. Generate a random number between 1 and 100
3. Set attempts counter to 0
4. Ask user for a guess
5. Compare guess with secret number:
   · If guess is too low → show "Too low!" hint
   · If guess is too high → show "Too high!" hint
   · If guess is correct → show success message and number of attempts
6. Repeat until correct guess
7. End program

What I Learned

Through this project, I learned how to use loops, conditions, and random number generation in Python. I also improved my understanding of how to handle user input and build logical step-by-step programs.

Future Improvements

In the future, this project can be improved by:

· Adding difficulty levels
· Limiting the number of attempts
· Adding a scoring system
· Developing a graphical user interface (GUI) version of the game

Conclusion

This project helped me strengthen my understanding of basic Python programming and improved my problem-solving skills by building a simple interactive game.


 the Author

Nura Husein
Student / Beginner Python Developer

This project was developed as part of a learning exercise to strengthen programming fundamentals. Passionate about building small, useful tools and gradually moving into real-world applications.
· GitHub: nurahusein47
· Goal: Continue improving and building more interactive systems with databases and GUIs.

Acknowledgments

· Inspired by classic number guessing games.
· Thanks to Python practice projects that helped build this interactive game.

Version

v1.0 – Basic number guessing game with hints and attempt counter (command-line based)

License

This project is for educational purposes only.
