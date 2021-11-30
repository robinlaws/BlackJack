## MAIN BlackJack module
import menu
import deal
import rounds
import dealer
import winner


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
        cards_dealt = deal.deal_cards(deck, players)
        deal.assign_cards(cards_dealt,players,player_list)

    ##Go into round for player (hit or stay) then dealer hand
        rounds.round(deck,player_list, players)
        dealer_score = deal.dealer_cards(cards_dealt, players, player_list)
        dealer_score_2 = dealer.dealer_hand(dealer_score, deck)

    ##Compare scores and get winners
        winner.get_player_points(player_list)
        winner.get_winner(player_list, dealer_score_2,players)

        choice = input("\nWould you like to play again? (y/n): ")
        if choice.lower() == "n":
            break
    print("\nThanks for playing BlackJack!")

    

if __name__ == "__main__":
    main()
            

