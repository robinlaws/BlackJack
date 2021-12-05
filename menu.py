# Blackjack Menu

import sys
"""This module containts the menu and rules for blackjack. It will also get
number of placers and starting balance for all players. These will be stored
in a list for each player : [player#, balance, score, bet]."""

def menu():
    print()
    print("----------------------- Welcome to BlackJack -----------------------")
    print( "                             \u2660 \u2661 \u2662 \u2663")
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
    print("\n\t\t\tBLACKJACK RULES")
    print("\nEach participant attempts to beat the dealer by getting a count as close to 21 \nas possible, without going over 21.")
    print("Ace can be worth 1 or 11, depending on your score. \nJack Queen King are worth 10. All other cards are number value.")
    print("\nPlace your bet. (Minimum bet is 5$. Maximum bet is 1000$).")
    print("\n\tIf the dealer has 21, all bets go to dealer.\n\tIf player has 21, you recieve 1.5 times your bet.")
    print("\tIf both have 21, it is a tie and you keep your bet.")
    print("\tIf none of this occurs, you may move into the round. \n\nPlayer can hit for another card, or stay to keep current hand:")
    print("\tIf you go over 21, you bust and you lose your bet.\n\nOnce the round is complete, the dealer will flip their cards:")
    print("\tIf you are closer to 21 then the dealer then you WIN your bet.")
    print("\tIf the dealer is closer to 21 then you LOSE your bet.")
    print("\n\n\t\t\t   GOOD LUCK")
    print("\n--------------------------------------------------------------------")

    
def get_players():
    while True:
        try:
            players = int(input("\nPlease enter the number of players (1-5): "))
            if players > 5 or players <= 0:
                print("Please enter a number between 1 and 5.")
                continue
            else:
                return players
                break
        except ValueError:
            print("Not a valid number.")

            
def get_balance():
    while True:
        try:
            balance = int(input("\nPlease enter starting balance for players (5-1000): "))
            if balance > 1000 or balance < 5:
                print("Please enter a number between 5 and 1000.")
                continue
            else:
                return balance
                break
        except ValueError:
            print("Not a valid number.")

            
def get_player_list(players, balance):
    player_list = []
    for i in range(0,players):
        player_list.append([i+1,balance,0])
    return player_list


def check_balance(player):
    i = 0
    while i == 0:
        try:
            bet = int(input("\nPLAYER " + str(player[0]) + " Place your bet: "))
            if bet > player[1]:
                print("You do not have enough to make this bet. Your current balance is: " + str(player[1]))
            elif bet < 5 or bet > 1000:
                print("Bet value must be between 5 and 1000.")
            else:
                return bet
                i += 1
        except ValueError:
            print("Not a valid number.")

            
def place_bets(player_list):
    print("\n----------------------PLACE YOUR BETS-------------------------------")
    print("                   MINIMUM: 5 MAX: 1000")
    for player in player_list:
        bet = check_balance(player)
        new_balance = player[1] - bet
        player[1] = new_balance
        player.append(bet)

        
def clear_bets(player_list):
    for player in player_list:
        player.pop(3)
        

    
