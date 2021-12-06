# Module contains logic for determining the winners by comparing player and dealer scores.
# Module updates balance based on bet and results from score comparison.
import time
import dealer
import sys

def get_final_points(players, dealer_hand):
    time.sleep(0.5)
    print("\n---------------------------FINAL SCORES-----------------------------\n")
    for index, player in enumerate(players):
        if player["lose"] != True:
            score = dealer.card_total(player["hand"])
            print("Player " + str(index+1) + " score: " + str(score))
    dealer_score = dealer.card_total(dealer_hand)
    print("Dealer score: " + str(dealer_score))

def get_winner(players, dealer_hand):
    out_count = 0
    dealer_score = dealer.card_total(dealer_hand)
    time.sleep(1)
    input("\n-------------------PRESS ENTER TO VIEW RESULTS----------------------")

    for index, player in enumerate(players):
        if player["lose"] == True:
            out_count += 1
        else:            
            player_score = dealer.card_total(player["hand"])
            if (dealer_score < player_score) and player_score < 21 or (dealer_score > 21 and player_score < 21):
                time.sleep(0.5)
                print("\nPlayer " + str(index+1) + " WINS.")
                player["balance"] += player["bet"]
                print("Balance:", player["balance"])
            if player_score == 21:
                time.sleep(0.5)
                print("\nPlayer " + str(index+1) + " HAS BLACKJACK.")
                player["balance"] += player["bet"]*2
                print("Balance:", player["balance"])
            if ((dealer_score > player_score) and dealer_score <= 21) or player_score > 21:
                time.sleep(0.5)
                print("\nPlayer " + str(index+1) + " LOSES.")
                player["balance"] -= player["bet"]
                print("Balance:", player["balance"])
                if player["balance"] >=0 and player["balance"] < 5:
                    print("You've run out of money. Better luck next time!")
                    player["lose"] = True
                    out_count += 1
            if player_score == dealer_score and player_score <= 21:
                time.sleep(0.5)
                print("\nPlayer " + str(index+1) + " TIES.")
                print("Balance:", player["balance"])
    if out_count == len(players):
        print("\n--------------------------------------------------------------------")
        print("\n\nALL PLAYERS ARE OUT OF MONEY. Thanks for playing!\n***PLEASE PLAY RESPONSIBLY***")
        sys.exit()
