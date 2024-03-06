import random


class PlayingCard():
    card_to_name = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
                    8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, value, suit):
        self.name = self.card_to_name[value]
        self.suit = suit
        self.title = f"{self.name} {self.suit}"
        self.value = value

    def isRankBelow(self, card):
        return self.value == (card.value - 1)

    def isOppositeSuit(self, card):
        if self.suit == "club" or self.suit == "spde":
            return card.suit == "hrt" or card.suit == "diam"
        else:
            return card.suit == "spde" or card.suit == "club"

    def canAttach(self, card):
        if card.isRankBelow(self) and card.isOppositeSuit(self):
            return True
        else:
            return False

    def __str__(self):
        return self.title

class Deck():
    unshuffled_deck = [PlayingCard(card, suit) for card in range(1, 14) for suit in ["club", "diam", "hrt", "spde"]]

    def __init__(self, num_decks=1):
        self.deck = self.unshuffled_deck * num_decks
        random.shuffle(self.deck)

    def flipCard(self):
        return self.deck.pop()

    def deal(self, num_cards):
        return [self.deck.pop() for _ in range(0, num_cards)]

    def __str__(self):
        return str(self.deck)

class Table():
    # Class that keeps track of the seven piles of cards on the table

    def __init__(self, card_list):
        self.unflipped = {x: card_list[x] for x in range(7)}
        self.flipped = {x: [self.unflipped[x].pop()] for x in range(7)}

    def flipCard(self, col):
        """ Flips a card under column col on the table """
        if len(self.unflipped[col]) > 0:
            self.flipped[col].append(self.unflipped[col].pop())

    def pileLength(self):
        """ Returns the length of the longest pile on the table """
        return max([len(self.flipped[x]) + len(self.unflipped[x]) for x in range(7)])

    def addCards(self, cards, column):
        """ Returns true if cards were successfully added to column on the table.
            Returns false otherwise. """
        column_cards = self.flipped[column]
        if len(column_cards) == 0 and cards[0].value == 13:
            column_cards.extend(cards)
            return True
        elif len(column_cards) > 0 and column_cards[-1].canAttach(cards[0]):
            column_cards.extend(cards)
            return True
        else:
            return False

    def tableToTable(self, c1, c2):
        """ Returns True if any card(s) are successfully moved from c1 to c2 on
            the table, returns False otherwise. """
        c1_cards = self.flipped[c1]

        for index in range(len(c1_cards)):
            if self.addCards(c1_cards[index:], c2):
                self.flipped[c1] = c1_cards[0:index]
                if index == 0:
                    self.flipCard(c1)
                return True
        return False

    def tableToFoundation(self, Foundation, column):
        """ Moves a card from the table to the appropriate Foundation pile """
        column_cards = self.flipped[column]
        if len(column_cards) == 0:
            return False

        if Foundation.addCard(column_cards[-1]):
            column_cards.pop()
            if len(column_cards) == 0:
                self.flipCard(column)
            return True
        else:
            return False

    def wasteToTable(self, waste_pile, column):
        """ Returns True if a card from the waste pile is successfully moved to a column
            on the table, returns False otherwise. """
        card = waste_pile.waste[-1]
        if self.addCards([card], column):
            waste_pile.popWasteCard()
            return True
        else:
            return False

class StockWaste():
    """A StockWaste object keeps track of the stock and waste piles."""

    def __init__(self, cards):
        self.deck = cards
        self.waste = []

    def stockToWaste(self):
        """Returns True if a card is successfully moved from the stock pile to the
        waste pile, returns False otherwise."""
        if len(self.deck) + len(self.waste) == 0:
            print("There are no more cards in the stock pile!")
            return False

        if len(self.deck) == 0:
            self.waste.reverse()
            self.deck = self.waste.copy()
            self.waste.clear()

        self.waste.append(self.deck.pop())
        return True

    def popWasteCard(self):
        """Removes a card from the waste pile."""
        if len(self.waste) > 0:
            return self.waste.pop()

    def getTopWaste(self):
        """Retrieves the top card of the waste pile."""
        if len(self.waste) > 0:
            return self.waste[-1]
        else:
            return None  # Return None when the waste pile is empty

    def getStockAmount(self):
        """Returns a string of the number of cards in the stock."""
        if len(self.deck) > 0:
            return str(len(self.deck)) + " card(s)"
        else:
            return "empty"


