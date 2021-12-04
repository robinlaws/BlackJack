##WINNER BlackJack
import time

def get_player_points(player_list):
    time.sleep(0.5)
    print()
    for player in player_list:
        print("Player " + str(player[0]) + " score: " + str(player[2]))

def get_winner(player_list, dealer_score):
    time.sleep(0.5)
    print("\n-----------------------------------------------------------")
    winner = 0
    if dealer_score == 21:
        print("\nDEALER HAS BLACKJACK.")
        for player in player_list:
            if player[2] == 21:
                print("\nPlayer " + str(player[0]) + " TIE")
                update_balance_tie(player)
            elif player[2] != 21:
                print("\nPlayer " + str(player[0]) + " LOSES.")
                zero_balance(player)
                winner +=1


    elif dealer_score != 21:
        for player in player_list:
            if player[2] == 21:
                if dealer_score== 21:
                    print("\nPlayer " + str(player[0]) + " TIE.")
                    update_balance_tie(player)
                else:
                    print("\nPlayer " + str(player[0]) + " HAS BLACKJACK")
                    update_balance_21(player)

            elif player[2] < 21 and dealer_score < 21:
                if 21 - player[2] < 21 - dealer_score:
                    print("\nPlayer " + str(player[0]) + " WINNER")
                    update_balance_win(player)

                elif player[2] == dealer_score:
                    print("\nPlayer " + str(player[0]) + " TIE.")
                    update_balance_tie(player)

                elif 21 - player[2] > 21 - dealer_score:
                    print("\nPlayer " + str(player[0]) + " LOSES.")
                    print("Balance: " + str(player[1]))
                    zero_balance(player)

            elif player[2] > 21:
                print("\nPlayer " + str(player[0]) + " LOSES.")
                print("Balance: " + str(player[1]))
                zero_balance(player)

            elif player[2] < 21 and dealer_score > 21:
                print("\nPlayer " + str(player[0]) + " WINNER")
                update_balance_win(player)
    print("\n-----------------------------------------------------------")
    

def update_balance_tie(player):
    bet = player[3]
    new_balance = bet + player[1]
    player[1] = new_balance
    print("Balance: " + str(new_balance))


def update_balance_win(player):
    bet = player[3]
    new_balance = (bet*2) + player[1]
    player[1] = new_balance
    print("Balance: " + str(new_balance))

def update_balance_21(player):
    bet=player[3]
    new_balance = (bet*2.5) + player[1]
    player[1] = new_balance
    print("Balance: " + str(new_balance))

def zero_balance(player):
    if player[1] < 5:
        print("GAME 0VER, better luck next time!")

def update_player_list(player_list):
    player_list = [player for player in player_list if player[1]  >= 5]
    print(player_list)
    return player_list

