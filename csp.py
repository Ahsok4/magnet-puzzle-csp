import math

def backtrack(state):
    
    x, y = mrv(state)
    domain = state.domain
    
    for d in domain:
        new_board = state.board
        new_board[x][y] = d
        
    
    
    
def finished(state):
    return

def mrv(state):
    min = math.inf
    for i in range(0, len(state.domain)):
        for j in range(0, len(state.domain[0])):
            size = len(state.domain[i][j])
            if (size < min):
                min = size
                x, y = i, j
                
    return x, y
        
    