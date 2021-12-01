## MAIN BlackJack module
import menu
import deal
import rounds
import dealer
import winner
import sys


def main():
##Print rules, get players, get balance.
    menu.menu()
    players = menu.get_players()
    balance = menu.get_balance()
    player_list = menu.get_player_list(players, balance)

    while True:
        menu.place_bets(player_list)
        
##Fill deck, shuffle deck, deal cards and get card values
        deck = []
        deal.fill_deck(deck)
        deal.shuffle(deck)
        cards_dealt = deal.deal_cards(deck, player_list)
        deal.assign_cards(cards_dealt,player_list)

##Go into round for player (hit or stay) then dealer hand
        rounds.round(deck,player_list)
        dealer_score = deal.dealer_cards(cards_dealt, player_list)
        dealer_score_2 = dealer.dealer_hand(dealer_score, deck)

##Compare scores and get winners
        winner.get_player_points(player_list)
        winner.get_winner(player_list, dealer_score_2,players)


##Update player list for players out of money
        player_list = winner.update_player_list(player_list)
        if len(player_list) == 0:
            print("\n\nALL PLAYERS ARE OUT OF MONEY. Thanks for playing! Please gamble responsibly")
            sys.exit()

        choice = input("\nMove to the next round? (y/n): ")
        menu.clear_bets(player_list)

                
        if choice.lower() == "n":
            break
    print("\nThanks for playing BlackJack! \nPlease gamble responsibly.")
    print("PLEASE GAMBLE RESPONSIBLY")

    

if __name__ == "__main__":
    main()
            

