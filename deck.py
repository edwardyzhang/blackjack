from card import Card
import random
from operator import attrgetter
from turtle import color


class deck:
    def __init__(self):
        # initalizes a set of Cards
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", 'Q', 'K']
        color = ['Spade', 'Heart', 'Clover', 'Diamond']

        self.cards = []

        for num in number:
            for col in color:
                self.cards.append(Card(num, col))

    def get_card(self):
        return random.choice(self.cards)

    def __str__(self) -> str:
        return str(self.cards)


l = deck()
print(l)
