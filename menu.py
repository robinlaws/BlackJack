##Blackjack Menu
"""This module containts the menu and rules for blackjack. It will also get
number of placers and starting balance for all players. These will be stored
in a list for each player : [player#, balance, score]."""

def menu():
    print("Welcome to BlackJack")
    rules = input("\nWould you like to see the rules before you play? (y/n): ")
    if rules.lower() == "y":
        blackjack_rules()
    if rules.lower() == "n":
        print("Good Luck!")


    
def blackjack_rules():
    print("\nBLACKJACK RULES")
    print("Each participant attempts to beat the dealer by getting a count as close to 21 \nas possible, without going over 21.")
    print("It is up to the player if ace is worth 1 or 11. \nJack Queen King are worth 10. All other cards are number value.")
    print("\nPlace your bet. (Minimum bet is 5$. Maximum bet is 1000$).")
    print("\n\tIf the dealer has 21, all bets go to dealer.\n\tIf player has 21, you recieve 1.5 times your bet.")
    print("\tIf both have 21, it is a tie and you keep your bet.")
    print("\tIf none of this occurs, you may move into the round. \n\nPlayer can hit for another card, or stay to keep current hand:")
    print("\tIf you go over 21, you bust and you lose your bet.\n\nOnce the round is complete, the dealer will flip their cards:")
    print("\tIf you are closer to 21 then the dealer then you WIN your bet.")
    print("\tIf the dealer is closer to 21 then you LOSE your bet.")
    print("\n\n\t\t\tGOOD LUCK\n\n")

def get_players():
    players = int(input("\nPlease enter the number of players (1-5): "))
    return players

def get_balance():
    balance = int(input("\nPlease enter starting balance for players (0-1000): "))
    return balance

def get_player_list(players, balance):
    player_list = []
    for i in range(0,players):
        player_list.append([i+1,balance,0])
    return player_list
    

def place_bets(player_list):
    for i in range (0, len(player_list)):
        bet = int(input("\nPlayer " + str(i+1) + ": Place your bet.(MIN 5 MAX 1000): "))
        new_balance = player_list[i][1] - bet
        player_list[i][1] = new_balance
        print(player_list)
    
        
        
    


