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
    if len(deck)>((players+1)*2):

##First cards dealt:
        deal = input("---Press enter to deal cards----")
        for i in range(0,players):
            card = deck[0]
            print("\nPlayer " + str(i+1) + ": " + str(card[0]) + " of " + str(card[1]))
            cards_dealt.append(card)
            deck.remove(card)
            deal=input()
        dealer_card = deck[0]
        print("\nDealers card face down.\n")
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

    else:
        print("Not enough cards in deck. Reshuffling.")
        fill_deck()
        shuffle(deck)

    return cards_dealt

def assign_cards(cards_dealt, players, player_list):
    i = 0
    for player in player_list:
        player = [cards_dealt[i], cards_dealt[players+1]]
        players+=1
        score = card_values(player)
        player_list[i][2] = score
        print("Player " + str(i+1) + " Score: " + str(score))
        i+=1


def card_values(player):
    total = 0
    i = 0
    n = 0
    print(player)
    for i in range(0,2):
        if player[i][n] == "Ace":
            score = 1
            total+=score
        elif player[i][n] == "Two":
            score = 2
            total+=score
        elif player[i][n] == "Three":
            score = 3
            total+=score
        elif player[i][n] == "Four":
            score = 4
            total+=score
        elif player[i][n] == "Five":
            score = 5
            total+=score
        elif player[i][n] == "Six":
            score = 6
            total+=score
        elif player[i][n] == "Seven":
            score = 7
            total+=score
        elif player[i][n] == "Eight":
            score = 8
            total+=score
        elif player[i][n] == "Nine":
            score = 9
            total+=score
        elif player[i][n] == "Ten" or player[i][n] == "Jack" or player[i][n] == "Queen" or player[i][n] == "King" :
            score = 10
            total+=score
    i+=1
    n+=2
    return total



    

