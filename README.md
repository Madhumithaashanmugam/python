# These are the mini one-day projects I've completed while learning Python.


# Blackjack Game

## Overview
This is a simple console-based Blackjack game implemented in Python. The game simulates a standard Blackjack game where the player competes against the dealer. The game includes features such as shuffling a deck of cards, dealing cards, calculating hand values, and determining the winner based on standard Blackjack rules.

## Features
- **Deck of Cards**: A deck containing 52 cards across four suits: Spades, Clubs, Hearts, and Diamonds.
- **Card Dealing**: Cards are dealt to both the player and the dealer, with the ability to "hit" (draw more cards) or "stand" (end your turn).
- **Blackjack Detection**: Automatically checks for Blackjack (a hand value of 21) for both the player and the dealer.
- **Bust Condition**: Detects if the player's or dealer's hand exceeds 21, resulting in a bust.
- **Game Rounds**: Supports multiple rounds of play within a single session.
- **Dealer Rules**: The dealer will continue to draw cards until the hand value is 17 or higher.

## Classes
- **Card**: Represents a single card with a suit and rank.
- **Deck**: Represents a deck of 52 cards and handles shuffling and dealing.
- **Hand**: Represents the hand of a player or dealer, calculates the value, and checks for Blackjack.
- **Game**: Manages the overall flow of the game, including multiple rounds and determining the winner.

## How to Play
1. **Run the Game**: Start the game by running the script.
   ```bash
   python blackjack.py

**Enter the Number of Rounds:** You will be prompted to enter the number of rounds you want to play.
Play the Game: During each round, you will be dealt two cards, and the dealer will also be dealt two cards (one hidden). You can choose to "Hit" to draw another card or "Stand" to end your turn.
**Winning:*** The objective is to get a hand value of 21 or as close to it as possible without exceeding it. The dealer will reveal the hidden card after the player's turn and will draw until reaching a minimum value of 17. The winner is determined based on whose hand is closer to 21 without exceeding it.
## Installation
Clone this repository to your local machine:
bash :git clone https://github.com/Madhumithaashanmugam/python.git

**Navigate to the project directory:**
bash: cd blackjackproject

Ensure you have Python installed on your system.
Usage

**Run the game using Python:**
bash: python blackjackproject.py

**Images:**

![Screenshot 2024-08-19 150915](https://github.com/user-attachments/assets/bdd16b01-c00e-47f9-89ff-be4f5392740f)

![Screenshot 2024-08-19 151050](https://github.com/user-attachments/assets/1544f362-23b4-42c1-999e-9fda84294385)


# Rock-Paper-Scissors Game

## Overview
This is a simple console-based Rock-Paper-Scissors game implemented in Python. The player can choose between rock, paper, or scissors, and the computer randomly selects one of the three options. The game then determines the winner based on the classic rules of Rock-Paper-Scissors.

## Features
- **Player Input**: The player can choose between "rock", "paper", or "scissors".
- **Computer Choice**: The computer randomly selects "rock", "paper", or "scissors".
- **Result Display**: The game compares the player's choice with the computer's choice and displays the result, indicating whether the player won, lost, or if it's a tie.

## Game Rules
- **Rock** smashes **Scissors**.
- **Scissors** cut **Paper**.
- **Paper** covers **Rock**.
- If both the player and the computer choose the same option, it's a tie.

## How to Play
1. **Run the Game**: Start the game by running the script.
   ```bash
   python rock_paper_scissirs.py
Enter Your Choice: When prompted, enter your choice ("rock", "paper", or "scissors").

**View the Result:** The game will display what both you and the computer chose, and it will tell you whether you won, lost, or tied.

**Installation**
**Clone this repository to your local machine:**
bash: git clone https://github.com/Madhumithaashanmugam/python.git

**Navigate to the project directory:**
bash 
cd rock-paper-scissirs

Ensure you have Python installed on your system.

Usage
Run the game using Python:

bash
python rock_paper_scissirs.py

![Screenshot 2024-08-19 152519](https://github.com/user-attachments/assets/7e634385-fea3-43e1-be08-4959bdcbd84b)

# To-Do List Application

## Overview
This is a simple console-based To-Do List application implemented in Python. The application allows users to manage their tasks by adding, removing, and viewing them. It is designed to help users keep track of their tasks in a straightforward and easy-to-use manner.

## Features
- **Add Task**: Users can add a new task to their To-Do List.
- **Remove Task**: Users can remove a specific task from their To-Do List.
- **View Tasks**: Users can view all the tasks in their To-Do List, with each task numbered for easy reference.

## How to Use
1. **Run the Application**: Start the application by running the script.
   ```bash
   python todo_list.py

   
Choose an Option: You will be presented with a menu:
1. Add Task: Enter the task you want to add.
2. Remove Task: Enter the task you want to remove.
3. View Tasks: View all the tasks currently in your To-Do List.
4. Quit: Exit the application.


Manage Your Tasks: Use the options to add, remove, or view tasks as needed.
Installation
**Clone this repository to your local machine:**
bash: git clone https://github.com/your-username/todo-list.git

Navigate to the project directory:
bash: cd todolist

Ensure you have Python installed on your system.

Usage
Run the application using Python:

bash
python todolist.py
![Screenshot 2024-08-19 152834](https://github.com/user-attachments/assets/8cca05e4-34d2-4607-b34b-bb903b2b103c)

