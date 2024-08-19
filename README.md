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
bash :git clone https://github.com/your-username/blackjack-game.git

**Navigate to the project directory:**
bash: cd blackjack-game

Ensure you have Python installed on your system.
Usage

**Run the game using Python:**
bash: python blackjack.py

**Images:**

![Screenshot 2024-08-19 151050](https://github.com/user-attachments/assets/1544f362-23b4-42c1-999e-9fda84294385)


![Screenshot 2024-08-19 150915](https://github.com/user-attachments/assets/bdd16b01-c00e-47f9-89ff-be4f5392740f)