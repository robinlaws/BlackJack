## MAIN BlackJack module
# test test test
import menu
import deal
import rounds
import winner
import dealer
import sys
import time


def main():
    
# Print rules, get players, get balance.
    menu.menu()
    while True:
        players = menu.get_players()
        balance = menu.get_balance()
        player_list = menu.get_player_list(players, balance)
        while True:
            menu.place_bets(player_list)

# Fill deck, shuffle deck, deal cards and get scores
            deck = []
            player_cards = []
            dealer_cards = []
            deal.fill_deck(deck)
            deal.shuffle(deck)
            input("\n----------------PRESS ENTER TO DEAL FIRST CARDS--------------------")
            deal.deal_player_cards(deck,player_list,player_cards)
            deal.deal_dealer_cards(deck, 1, dealer_cards)
            input("\n----------------PRESS ENTER TO DEAL SECOND CARDS--------------------")
            deal.deal_player_cards(deck,player_list,player_cards)
            deal.deal_dealer_cards(deck, 2, dealer_cards)
            dealer_score = deal.assign_cards(player_cards, dealer_cards, player_list)

# Go into player and dealer rounds (hit or stay)
            player_list = rounds.round(deck,player_list,player_cards)
            dealer_score_final = dealer.dealer_hand(dealer_score, deck, dealer_cards)

# Compare scores and get winners
            winner.get_player_points(player_list)
            winner.get_winner(player_list, dealer_score_final)

# Update player list for players out of money
            player_list = winner.update_player_list(player_list)
            if len(player_list) == 0:
                print("\n\nALL PLAYERS ARE OUT OF MONEY. Thanks for playing!\n***PLEASE GAMBLE RESPONSIBLY***")
                sys.exit()
            time.sleep(0.5)
            print("\t\t\t" + str(len(player_list)) + " PLAYERS REMAIN")

# Check if players would like to continue
            choice = input("\nMove to the next round? (y/n): ")
            menu.clear_bets(player_list)
            if choice.lower() == "n":
                break
            elif choice.lower() =="y":
                continue
            else:
                print("Please choose yes or no.")

# Check if players would like to start a new game
        new_game = input("\nWould you like to start a new game? (y/n) ")
        if new_game.lower() == "y":
            continue
        if new_game.lower() == "n":
            break
        else:
            print("Please choose yes or no.")

# Exit game if player does not want to continue
    print("\nThanks for playing BlackJack!")
    print("We do not encourage gambling. \n***PLEASE GAMBLE RESPONSIBLY***")

            

if __name__ == "__main__":
    main()
