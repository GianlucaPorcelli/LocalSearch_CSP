from node import*
from copy import*
import random

# def minimo(coda):
#     min=10000000
#     Nodo=None
#     for i in range(0,len(coda)):
#         #print(coda[i].heuristic,coda[i].state)
#         if coda[i].heuristic<min:
#         #if vincoli(coda[i].state,coda[i].litigi)<min:
#             Nodo=coda[i]
#             min=coda[i].heuristic
#             #min=vincoli(coda[i].state,coda[i].litigi)
#     return Nodo

def HillClimbing(root):
    path=root
    var=0
    while True:
        var+=1
        POS=random.randint(0,len(path.tabella)-1)
        minimum=fringeMIN(path,POS)     #funzione che espande tutti i nodi vicini e ne restituisce solo quello con euristica minima
        if var%500==0:
            # for i in range(0, 81):
            #     print("|", minimum.tabella[i], "|", end='')
            #     if (i + 1) % 9 == 0:
            #         print(" ")
            print("Euristica: ",minimum.heuristic)
            #break
        if minimum.heuristic==0:
            path = Node(deepcopy(minimum.tabella))
            # for i in range(0, 81):
            #     print("|", minimum.tabella[i], "|", end='')
            #     if (i + 1) % 9 == 0:
            #         print(" ")
            # print(minimum.heuristic)
            return path
        if minimum!=None:
            if minimum.heuristic>path.heuristic:
                print("\n---------------------------------------------------------------------------------------------------------------------")
                print("Algoritmo HillClimbing non terminabile perchè i nodi generabili hanno euristica maggiore del nodo generatore")
                print("Il prossimo invitato da far sedere non può sedersi con la sua famiglia perchè ha litigato con qualcuno a quel tavolo")
                print("---------------------------------------------------------------------------------------------------------------------\n")
                return None
            else:
                path=Node(deepcopy(minimum.tabella))                             #Il prossimo nodo da espandere è il migliore della lista dei generati
        else:
            print("Soluzione non esistente")
            return None

def fringeMIN(path,POS):
    m=path.heuristic
    minimo=path
    for i in range(0, len(path.tabella)):
        table = deepcopy(path.tabella)  # faccio una copia dello stato padre
        aux = table[i]
        table[i] = table[POS]
        table[POS] = aux
        NODO = Node(table)
        # print("Nodo: ",NODO.heuristic," pos: ",POS)
        # for i in range(0, 81):
        #     print("|", NODO.tabella[i], "|", end='')
        #     if (i + 1) % 9 == 0:
        #         print(" ")
        if NODO.heuristic<=m:
            if NODO.heuristic==m:
                sorteggio = random.randint(0, 1)
                if sorteggio==1:
                    minimo=NODO
                    m=NODO.heuristic
            else:
                minimo = NODO
                m = NODO.heuristic
    return minimo