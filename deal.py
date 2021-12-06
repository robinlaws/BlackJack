# Module fills and shuffles the deck, and deals cards to each player and the dealer. 
# Module calculates and displays player and dealer scores.
import random
import menu
import time
import dealer

number_list = ["Ace", "Two", "Three", "Four", "Five", "Six",
               "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]

def fill_deck(deck):
    for number in number_list:
        for suit in suit_list:
            deck.append([number, suit])

def shuffle(deck):
    random.shuffle(deck)

def deal_cards(deck, players, dealer_hand):
    # First cards dealt:
    print("\n----------------PRESS ENTER TO DEAL FIRST CARDS---------------------")
    for index,player in enumerate(players):
        if player["lose"] != True:
            card = deck.pop()
            print("\nPlayer " + str(index+1) + ": " + str(card[0]) + " of " + str(card[1]))
            time.sleep(0.5)
            player["hand"].append(card)
        
    dealer_hand.append(deck.pop())
    print("\nDealers card:  ?????????")

    # Second cards dealt:
    time.sleep(0.5)
    print("\n----------------PRESS ENTER TO DEAL SECOND CARDS--------------------")
    for index, player in enumerate(players):
        if player["lose"] != True:
            card = deck.pop()
            print("\nPlayer " + str(index+1) + ": " + str(card[0]) + " of " + str(card[1]))
            time.sleep(0.5)
            player["hand"].append(card)

    dealer_card = deck.pop()

    print("\nDealers card: " + str(dealer_card[0]) + " of " + str(dealer_card[1]))
    
    dealer_hand.append(dealer_card)

def get_player_scores(players):
    time.sleep(0.5)
    print("\n------------------------------SCORES--------------------------------\n")
    for index, player in enumerate(players):
        if player["lose"] != True:
            score = dealer.card_total(player["hand"])
            print("Player " + str(index+1) + " Score: " + str(score))

def get_dealer_score(dealer_hand):
    print("\n--------------------------------------------------------------------")
    print("\nDealers cards: " + dealer_hand[0][0] + " of " + dealer_hand[0][1] + " and " + dealer_hand[1][0] + " of " + dealer_hand[1][1])
    dealer_score = dealer.card_total(dealer_hand)
    print("\nDealers score: " + str(dealer_score))
