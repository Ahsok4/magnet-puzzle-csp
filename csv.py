import math

def backtrack(state):
    
    v = mrv(state)
    print(v)
    
    
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
        
    