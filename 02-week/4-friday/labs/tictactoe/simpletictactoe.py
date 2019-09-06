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



board = ['_' for x in range(10)]

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
 	  
    while True:
        player1 = []
        print('Player 1 enter your number')
        x = input('Pick a number from 1-9: ')
        x = int(x)
        board[x] = 'X'
        print(board)
    else:
        player2 = []
        print('Player 2 enter your number')
        x = input('Pick a number from 1-9: ')
        x = int(o)
        board[0] = 'O'
        print(board)

        


printBoard(board)



