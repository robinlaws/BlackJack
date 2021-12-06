# Blackjack
5 modules. executed from DEALER.


deal, dealer, menu, rounds, winner

VARIABLES:
•	Player_list = LIST: [player number, balance, score, bet]
•	Players = INT: number of players
•	Deck = LIST: 2d list of cards 
•	Cards_dealt = LIST: 2d list of cards that have been dealt. Only used in first round to assign values for the cards they get. 
•	Dealer_score = INT: initial dealer score with first 2 cards
•	Dealer_score_2 = INT: final dealer score

MENU MODULE:
•	Menu – greeting, would you like to see the rules
•	Blackjack_rules – print rules
•	Get_players – returns number of players and returns to player list for player number
•	Get_balance – enter starting balance for players  – returns to player list
•	Get_bet – user enters bet and subtracts from balance – returns to player list
•	Reset_player_hands – will clear player hand for next round

DEAL MODULE:
•	Fill_deck – Fills full deck
•	Shuffle – shuffles full deck

•	Deal_cards: First round of 2 cards each.
o	Checks deck length, if cards less then players * 2, calls fill deck and shuffle.
•	Get_player_scores
•	Get_dealer_score

ROUNDS MODULE:
•	Round: check for 21, send to play
•	Play: gives player score and asks to hit or stay
•	Dealer_round


WINNER MODULE:
•	Get_final_points: prints players final points
•	Get_winner: compares players to dealer score and prints winners.


MAIN:
•	card_values
•	card_total
•	main
Executes all modules for the game.

GAMEPLAY:

Menu: welcome, print rules yes or no
Menu: get number of players
Menu: get balance (all players will start with the same balance)
Menu: Create player list (player#, balance, score)
Menu: Place bets, update balance in player list

*Deal: Fill deck
Deal: shuffle deck
Deal: deal cards, create cards dealt list
Deal: assign cards dealt to players and get score

Rounds: Play round for each player, hit or stay. Get final score.

Deal: get dealer initial cards dealt.

Dealer: get dealer initial score
Dealer: hit on lower then 17 and get dealer final score

Winner: print player final points
Winner: compare points and display winners.
Play again? If yes, go to deal: fill deck*

