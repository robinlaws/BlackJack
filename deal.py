## Blackjack card deck
import random
import rounds
import menu

number_list = ["Ace", "Two", "Three", "Four", "Five", "Six",
    "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
##suit_list =['\u2660', '\u2661', '\u2662', '\u2663']

def fill_deck(deck):
    for number in number_list:
        for suit in suit_list:
            deck.append([number, suit])

def shuffle(deck):
    random.shuffle(deck)

def deal_cards(deck, player_list):
    cards_dealt = []

##First cards dealt:
    deal = input("\n----------------PRESS ENTER TO DEAL FIRST CARD----------------------")
    for player in player_list:
        card = deck[0]
        print("\nPlayer " + str(player[0]) + ": " + str(card[0]) + " of " + str(card[1]))
        cards_dealt.append(card)
        deck.remove(card)

    dealer_card = deck[0]
    print("\nDealers card:  ?????????")
    cards_dealt.append(dealer_card)
    deck.remove(dealer_card)


##Second cards dealt:
    deal = input("\n----------------PRESS ENTER TO DEAL SECOND CARD---------------------")
    for player in player_list:
        card = deck[0]
        print("\nPlayer " + str(player[0]) + ": " + str(card[0]) + " of " + str(card[1]))
        cards_dealt.append(card)
        deck.remove(card)

    dealer_card = deck[0]

    print("\nDealers card: " + str(dealer_card[0]) + " of " + str(dealer_card[1]))
    
    cards_dealt.append(dealer_card)
    deck.remove(dealer_card)


    return cards_dealt

def assign_cards(cards_dealt, player_list):
    print("\n---------------------------SCORES------------------------------------\n")
    i = 0
    players = len(player_list)
    for player in player_list:
        player_hand = [cards_dealt[i], cards_dealt[players+1]]
        players+=1
        score = card_values(player_hand, player[2])
        player_list[i][2] = score
        
        print("Player " + str(player[0]) + " Score: " + str(score))
        i+=1

def dealer_cards(cards_dealt, player_list):
    dealer_score = 0
    dealer_hand = [cards_dealt[len(player_list)],cards_dealt[len(player_list)*2+1]]
    print("\n-------------------------------------------------------------------------")
    print("\nDealers cards: " + dealer_hand[0][0] + " of " + dealer_hand[0][1] + " and " + dealer_hand[1][0] + " of " + dealer_hand[1][1])
    dealer_score = card_values(dealer_hand, dealer_score)
    return dealer_score


def card_values(player_hand, points):
    total = 0
    i = 0

    for i in range(0,2):
        if player_hand[i][0] == "Ace":
            if points > 12:
                score = 1
                total+=score
            else:
                score = 11
                total+=score
        elif player_hand[i][0] == "Two":
            score = 2
            total+=score
        elif player_hand[i][0] == "Three":
            score = 3
            total+=score
        elif player_hand[i][0] == "Four":
            score = 4
            total+=score
        elif player_hand[i][0] == "Five":
            score = 5
            total+=score
        elif player_hand[i][0] == "Six":
            score = 6
            total+=score
        elif player_hand[i][0] == "Seven":
            score = 7
            total+=score
        elif player_hand[i][0] == "Eight":
            score = 8
            total+=score
        elif player_hand[i][0] == "Nine":
            score = 9
            total+=score
        elif player_hand[i][0] == "Ten" or player_hand[i][0] == "Jack" or player_hand[i][0] == "Queen" or player_hand[i][0] == "King" :
            score = 10
            total+=score
    i+=1
    return total



    

