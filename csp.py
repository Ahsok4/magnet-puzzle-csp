import math
from os import stat
from state import *

def backtrack(state:state):
    
    x1, y1 = mrv(state)
    domain = state.domain[x1][y1]
    
    for d in domain:
        new_board = state.board
        x2, y2 = get_other_pole(state, x1, y1)
        if (d == '+'):
            d_prime = '-'
        elif (d == '-'):
            d_prime = '+'
        elif (d == ' '):
            d_prime = ' '
            
        new_board[x1][y1] = d
        new_board[x2][y2] = d_prime
        
        new_domain = state.domain
        new_domain[x1][y1].remove(d)
        new_domain[x2][y2].remove(d_prime)
        
        new_state = state(new_board, state, new_domain, x1, y1, x2, y2)
        #forward check
        
      
def forward_check(state:state):
    n = len(state.board)
    m = len(state.board[0])
    
    if (state.x1-state.x2 == 0):
        is_vertical = False
    else:
        is_vertical = True      
        
      
    
    return  
        
def get_other_pole(state, x, y):
    board = state.board
    num = board[x][y]
    if (board[x][y-1] == num):
        return x, y-1
    elif (board[x][y+1] == num):
        return x, y+1
    elif (board[x-1][y] == num):
        return x-1, y
    elif (board[x+1][y] == num):
        return x+1, y
    
    return 'failure'
    
    
def finished(state):
    return

def mrv(state):
    min = math.inf
    for i in range(0, len(state.domain)):
        for j in range(0, len(state.domain[0])):
            size = len(state.domain[i][j])
            if (size < min and (state.board[i][j] != '+' or 
                                state.board[i][j] != '-' or 
                                state.board[i][j] != ' ')):
                min = size
                x, y = i, j
                
    return x, y
        
    