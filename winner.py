##calculate bets
def get_player_points(player_list):
    print()
    for player in player_list:
        print("Player " + str(player[0]) + " score: " + str(player[2]))

def get_winner(player_list, dealer_score,players):
    winner = 0
    if dealer_score == 21:
        print("\nDEALER HAS BLACKJACK.")
        for player in player_list:
            if player[2] == 21:
                print("\nPlayer " + str(player[0]) + " TIE GAME")
                update_balance_tie(player)
            elif player[2] != 21:
                winner +=1
        if winner == players:
            print("All players lose their bets.")
            for player in player_list:
                print("Player " + str(player[0]) + " balance remains at " + str(player[1]))

    elif dealer_score != 21:
        for player in player_list:
            if player[2] == 21:
                if dealer_score== 21:
                    print("\nPlayer " + str(player[0]) + "TIED.")
                    update_balance_tie(player)
                else:
                    print("\nPlayer " + str(player[0]) + " WINNER")
                    update_balance_win(player)

            elif player[2] < 21 and dealer_score < 21:
                if 21 - player[2] < 21 - dealer_score:
                    winner = player[0]
                    print("\nPlayer " + str(player[0]) + " WINNER")
                    update_balance_win(player)

                elif player[2] == dealer_score:
                    winner = "Tie"
                    print("\nPlayer " + str(player[0]) + " has TIED.")
                    update_balance_tie(player)

                elif 21 - player[2] > 21 - dealer_score:
                    winner = player[0]
                    print("\nPlayer " + str(player[0]) + " loses their bet.")
                    print("Your balance remains at " + str(player[1]))

            elif player[2] > 21:
                winner = "Dealer"
                print("\nPlayer " + str(player[0]) + " loses their bet.")
                print("Your balance remains at " + str(player[1]))

            elif player[2] < 21 and dealer_score > 21:
                print("\nPlayer " + str(player[0]) + " WINNER")
                update_balance_win(player)

def update_balance_tie(player):
    bet = player[3]
    new_balance = bet + player[1]
    player[1] = new_balance
    print("Your balance is now " + str(new_balance))

def update_balance_win(player):
    bet = player[3]
    new_balance = (bet*2) + player[1]
    player[1] = new_balance
    print("Your balance is now " + str(new_balance))
            
            
                
        
    

        
