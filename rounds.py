##Round BlackJack

"""This module contains the first round where the player will hit or stay."""

def round(deck, player_list, players):
    i=0
    for player in player_list:
        if player_list[i][2] == 21:
            print("-------------------------------------------------------------------")
            print("\nPLAYER " + str(i+1) + " HAS BLACKJACK")

        elif player_list[i][2] < 21:
            player_list[i] = play(player_list[i], deck)

        i+=1

def play(player, deck):
    score = int(player[2])
    print("-------------------------------------------------------------------")
    print("\nPlayer " + str(player[0]) + ": You have " + str(score))
    stop = 0
    while stop == 0:
        deal = input("\nPress Y to hit. Press N to stay: ")
        if deal.lower() == "y":
            card = deck[0]
            print(str(card[0]) + " of " + str(card[1]))
            deck.remove(card)
            points = int(round_card_values(card[0],player))
            score+=points
            player[2] = score
            print("Total score: " + str(score))

            if score > 21:
                print("BUST. You lose your bet.")
                stop+=1
            if score == 21:
                print("BLACKJACK")
                stop +=1
        else:
            print("Stay at " + str(score))
            stop +=1

    return player
            
def round_card_values(card, player):
    if card == "Ace":
        if player[2] > 12:
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


            
