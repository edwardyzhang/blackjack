from deck import deck
import sys


class Session:
    def __init__(self):
        self.deck = deck()
        self.player_total = 0
        self.comp_total = 0
        self.player_cards = []
        self.comp_cards = []

    def start(self):
        card1 = self.deck.get_card()
        card2 = self.deck.get_card()
        self.comp_cards.append(card1)
        self.comp_cards.append(card2)
        print(f"Dealer's up card is {card1}")
        self.comp_total = card1+card2
        card3 = self.deck.get_card()
        card4 = self.deck.get_card()
        self.player_cards.append(card3)
        self.player_cards.append(card4)
        self.player_total = card3+card4
        print(f"Your cards are {card3} and {card4}")

    def hit(self, turn):
        newcard = self.deck.get_card()
        if turn == "player":
            print(f"You got {newcard}")
            self.player_total += newcard.value
            print(f"Your total is {self.player_total}")
        else:
            print(f"Dealer got {newcard}")
            self.comp_total += newcard.value
            print(f"Dealer total is {self.comp_total}")


if __name__ == '__main__':
    game = Session()
    game.start()

    play = input("Do you want to hit (h) or stand (s)\n")

    while play == 'h':
        game.hit("player")
        play = input("Do you want to hit (h) or stand (s)\n")
        if game.player_total > 21:
            print("You lost")
            sys.exit()

    print(f"Dealer's face down card was {game.comp_cards[1]}")
    while game.comp_total < 17 and game.comp_total <= 21:
        game.hit("comp")

    if game.comp_total > 21:
        print("You won")
        sys.exit()

    if game.comp_total > game.player_total:
        print("You lost")
    elif game.player_total > game.comp_total:
        print("You won")
    else:
        print("You draw")
