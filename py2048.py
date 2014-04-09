import os, msvcrt, random
import numpy as np

def init():
    board = np.zeros((4, 4))
    zeroPos = np.where(np.array(board) == 0)
    totalLen = zeroPos[0].size
    selNonZeroPos = random.sample(range(totalLen), 2)
    board[zeroPos[0][selNonZeroPos], zeroPos[1][selNonZeroPos]] = [2, 2]
    print board
    return board

def calMove(board, direction):
    if direction == 'a':
        for iRow in xrange(4):
            for iCol in xrange(3):
                if board[iRow, iCol] is not None:
                    if (board[iRow, iCol] == board[iRow, iCol + 1]):
                        board[iRow, iCol] = board[iRow, iCol]*2
                        board[iRow, iCol+1] = 0
            nonZero = np.where(board[iRow, :])   
            if nonZero[0].size:       
                board[iRow, 0:nonZero[0].size] = board[iRow, nonZero[0]]
                board[iRow, nonZero[0].size:] = 0            

    elif direction == 'w':
        for iCol in xrange(4):
            for iRow in xrange(3):
                if board[iRow, iCol] is not None:
                    if (board[iRow, iCol] == board[iRow + 1, iCol]):
                        board[iRow, iCol] = board[iRow, iCol]*2
                        board[iRow + 1, iCol] = 0
            nonZero = np.where(board[:, iCol])   
            if nonZero[0].size:       
                board[0:nonZero[0].size, iCol] = board[nonZero[0].T, iCol]
                board[nonZero[0].size:, iCol] = 0 
    elif direction == 'd':
        board = np.fliplr(board)
        board = calMove(board, 'a')
        board = np.fliplr(board)
    elif direction == 's':
        board = np.flipud(board)
        board = calMove(board, 'w')
        board = np.flipud(board)
    print "After Move"
    print board
    return board

def refresh(board):
    nonZeroPos = np.where(np.array(board) == 0)
    if nonZeroPos[0].size<1:
        print "You Lose !!"
        os.sys.exit()
    elif nonZeroPos[0].size<2:
        board[nonZeroPos[0], nonZeroPos[1] ]= random.choice((2,4));
    elif nonZeroPos[0].size>=2:
        selNonZeroPos = random.sample(range(nonZeroPos[0].size), 2)
        board[nonZeroPos[0][selNonZeroPos], nonZeroPos[1][selNonZeroPos]] = [random.choice((2,4)),random.choice((2,4))]
    os.system('cls')
    print "After Refresh"
    print board
    return board


if __name__ == '__main__':
    keyPool = ("w", "s", "a", "d")
    board  = init()   
    while True:
        keyDown = msvcrt.getch()
        print keyDown
        if keyDown in keyPool:        
            board = calMove(board, keyDown)
            board = refresh(board)
        elif keyDown == "esc":
            break
        else:
            print "Supported Keys: a, s, d, w, esc"
            print "Press ESCto exist"