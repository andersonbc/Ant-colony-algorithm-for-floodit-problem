# encoding: utf-8

from random import randrange
import numpy as np

def get_movements_and_initialSolutionGraph(graph, num_colors):
    movements = 0
    initial_solution = []
    while not filldoneGraph(graph):
        neighbors = []
        visitados = []
        candidatos = []

        
        get_neighborsGraph(graph, neighbors, visitados, candidatos)
        print("Candidatos: " + str(candidatos)) #Mostra quais são os visinhos diretos que podem ser inuncados
        print("Troca Cores de: " + str(neighbors)) #Mostra quais já estão inundados e vão trocar de cor


        new_color = randrange(0,num_colors) # Escolhe uma cor aleatória

        print("Nova cor: " + str(new_color))
        
        movements = movements + 1
        initial_solution.append((new_color, 1))
        fillGraph2(graph, neighbors, new_color)

        print(graph)

    return movements, initial_solution
    
def filldoneGraph(graph):
    src = graph[0]['color']
    flag = True
    for i in graph:
        if graph[i]['color'] != src:
            flag = False
    return flag


def get_neighborsGraph(graph, neighbors, visitados, candidatos,  posicao=0):
    pivotColor = graph[0]['color']  # Pega a cor do pivo

    pilha = []
    pilha.append(posicao)
    neighbors.append(posicao)


    while len(pilha) > 0:
        elemento = pilha.pop()
        for i in graph[elemento]['edges']:
            #print("teste" + str(i))
            if (graph[i]['color'] == pivotColor) and (not any(i == j for j in visitados)):
                pilha.append(i)
                neighbors.append(i)
            elif(not any(i == j for j in visitados)):
                candidatos.append(i)
                #print(elemento)
            visitados.append(i)



    # for i in graph[posicao]['edges']:
    #     print("Visitados: " + str(i))
    #     jaVisitado = False
    #     for j in neighbors:
    #         if j == i:
    #             jaVisitado = True
    #     if jaVisitado:
    #         continue
    #
    #
    #     if (graph[i]['color'] == pivotColor):
    #         # visit = not any(posicao == i for i in visitados)
    #         # if visit:
    #         Visit = False
    #         for j in visitados:
    #             if j == i:
    #                 Visit = True
    #         if not Visit:
    #             visitados.append(i)
    #             get_neighborsGraph(graph, neighbors, visitados, i)




def fillGraph2(graph, neighbors, new_color):
    for i in neighbors:
        graph[i]['color'] = new_color
    return