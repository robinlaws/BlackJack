## MAIN
import menu
import deal
import rounds

def assign_cards(cards_dealt, players, player_list):
    i = 0
    for player in player_list:
        player = [cards_dealt[0], cards_dealt[players+1]]
        score = card_values(player)
        player_list[i][2] = score
        print("Player " + str(i+1) + " Score: " + str(score))
        i+=1

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
    print(player_list)

    rounds.round(deck,player_list)
    print("\nROUND 2")
    rounds.round(deck,player_list)






if __name__ == "__main__":
    main()
            

