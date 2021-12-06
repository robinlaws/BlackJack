import random


import time

number_list = ["Ace", "Two", "Three", "Four", "Five", "Six",
                "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]

def fill_deck(deck):
    for number in number_list:
        for suit in suit_list:
            deck.append([number, suit])

def shuffle(deck):
    random.shuffle(deck)


def deal_player_cards(deck, player_list,player_cards):
    for player in player_list:
        card = deck[0]
        print("\nPlayer " + str(player[0]) + ": " + str(card[0]) + " of " + str(card[1]))
        time.sleep(0.5)
        player_cards.append(card)
        deck.remove(card)


def deal_dealer_cards(deck, flag, dealer_cards):
    card = deck[0]
    dealer_cards.append(card)
    deck.remove(card)
    if flag == 1:
        print("\nDealers card:  ?????????")
    elif flag == 2:
        print("\nDealers card: " + str(card[0]) + " of " + str(card[1]))

def assign_cards(player_cards, dealer_cards, player_list):
    print("\n------------------------------SCORES--------------------------------\n")
    i=0
    players = len(player_list)
    for player in player_list:
        player_hand = [player_cards[i], player_cards[players]]
        score = card_values(player_hand)
        player[2] = score
        print("Player " + str(player[0]) + " Score: " + str(score))
        i+=1
        players+=1

    dealer_score = card_values(dealer_cards)
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


    
