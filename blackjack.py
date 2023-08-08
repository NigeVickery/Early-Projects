import random

playerIn = True
dealerIn = True

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', "K", 'A']*4
playerHand = []
dealerHand = []


def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total_value = 0
    face = ['K', 'Q', 'J']
    for card in turn:
        if card.isdigit():
            total_value += int(card)
        elif card in face:
            total_value += 10
        elif card == 'A':
            if total_value > 11:
                total_value += 1
            else:
                total_value += 11
    return total_value

def revealdealerhand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


for _ in range(2):
    dealcard(dealerHand)
    dealcard(playerHand)

while playerIn:
    print(f"Dealer has {revealdealerhand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    stayorhit = input("Enter '1' to stay\nEnter '2' to hit\n")

    if stayorhit == '1':
        playerIn = False
    elif stayorhit == '2':
        dealcard(playerHand)

    if total(playerHand) >= 21:
        break

while dealerIn:
    if total(dealerHand) >= 16:
        dealerIn = False
    else:
        dealcard(dealerHand)

if total(playerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} ")
    print("You bust! Dealer wins!")
elif total(dealerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} "
          f" and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("The dealer busts! You win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)}"
          f" and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer wins!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} "
          f" and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!")
elif total(dealerHand) == total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} "
          f" and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("It's a push!")





