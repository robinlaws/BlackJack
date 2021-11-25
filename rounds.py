##Round BlackJack
"""This module contains the first round where the player will hit or stay."""

def round(deck, player_list):
    i=0
    for player in player_list:
        if player_list[i][2] == 21:
            print("PLAYER " + str(i+1) + "HAS BLACKJACK")
        elif player_list[i][2] < 21:
            score = player_list[i][2]
            deal = input("\nPlayer " + str(i+1) + ": You have " + str(score) + ". \nPress Y to hit. Press N to stay: ")
            if deal.lower() == "y":
                card = deck[0]
                print(str(card[0]) + " of " + str(card[1]))
                deck.remove(card)
                points = round_card_values(card[0])
                score+=points
                player_list[i][2] = score
                print("Total score: " + str(score))
                if score > 21:
                    print("BUST. You lose your bet.")
                if score == 21:
                    print("BLACKJACK")
            else:
                print("Stay at " + str(score))
            i+=1


def round_card_values(card):
    if card == "Ace":
        return 1
    elif card == "Deuce":
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

def check_scores(scores):
    for score in scores:
        if score > 21:
            scores.remove(score)
            


    
    
