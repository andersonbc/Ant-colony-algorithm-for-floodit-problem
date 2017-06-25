"""
Created on 28/05/2017

@author: Anderson Botelho
         Raphael Miranda
"""
import numpy as np
import time
import timeit
from floodIt.src.initial_solution import get_movements_and_initialSolutionGraph


def generateGraph():
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
    print(cuts)



    counter = 0

    graph = {}
    for i in range(0, row*col):
        graph[counter] = {}
        graph[counter]['color'] = cuts[i]
        graph[counter]['edges'] = []

        if(i == 0):
            graph[counter]['edges'].append(i + 1)
            graph[counter]['edges'].append(i + col)
        elif (i == col-1):
            graph[counter]['edges'].append(i - 1)
            graph[counter]['edges'].append(i + col)
        elif (i == col*row-col):
            graph[counter]['edges'].append(i + 1)
            graph[counter]['edges'].append(i - col)
        elif (i == (col*row-1)):
            graph[counter]['edges'].append(i - 1)
            graph[counter]['edges'].append(i - col)


        elif i < col: # Primeira linha
            #print(i)
            graph[counter]['edges'].append(i+1)
            graph[counter]['edges'].append(i-1)
            graph[counter]['edges'].append(i+col)


        elif i%col == 0: #Primeira coluna
            #print(i)
            graph[counter]['edges'].append(i+1)
            graph[counter]['edges'].append(i+col)
            graph[counter]['edges'].append(i-col)

        elif i%col == col-1: #Ultima coluna
            #print(i)
            graph[counter]['edges'].append(i-1)
            graph[counter]['edges'].append(i+col)
            graph[counter]['edges'].append(i-col)

        elif i > ((col*row)-col): #Ultima linha
            # print(i)
            graph[counter]['edges'].append(i+1)
            graph[counter]['edges'].append(i-1)
            graph[counter]['edges'].append(i-col)
        else:
            print(cuts[i])
            graph[counter]['edges'].append(i+1)
            graph[counter]['edges'].append(i-1)
            graph[counter]['edges'].append(i+col)
            graph[counter]['edges'].append(i-col)
        counter+=1

    # print(graph)

    matrix = np.reshape(cuts, (-1, row))
    print("Instance: ")
    print(matrix)
    print('')

    print(graph);


    return graph, num_colors


def main():

    graph, num_colors = generateGraph()

    start = time.time()
    #start = time.time()
    #t = timeit.Timer( lambda: get_movements_and_initialSolution(matrix, num_colors))
    #t.repeat(1)
    movements, initial_solution = get_movements_and_initialSolutionGraph(graph, num_colors)
    print(graph)
    #print(movements, initial_solution)
    end = time.time()
    print(end - start)
    # end = time.time()
    # print ("Movements: " + str(movements))
    # print('')
    # print("Initial Solution: ")
    # print(initial_solution)
    # print('')
    # print("Result Matrix: ")
    # print(matrix)
    # print("Time: ")
    # print(end-start)
          
          
if __name__ == '__main__':
    main()