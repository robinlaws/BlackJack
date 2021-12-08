# Blackjack
5 modules. executed from DEALER.


deal, dealer, menu, rounds, winner

VARIABLES:
card_values - dictionary for cards
players = player dictionary for score, hand, bet, balance
deck
dealer_hand

MENU MODULE:
menu – greeting, would you like to see the rules
blackjack_rules – print rules
get_players – returns number of players and returns to player list for player number
get_balance – enter starting balance for players  – returns to player list
get_bet – user enters bet and subtracts from balance – returns to player list
reset_player_hands – will clear player hand for next round

DEAL MODULE:
fill_deck – Fills full deck
shuffle – shuffles full deck
deal__player_cards: First round of 2 cards each
deal_dealer_cards: give dealers cards first face down and second face up
get_player_score
get_dealer_score

ROUNDS MODULE:
round: check for 21, send to play
play : hit or say
dealer_round: hit or stay


WINNER MODULE:
get_final_points: prints players final points
get_winner: compares players to dealer score and prints winners.


DEALER MODULE:
Executes all modules for the game.

GAMEPLAY:

Menu: welcome, print rules yes or no, get number of players, get balance (all players will start with the same balance),Create player dict, Place bets

Deal: Fill deck, shuffle deck, deal cards, assign cards dealt to players and get score

Rounds: Play round for each player, hit or stay. Get final score.

Deal: hit on lower then 17 and get dealer final score

Winner: print player final points, compare points and display winners.
Play again? If yes, go to deal and fill deck

