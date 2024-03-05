
# Solitaire Game
## Introduction
This is a simple implementation of the Solitaire card game in Python. The game includes a deck of cards, a table with seven piles, a stock and waste pile, and foundation piles. The goal of the game is to move all the cards to the foundation piles following specific rules.

## Components
1. PlayingCard Class
   
Represents an individual playing card with attributes such as name, suit, title, and value. Provides methods for checking if a card is below another card and if they have opposite suits.

2. Deck Class
   
Represents a deck of playing cards. Allows shuffling and dealing cards.

3. Table Class
   
Keeps track of the seven piles of cards on the table. Allows flipping cards, moving cards between columns, and moving cards to the foundation.

4. StockWaste Class
   
Manages the stock and waste piles. Allows moving cards from the stock to waste and retrieving information about the piles.

5. Foundation Class
   
Represents the foundation piles. Cards can be added if they follow specific rules.

## How to Play
Run the script and select a game mode.

Follow the provided commands to interact with the game:

sw - Move a card from stock to waste.

wf - Move a card from waste to foundation.

wt #T - Move a card from waste to the table column.

tf #T - Move a card from the table column to the foundation.

tt #T1 #T2 - Move a card from one table column to another.

h - Display valid commands.

q - Quit the game.

## Dependencies
The script uses the random module for shuffling cards.
