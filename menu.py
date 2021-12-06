# Module containts the menu and rules for blackjack. Receives number of
# players and starting balance for all players.
import sys

def menu():
    print()
    print("----------------------- Welcome to BlackJack -----------------------")
    print( "                              \u2660 \u2661 \u2662 \u2663")
    while True:
        rules = input("\nWould you like to see the rules before you play? (y/n): ")
        if rules.lower() == "y":
            blackjack_rules()
            break
        elif rules.lower() == "n":
            print("\n                           GOOD LUCK!")
            break
        else:
            print("Please choose yes or no.")
    
def blackjack_rules():
    print("\nBLACKJACK RULES")
    print("Each participant attempts to beat the dealer by getting a count as close to 21 \nas possible, without going over 21.")
    print("Ace can be worth 1 or 11, depending on your score. \nJack, Queen, and King are worth 10. All other cards are their number value.")
    print("\nPlace your bet. (Minimum bet is $5. Maximum bet is $1000).")
    print("\n\tIf the dealer has 21, all bets go to dealer.\n\tIf player has 21, they recieve double their bet.")
    print("\tIf both have 21, it is a tie and player keeps their bet.")
    print("\tIf none of this occurs, player may move into the next round. \n\nPlayer can hit for another card, or stay to keep current hand:")
    print("\tIf you go over 21, you bust and you lose your bet.\n\nOnce the round is complete, the dealer will flip their cards:")
    print("\tIf player is closer to 21 than the dealer, then player WINS their bet.")
    print("\tIf the dealer is closer to 21 then player LOSES their bet.")
    print("\tIf the player balance is less than 5, player is out of the game.")
    print("\n\n\t\t\tGOOD LUCK\n\n")

def get_players():
    while True:
        try:
            num_players = int(input("\n\nPlease enter the number of players (1-5): "))
            if num_players > 5 or num_players <= 0:
                print("Please enter a number between 1 and 5.")
                continue
            else:
                player_list = []
                for i in range(0,num_players):
                    player_list.append({
                        "balance": None,
                        "bet": None,
                        "hand": [],
                        "lose": None
                    })
                return player_list
        except ValueError:
            print("Not a valid number.")

def get_balance(player_list):
    while True:
        try:
            balance = int(input("\nPlease enter starting balance for players (5-1000): "))
            if balance > 1000 or balance < 5:
                print("Please enter a number between 5 and 1000.")
                continue
            else:
                for player in player_list:
                    player["balance"] = balance
                return
        except ValueError:
            print("Not a valid number.")

def get_bet(players):
    print("\n----------------------PLACE YOUR BETS-------------------------------")
    print("---------------------MINIMUM: 5 MAX: 1000---------------------------")
    for index,player in enumerate(players):
        while True:
            try:
                if player["lose"] == True:
                    break
                bet = int(input("\nPLAYER " + str(index+1) + " Place your bet: "))
                if bet > player["balance"]:
                    print("You do not have enough to make this bet. Your current balance is: " + str(player["balance"]))
                elif bet < 5 or bet > 1000:
                    print("Bet value must be between 5 and 1000.")
                else:
                    player["bet"] = bet
                    break
            except ValueError:
                print("Not a valid number.")
    return

def reset_player_hands(players):
    for player in players:
        player["hand"] = []
