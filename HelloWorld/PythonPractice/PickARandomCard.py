"""
This program is to pick the random card from a deck of playing cards. To achieve this we will choose from the deck of 52 cards

"""
import random



def pickCard():
    card = ['diamond', 'spade', 'heart', 'club']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    card = random.choices(card)
    rank = random.choices(ranks)

    print(f"{rank} of {card}")


pickCard()
