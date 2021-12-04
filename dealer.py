import time

def dealer_hand(dealer_score, deck, dealer_cards):
    print("\n--------------------------------------------------------------------")
    print("\nDealers cards: " + dealer_cards[0][0] + " of " + dealer_cards[0][1] + " and " + dealer_cards[1][0] + " of " + dealer_cards[1][1])
    time.sleep(0.5)
    if dealer_score >= 17:
        print("\nDealer will STAY at " + str(dealer_score))
    while dealer_score < 17:
        card = deck[0]
        dealer_cards.append(card)
        print("\nDealer will HIT")
        print("\nDealers card: " + card[0] + " of " + card[1])
        dealer_score = card_values(dealer_cards)
        deck.remove(card)
        if dealer_score > 21:
            print("The dealer has BUSTED.")
        time.sleep(0.5)
    print("\n-----------------------------------------------------------")
    print("\nDealer score is: " + str(dealer_score))
    return dealer_score

        
def card_values(hand):
    total = 0
    aces_count = 0
    for card in hand:
        if card[0] == "Ace":
            total+=11
            aces_count += 1
            while total > 21 and aces_count > 0:
                total -= 10
                aces_count -= 1
        elif card[0] == "Two":
            total+=2
        elif card[0] == "Three":
            total+=3
        elif card[0] == "Four":
            total+=4
        elif card[0] == "Five":
            total+=5
        elif card[0] == "Six":
            total+=6
        elif card[0] == "Seven":
            total+=7
        elif card[0] == "Eight":
            total+=8
        elif card[0] == "Nine":
            total+=9
        elif card[0] == "Ten" or card[0] == "Jack" or card[0] == "Queen" or card[0] == "King" :
            total+=10
    return total
