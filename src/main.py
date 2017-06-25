'''
Created on 28/05/2017

@author: Raphael
'''
import numpy as np
import time
import timeit
from initial_solution import get_movements_and_initialSolution

row, col = 0, 0

def generateMatrix():
    fileTxt = open('../instances/color_seq_medium/matseq_12_12_6_1.txt')
    lines = fileTxt.read()
    fileTxt.close()

    cuts = []
    cuts = lines.split()
    row, col, num_colors = int(cuts[0]), int(cuts[1]), int(cuts[2]) 

    cuts.remove(cuts[0])
    cuts.remove(cuts[1])
    cuts.remove(cuts[2])

    cuts = [int(i) for i in cuts]

    matrix  = np.reshape(cuts, (-1, row))

    print("Instance: ")
    print(matrix)
    print('')

    return matrix, num_colors


def main():
    
    movements = 0
    solution = []
    matrix, num_colors = generateMatrix()
    trail = []
    
    best_ant = {}
    best_ant['movements'] = 0
    best_ant['solution'] = []
    best_ant['matrix'] = matrix
    
    start = time.time()
 

    #t = timeit.Timer( lambda: get_movements_and_initialSolution(matrix, num_colors))
    #t.repeat(1)
    
    
    for i in range(0, 10):
        copy_matrix = np.copy(matrix)        
        movements, solution = get_movements_and_initialSolution(copy_matrix, num_colors)
        
        if best_ant['movements'] == 0:
            best_ant['movements'] = movements
            best_ant['solution'] = solution
            best_ant['matrix'] = copy_matrix
             
        elif movements < best_ant['movements']:
            best_ant['movements'] = movements
            best_ant['solution'] = solution
            best_ant['matrix'] = copy_matrix
         
        for i in range(0, len(solution)):
            
            if i >= len(trail):
                colors = {}
                colors[solution[i][0]] = solution[i][1]    
                trail.append(colors)
            
            elif solution[i][0] in trail[i]:
                trail[i][solution[i][0]] = trail[i][solution[i][0]] + solution[i][1] 
            #coloca na trilha as cores utilizadas com seus feromônios
            else:
                trail[i][solution[i][0]] = solution[i][1]
           
    print('')        
    print("Trilha:")
    print(trail)
      
    end = time.time()
    print('')
    print("Best Ant:")
    print('')
    print ("    Movements: " + str(best_ant['movements']))
    print('')
    print("    Solution: ")
    print(best_ant['solution'])
    print('')
    print("    Result Matrix: ")
    print(best_ant['matrix'])
    print("Time: ")
    print(end-start)
    
if __name__ == '__main__':
    main()