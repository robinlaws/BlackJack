## MAIN
import menu
import deal
import rounds
import dealer
import winner


def main():
    menu.menu()
    players = menu.get_players()
    balance = menu.get_balance()
    player_list = menu.get_player_list(players, balance)
    menu.place_bets(player_list)


    print(player_list)
    deck = []
    deal.fill_deck(deck)
    deal.shuffle(deck)
    cards_dealt = deal.deal_cards(deck, players)
    deal.assign_cards(cards_dealt,players,player_list)

    ##Go into round
    rounds.round(deck,player_list, players)
    dealer_score = deal.dealer_cards(cards_dealt, players, player_list)
    dealer_score_2 = dealer.dealer_hand(dealer_score, deck)

    winner.get_player_points(player_list)
    winner.get_winner(player_list, dealer_score_2)
    


    
    


if __name__ == "__main__":
    main()
            

