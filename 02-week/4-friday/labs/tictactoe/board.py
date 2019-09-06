def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    if isBoardFull(board):
     print('Tie Game!')