import numpy as np
import time
# check if number n can be placed at board in pos (x,y)
def validate(board, n, row, col):

    max_r = len(board)
    max_c = len(board[0])
    c = [[] for i in range(0, max_c)]
    r = [[] for j in range(0, max_r)]
    b = []

    # get all col and rows
    for x in range(0, max_r):
        for y in range(0, max_c):
            c[x].append(board[y][x])
            r[y].append(board[y][x])
    # get blocks
    split_c = np.hsplit(board,3)
    for m in range(len(split_c)):
        b.append(np.vsplit(split_c[m],3))            
    
    #check col
    if n in c[col]:
        return False
    #check row
    if n in r[row]:
        return False
    #check block
    if n in b[col//3][row//3]:
        return False 
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None

def solve(board):
    solve.board = board
    find = find_empty(solve.board)
    if not find:
        return True
    else:
        i, j = find
    
    for k in range(1,10):
        if validate(board=solve.board,n=k,row=i,col=j):
            solve.board[i][j] = k
            if solve(solve.board):
                return True
            board[i][j] = 0                        
    return False

def sudoku(puzzle):
    solve(np.array(puzzle))
    return solve.board.tolist()