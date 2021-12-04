##ROUNDS BlackJack
import time
import deal
"""This module contains the first round where the player will hit or stay."""

def round(deck, player_list, player_cards):
    i=0
    players = len(player_list)
    print("\n--------------------------------------------------------------------")
    print("\n\t\t\t   LETS PLAY!")
    for player in player_list:
        if player[2] == 21:
            print("\n--------------------------------------------------------------------")
            print("\nPLAYER " + str(player[0]) + " HAS BLACKJACK")

        elif player[2] < 21:
            print("\n--------------------------------------------------------------------")
            player_hand = [player_cards[i], player_cards[players]]
            score = play(player, deck, player_hand)
            player[2] = score
        i+=1
        players+=1
    return player_list

def play(player, deck, player_hand):
    score = int(player[2])
    time.sleep(0.5)
    print("\nPlayer " + str(player[0]) + ": You have " + str(score))
    stop = 0
    while stop == 0:
        deal = input("\n(H)IT OR (S)TAY: ")
        time.sleep(0.5)
        if deal.lower() == "hit" or deal.lower() == "h":
            card = deck[0]
            print(str(card[0]) + " of " + str(card[1]))
            deck.remove(card)
            player_hand.append(card)
            score = card_values(player_hand)
            player[2] = score
            print("Total score: " + str(score))

            if score > 21:
                print("BUST. You lose your bet.")
                stop+=1
            if score == 21:
                print("BLACKJACK")
                stop +=1

        elif deal.lower()=="stay" or deal.lower() == "s":
            print("Stay at " + str(score))
            stop +=1

        else:
            print("Please enter a valid command.")
    return player[2]


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


