# Dealer module contains main function for executing program.
import menu
import deal
import rounds
import winner
import time

card_values = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
         "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

def card_total(hand):
total = 0
    aces_count = 0
    for card in hand:
        total += card_values[card[0]]
        if card[0] == "Ace":
            aces_count += 1
    if total < 12 and aces_count > 0:
        total += 10    
    return total

def next_round():
    while True:
        choice = input("\nMove to the next round? (y/n): ")
        if choice.lower() == "n":
            return False
        elif choice.lower() =="y":
            return True
        else:
            print("Please choose yes or no.")

def new_game():
    while True:
        new_game = input("\nWould you like to start a new game? (y/n) ")
        if new_game.lower() == "y":
            return True
        elif new_game.lower() == "n":
            return False
        else:
            print("Please choose yes or no.")

def main():
    # Print rules, get players, get balance, get bet.
    menu.menu()
    while True:
        players = menu.get_players()
        menu.get_balance(players)

        while True:
            menu.reset_player_hands(players)
            menu.get_bet(players)

    # Fill deck, shuffle deck, deal cards and get player scores.
            deck = []
            dealer_hand = []
            deal.fill_deck(deck)
            deal.shuffle(deck)
            deal.deal_cards(deck, players, dealer_hand)
            deal.get_player_scores(players)       

    # Go into round for player (hit or stay) then proceed to dealer round.
            rounds.round(deck, players)
            deal.get_dealer_score(dealer_hand)
            rounds.dealer_round(dealer_hand, deck)

    # Compare scores and get winners.
            winner.get_final_points(players, dealer_hand)
            winner.get_winner(players, dealer_hand)

    # Options for progressing with game.         
            time.sleep(0.5)
            if next_round() == True:
                  continue
            else:
                  break
      if new_game()== True:
          continue
      else: 
          print("\nThanks for playing BlackJack!")
          print("We do not encourage gambling. \n***PLEASE PLAY RESPONSIBLY***")
          sys.exit()

if __name__ == "__main__":
    main()
            
