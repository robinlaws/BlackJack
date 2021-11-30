##calculate bets
def get_player_points(player_list):
    print()
    for player in player_list:
        print("Player " + str(player[0]) + " score: " + str(player[2]))

def get_winner(player_list, dealer_score):
    winner = None
    for player in player_list:
        if player[2] < 21 and dealer_score < 21:
            if player[2] - 21 > dealer_score - 21:
                winner = player[0]
                print("\nPlayer " + str(player[0]) + " wins!")
            elif player[2] == dealer_score:
                winner = "Tie"
                print("It's a TIE.")
            else:
                winner = "Dealer"
                print("\nPlayer " + str(player[0]) + " loses their bet.")
        elif player[2] > 21 and dealer_score < 21:
            winner = "Dealer"
            print("\nPlayer " + str(player[0]) + " loses their bet.")
        else:
            print("\nPlayer " + str(player[0]) + " wins!")
            
                
        
    

        