class Foundation():

    def __init__(self):
        self.Foundation_stacks = {"club": [], "hrt": [], "spde": [], "diam": []}

    def addCard(self, card):
        """Returns True if a card is successfully added to the foundation,
        otherwise, returns False."""
        stack = self.Foundation_stacks[card.suit]

        if len(stack) == 0:
            if card.value == 1:
                stack.append(card)
                return True
            else:
                return False
        elif stack[-1].isRankBelow(card):
            stack.append(card)
            return True
        else:
            return False

    def getTopCard(self, suit):
        """ Return the top card of a Foundation pile. If the pile
            is empty, return the letter of the suit."""
        stack = self.Foundation_stacks[suit]
        if len(stack) == 0:
            return suit[0].upper()
        else:
            return self.Foundation_stacks[suit][-1]

    def gameWon(self):
        """ Returns whether the user has won the game. """
        for suit, stack in self.Foundation_stacks.items():
            if len(stack) == 0:
                return False
            card = stack[-1]
            if card.value != 13:
                return False
        return True

def printValidCommands():
    """ Provides the list of commands, for when users press 'l' """
    print("Valid Commands: ")
    print("\tmv - move card from stock to waste")
    print("\twf - move card from waste to foundation")
    print("\twt (table column #) - move card from waste to table")
    print("\ttf (table column #) - move card from table to foundation")
    print("\ttt (first table column #) (second table column #) - move card from one table column to another")
    print("\tl - display the list of commands")
    print("\tq - quit")
    print("\t Note: club = clubs, hrt = hearts, spde = spades, diam = diamonds")
    print("\n")


def printTable(table, Foundation, stock_waste):
    """ Prints the current status of the table """

    print("waste \t stock \t\t\t\t Foundation")
    print("{}\t{}\t\t{}\t{}\t{}\t{}".format(stock_waste.getTopWaste(), stock_waste.getStockAmount(),
                                             Foundation.getTopCard("club"), Foundation.getTopCard("hrt"),
                                             Foundation.getTopCard("spde"), Foundation.getTopCard("diam")))
    print("\n")
    print("\ntable\n\t1\t2\t3\t4\t5\t6\t7\n")
    # Print the cards, first printing the unflipped cards, and then the flipped.
    for x in range(table.pileLength()):
        print_str = ""
        for col in range(7):
            hidden_cards = table.unflipped[col]
            shown_cards = table.flipped[col]
            if len(hidden_cards) > x:
                print_str += "\tx"
            elif len(shown_cards) + len(hidden_cards) > x:
                print_str += "\t" + str(shown_cards[x - len(hidden_cards)])
            else:
                print_str += "\t"
        print(print_str)
    print("\n")


def selectGame():
    print("Select a game mode:")
    print("1. Easy")
    print("2. Other Modes")
    choice = input("Enter the number of the game you'd like to play: ")
    return int(choice)

if __name__ == "__main__":
    selected_game = selectGame()

    if selected_game == 1:
        d = Deck()
        t = Table([d.deal(x) for x in range(1, 8)])
        f = Foundation()
        sw = StockWaste(d.deal(24))

        print("\n")
        print("Welcome to Solitaire!\n")
        printValidCommands()
        printTable(t, f, sw)

        while not f.gameWon():
            command = input("Enter a command (type 'l' for list of commands): ")
            command = command.lower().replace(" ", "")
            if command == "l":
                printValidCommands()
            elif command == "q":
                print("Game exited.")
                break
            elif command == "sw":
                if sw.stockToWaste():
                    printTable(t, f, sw)
            elif command == "wf":
                if f.addCard(sw.getTopWaste()):
                    sw.popWasteCard()
                    printTable(t, f, sw)
                else:
                    print("Error! Card could not be moved from the waste to the foundation.")
            elif "wt" in command and len(command) == 3:
                col = int(command[-1]) - 1
                if t.wasteToTable(sw, col):
                    printTable(t, f, sw)
                else:
                    print("Error! Card could not be moved from the waste to the table column.")
            elif "tf" in command and len(command) == 3:
                col = int(command[-1]) - 1
                if t.tableToFoundation(f, col):
                    printTable(t, f, sw)
                else:
                    print("Error! Card could not be moved from the table column to the foundation.")
            elif "tt" in command and len(command) == 4:
                c1, c2 = int(command[-2]) - 1, int(command[-1]) - 1
                if t.tableToTable(c1, c2):
                    printTable(t, f, sw)
                else:
                    print("Error! Card could not be moved from that table column.")
            else:
                print("Sorry, that is not a valid command.")

        if f.gameWon():
            print("Congratulations! You've won!")
    else:
        print("Selected game not implemented yet.")
