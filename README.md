
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

wt (table column #) - Move a card from waste to the table column.

tf (table column #) - Move a card from the table column to the foundation.

tt (first table column #) (second table column #) - Move a card from one table column to another.

l - Display valid commands.

q - Quit the game.

## Rules of Solitaire
- Cards can be moved to the foundation piles if they follow the sequence: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.
- Cards in the table columns can be moved if they are in descending order and have alternating colors.
- Only Kings can be placed in an empty column on the table.
- A card from the waste pile can be moved to the table column if it follows the descending order and alternating color rule.
  
## Dependencies
The script uses the random module for shuffling cards.

## Sources
I used online resources for debugging such as StackOverflow and Geeks for Geeks. 
