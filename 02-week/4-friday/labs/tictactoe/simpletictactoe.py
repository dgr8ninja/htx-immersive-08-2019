# Write a function move that accepts three arguments:

#     board a 2-dimensional array that represents a 3x3 tic-tac-toe board

#     location a 2-item tuple that specifies an cell on the board

#     player a String, either "X" or "Y"

# Return a copy of the board with the player String placed at the location.

# Throw an error if:

#     The board is the wrong size
#     The location is already occupied by a player
#     The location is invalid
#     The player String is something other than "X" or "Y"

import random

def gameboard(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
#getting input from player
def player_input():
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose O or X to play!')
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
#place marker on borard
def place_marker(board,marker,postion):
    board[position] = marker
#Checking win or not 
def win_check (board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
# who first to go

def choose_first():
    rand_num = random.randint(0,1)
    if rand_num == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# checking space is free or not
def check_space(board,position):
    return board[position] == ' '
#full board check 
def full_board_check (board):
    for i in range (1,10):
        if check_space(board,i):
            return False
    return True


player_input()


