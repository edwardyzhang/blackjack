from random import choice
import sys
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
color = ['Spade', 'Heart', 'Clover', 'Diamond']

cards = []
for num in number:
    for col in color:
        cards.append(str(num) + col)

card1 = choice(cards)
card2 = choice(cards)

card3 = choice(cards)
card4 = choice(cards)


print(f"Dealer card is {card2}")
print(f"Your cards are {card3} and {card4}")

deal = int(card1[0]) + int(card2[0])
play = int(card3[0]) + int(card4[0])

move = input(f"H or hit or S for stand\n")

while move == "H":
    newcard = choice(cards)
    print(f'You got {newcard}\n')
    play += int(newcard[0])
    print(f'Your total is {play}')
    if play > 21:
        print("You lost")
        sys.exit()
    else:
        move = input(f"H or hit or S for stand\n")


print(f'Dealer face down card was {card1}')

while deal < 17 and deal < 21:
    newcard = choice(cards)
    print(f'Dealer got {newcard}')
    deal += int(newcard[0])
    print(f"Dealer has {deal} \n")

if deal > 21:
    print("You won")
elif deal > play:
    print("You lost")
