class Card:
    num = [i for i in range((11))]
    high = ['J', 'Q', 'K']

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.name = f"{number} of {suit}"
        if number in Card.high:
            self.value = 10
        else:
            self.value = int(number)

    # TODO need to make it so that adding two objects will add their value
    def __add__(self, x):
        return self.value + x.value

    def __str__(self) -> str:
        return self.name
