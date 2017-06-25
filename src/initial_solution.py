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

        candidato = escolheUmCandidato(candidatos)

        #new_color = randrange(0,num_colors) # Escolhe uma cor aleatória
        new_color = graph[candidato]['color']

        print("Nova cor: " + str(new_color))
        
        movements = movements + 1
        initial_solution.append((new_color, 1))
        fillGraph(graph, neighbors, new_color)

        #print(graph)

    return movements, initial_solution

def escolheUmCandidato(candidatos):
    candidato = candidatos[randrange(0, len(candidatos))]

    return candidato

    
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




def fillGraph(graph, neighbors, new_color):  #Colore todos os que estão inundados com a nova cor
    for i in neighbors:
        graph[i]['color'] = new_color
    return