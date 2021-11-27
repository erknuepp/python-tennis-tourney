########grab a dataset and have it calculate who will win a match############

#import numpy as np
#import pandas as pd
import random


##create the players
players = ['CG', 'TP', 'FT', 'UH', 'DJ', 'GM', 'RO',
"CM", "LS", "CA", "JI", 'CN', 'AK', 'MC', 
'GD', 'RBA', 'AB', 'MG', 'HH', 'ADF', 'SK',
'LD', 'BN', 'MM', 'KA', 'KK', 'RG', 'AM', 
'FK', 'ADM', 'DE', 'DS', 'YN', 'LH', 'MF',
'FAA', 'HFT', 'ARV', 'DK', 'JLS', 'FF', 'NB',
'JS', 'FD', 'DG', 'GP', 'MK', 'BP',
'ST', 'AZ', 'DM', 'PCB','AR','DS', 'CR',
'MB']
players = players[:36]
print(players)
matches = len(players) / 2
player_next_round = []
match_number = 0
round = 0
while  match_number < matches:
    #players = player_next_round
    #player_next_round = []
    player1_index = 2 * match_number
    player2_index = player1_index + 1
    player_name_1 = players[player1_index]
    player_name_2 = players[player2_index]
    ##calculate how likely the player is to win
    probability_player1_wins = 0.5
    #randomize outcome
    if random.random() <= probability_player1_wins:
        player_next_round.append(player_name_1)
        print(player_name_1)
    else:
        player_next_round.append(player_name_2)
        print(player_name_2)
    match_number += 1
    player1_index += 1
    player2_index += 1
    





####the total players in the tournament
'''
total_matches = len(players) - 1
print(total_matches)
#print(total_matches)
match = 0
round = 0
next_round = []
#while matches are still to be played
while match < total_matches:
    if match in players:
        print('Starting a new round')
        players = next_round
        next_round = []
        round = 0

    #player 1 is first in the list then player2 is second in the list
    player1 = players[round] #currently indexing error
    player2 = players[round + 1]
    x = random.shuffle(players)
    if player1 < player2:  #i want to randomize here but don't know how to rand() isn't working
        next_round.append(player1)
        print(player1, "vs" , player2, "The winner is ", player1)

    else:
        next_round.append(player2)
        print(player1, "vs" , player2, "The winner is ", player2)


    match += 1
    round += 1
    print( "Next round matchup list is ", next_round)
    print("round # ", round)
print(next_round)

'''

