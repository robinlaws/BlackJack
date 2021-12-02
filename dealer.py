import time

def dealer_hand(dealer_score, deck):
    time.sleep(0.5)
    if dealer_score >= 17:
        print("\nDealer will STAY at " + str(dealer_score))
    while dealer_score < 17:
        card = deck[0]
        print("\nDealer will HIT")
        print("Dealers card: " + card[0] + " of " + card[1])
        points = card_values(card[0], dealer_score)
        dealer_score += points
        deck.remove(card)
        if dealer_score > 21:
            print("The dealer has BUSTED.")
        time.sleep(0.5)
    print("-----------------------------------------------------------")
    print("\nDealer score is: " + str(dealer_score))
    return dealer_score

        
def card_values(card, dealer_score):
    if card == "Ace":
        if dealer_score > 12:
            return 1
        else:
            return 11
    elif card == "Two":
        return 2
    elif card == "Three":
        return 3
    elif card == "Four":
        return 4
    elif card == "Five":
        return 5
    elif card == "Six":
        return 6
    elif card == "Seven":
        return 7
    elif card == "Eight":
        return 8
    elif card == "Nine":
        return 9
    elif card == "Ten" or card == "Jack" or card == "Queen" or card == "King" :
        return 10
                                
        
