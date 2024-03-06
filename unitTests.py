import unittest
from unittest.mock import patch
from io import StringIO
from solitaire import PlayingCard, Deck, Table, StockWaste, Foundation, printValidCommands, printTable, selectGame

class TestSolitaireGame(unittest.TestCase):

    def test_playing_card_creation(self):
        card = PlayingCard(10, "spde")
        self.assertEqual(card.name, "10")
        self.assertEqual(card.suit, "spde")
        self.assertEqual(card.title, "10 spde")
        self.assertEqual(card.value, 10)
        print("playing_card_creation test passed")

    def test_deck_creation(self):
        deck = Deck(num_decks=2)
        self.assertEqual(len(deck.deck), 2 * 52)  # 52 cards per deck
        self.assertIsInstance(deck.flipCard(), PlayingCard)
        self.assertEqual(len(deck.deal(5)), 5)
        print("deck_creation test passed")

    def test_table_creation(self):
        card_list = [[PlayingCard(value, "club") for value in range(1, x + 1)] for x in range(1, 8)]
        table = Table(card_list)
        self.assertEqual(table.pileLength(), max([len(table.flipped[x]) + len(table.unflipped[x]) for x in range(7)]))

        print("table_creation test passed")

    def test_stockwaste_operations(self):
    # Adjust the range to only include valid card values (1 to 13)
        cards = [PlayingCard(value % 13 + 1, "club") for value in range(1, 25)]
        stock_waste = StockWaste(cards)

        self.assertTrue(stock_waste.stockToWaste())
        self.assertTrue(stock_waste.popWasteCard())

        self.assertIsInstance(stock_waste.getStockAmount(), str)

        print("stockwaste_operations test passed")



    def test_foundation_operations(self):
        foundation_stack = Foundation()
        card1 = PlayingCard(1, "club")
        card2 = PlayingCard(2, "hrt")

        self.assertTrue(foundation_stack.addCard(card1))
        self.assertFalse(foundation_stack.addCard(card2))
        self.assertFalse(foundation_stack.addCard(card2))  # Adding duplicate card2 should fail
        self.assertIsInstance(foundation_stack.getTopCard("club"), (PlayingCard, str))
        print("foundation_operations test passed")

if __name__ == '__main__':
    unittest.main()
