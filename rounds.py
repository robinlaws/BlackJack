# Module contains round where player & dealer hit or stay.
import time
import dealer
import deal

def round(deck, players):
    print("\n---------------------------------------------------------------------")
    print("\n                   $$$$     LETS PLAY!     $$$$")
    for index, player in enumerate(players):
        if dealer.card_total(player["hand"]) == 21:
            print("---------------------------------------------------------------------")
            print("\nPLAYER " + str(index+1) + " HAS BLACKJACK")


        elif dealer.card_total(player["hand"]) < 21:
            if player["lose"] != True:  
                time.sleep(0.5)
                score = dealer.card_total(player["hand"])
                print("\n--------------------------------------------------------------------")
                print("\nPlayer " + str(index+1) + ": You have " + str(score))
                play(player, deck)

def play(player, deck):
    while True:
        if player["lose"] != True:
            deal = input("\n(H)IT OR (S)TAY: ")
            if deal.lower() == "hit" or deal.lower() == "h":
                card = deck.pop()
                print(str(card[0]) + " of " + str(card[1]))
                player["hand"].append(card)
                score = dealer.card_total(player["hand"])
                print("Total score: " + str(score))
                if score > 21:
                    print("BUST. You lose your bet.")
                    break
                if score == 21:
                    print("BLACKJACK")
                    break
            elif deal.lower()=="stay" or deal.lower() == "s":
                score = dealer.card_total(player["hand"])
                print("Stay at " + str(score))
                break
            else:
                print("Please enter a valid command.")

def dealer_round(dealer_hand, deck):
    time.sleep(0.5)
    score = dealer.card_total(dealer_hand)
    if score == 21:
        time.sleep(0.5)
        print("The dealer has BLACKJACK.")
    if score >= 17 and score != 21:
        time.sleep(0.5)
        print("\nDealer will STAY at " + str(score))
    while score < 17:
        card = deck.pop()
        dealer_hand.append(card)
        score = dealer.card_total(dealer_hand)
        time.sleep(0.5)
        print("\nDealer will HIT")
        time.sleep(0.5)
        print("\n--------------------------------------------------------------------")
        print("\nDealers card: " + card[0] + " of " + card[1])
        print("Total score: " + str(score))
        if score > 21:
            time.sleep(0.5)
            print("The dealer has BUSTED.")
        time.sleep(0.5)
    return score
        
