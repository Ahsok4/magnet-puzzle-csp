from state import *
from csp import *


if __name__ == "__main__":
    
    input_numbers = []
    input = open('input.txt').readlines()
    for line in input:
        line = line.rstrip()
        numbers = line.split(' ')
        n = [int(number) for number in numbers]
        input_numbers.append(n)
    
    
    n, m = input_numbers[0]   
    bound_y = input_numbers[1:3]
    bound_x = input_numbers[3:5]
    
    State.bound_y = bound_y
    State.bound_x = bound_x
    
    domain = []
    for i in range(0, n):
        d = []
        for j in range (0, m):
            d.append(['+', '-', ' '])
        domain.append(d)
            
    board = input_numbers[5:]
    
    State.board = board
    State.domain = domain
    # print(State.bound_x[0])
    # print(State.bound_x[1])
    
    
    backtrack(board, domain)
    
    
    
    
