
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a simple Hangman game in Python so students practice string manipulation, loops, conditionals, and user input handling. The game should be playable from the command line and have clear win/lose behavior.

## 📝 Tasks

### 🛠️	Build the Hangman game

#### Description
Create a command-line Hangman game. The program should randomly select a word from a predefined list and let the player guess letters until they either guess the full word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses and reveal correct letters in the displayed progress (e.g., `_ a _ _ _`)
- Track and display remaining incorrect attempts
- End when the word is guessed or attempts are exhausted
- Display a clear win or lose message and reveal the word if the player loses

#### Example interaction
```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Good guess! Word: _ a _ _ _
Incorrect guesses left: 5
```

### 🛠️	(Stretch) Add difficulty modes (optional)

#### Description
Optionally add difficulty modes that change the allowed incorrect attempts or choose longer words.

#### Requirements
- Implement at least two difficulty levels (e.g., Easy/Hard)
- Document how to run the program with a selected difficulty in the README
