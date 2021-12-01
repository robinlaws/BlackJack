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

def deal_cards(deck, players):
    cards_dealt = []

##First cards dealt:
    deal = input("\n----------------PRESS ENTER TO DEAL THE CARDS-----------------------")
    for i in range(0,players):
        card = deck[0]
        print("\nPlayer " + str(i+1) + ": " + str(card[0]) + " of " + str(card[1]))
        cards_dealt.append(card)
        deck.remove(card)
        deal=input()
    dealer_card = deck[0]
    print("\nDealers card face down.\n")
    print(dealer_card)
    cards_dealt.append(dealer_card)
    deck.remove(dealer_card)
    deal = input()

##Second cards dealt:
    for i in range(1,players+1):
        card = deck[0]
        print("\nPlayer " + str(i) + ": " + str(card[0]) + " of " + str(card[1]))
        cards_dealt.append(card)
        deck.remove(card)
        deal = input()
    dealer_card = deck[0]

    print("\nDealers card: " + str(dealer_card[0]) + " of " + str(dealer_card[1]))
    cards_dealt.append(dealer_card)
    deck.remove(dealer_card)
    deal = input()

    return cards_dealt

def assign_cards(cards_dealt, players, player_list):
    i = 0
    for player in player_list:
        player = [cards_dealt[i], cards_dealt[players+1]]
        players+=1
        score = card_values(player, player_list)
        player_list[i][2] = score
        print("Player " + str(i+1) + " Score: " + str(score))
        i+=1

def dealer_cards(cards_dealt, players, player_list):
    dealer_score = 0
    dealer = [cards_dealt[players],cards_dealt[players*2+1]]
    print("------------------------------------------------------------------")
    print("\nDealers cards: " + dealer[0][0] + " of " + dealer[0][1] + " and " + dealer[1][0] + " of " + dealer[1][1])
    dealer_score = card_values(dealer, player_list)
    return dealer_score


def card_values(player, player_list):
    total = 0
    i = 0

    for i in range(0,2):
        if player[i][0] == "Ace":
            if player_list[i][2] > 12:
                score = 1
                total+=score
            else:
                score = 11
                total+=score
        elif player[i][0] == "Two":
            score = 2
            total+=score
        elif player[i][0] == "Three":
            score = 3
            total+=score
        elif player[i][0] == "Four":
            score = 4
            total+=score
        elif player[i][0] == "Five":
            score = 5
            total+=score
        elif player[i][0] == "Six":
            score = 6
            total+=score
        elif player[i][0] == "Seven":
            score = 7
            total+=score
        elif player[i][0] == "Eight":
            score = 8
            total+=score
        elif player[i][0] == "Nine":
            score = 9
            total+=score
        elif player[i][0] == "Ten" or player[i][0] == "Jack" or player[i][0] == "Queen" or player[i][0] == "King" :
            score = 10
            total+=score
    i+=1
    return total



    

