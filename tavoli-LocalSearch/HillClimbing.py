from node import*
from copy import*
import random


def minimo(coda):
    min=100
    Nodo=None
    for i in range(0,len(coda)):
        #print(coda[i].heuristic,coda[i].state)
        if coda[i].heuristic<min:
        #if vincoli(coda[i].state,coda[i].litigi)<min:
            Nodo=coda[i]
            min=coda[i].heuristic
            #min=vincoli(coda[i].state,coda[i].litigi)
    return Nodo

def HillClimbing(root,litigi,famiglia1,famiglia2,all):
    path=root
    while True:
        #print("root litigate: ", root.litigate)
        TAVrnd=random.randint(0,2)
        POSrnd=random.randint(0,len(path.state[TAVrnd])-1)
        coda=fringe(path,TAVrnd,POSrnd,litigi, famiglia1, famiglia2,all)
        minimum=minimo(coda)                        #estraggo dalla lista il nodo con l'euristica minore
        if minimum.heuristic==0:
            path = Node(deepcopy(minimum.state), litigi, famiglia1, famiglia2, all)
            return path
        if minimum!=None:
            if minimum.heuristic>path.heuristic:
                print("\n---------------------------------------------------------------------------------------------------------------------")
                print("Algoritmo HillClimbing non terminabile perchè i nodi generabili hanno euristica maggiore del nodo generatore")
                print("Il prossimo invitato da far sedere non può sedersi con la sua famiglia perchè ha litigato con qualcuno a quel tavolo")
                print("---------------------------------------------------------------------------------------------------------------------\n")
                return None
            else:
                path=Node(deepcopy(minimum.state),litigi,famiglia1,famiglia2,all)                             #Il prossimo nodo da espandere è il migliore della lista dei generati
        else:
            print("Soluzione non esistente")
            return None

def fringe(path,TAV,POS, litigi, famiglia1, famiglia2,all):
    coda = []
    for i in range(0, len(path.state) - 1):
        for j in range(0, len(path.state[i])):
            stato = deepcopy(path.state)  # faccio una copia dello stato padre
            aux = stato[i][j]
            stato[i][j] = stato[TAV][POS]  # aggiungo al tavolo i-esimo il rossimo da sistemare
            stato[TAV][POS] = aux  # rimuovo la persona sistemata da quelle in attesa di posto
            NODO = Node(stato, litigi, famiglia1, famiglia2,all)  # instanzio un nodo figlio aggiungendo la persona "next" al tavolo i-esimo
            coda.append(NODO)  # aggiungo il nodo ad una coda dal quale estrarrò i nodo con euristica minore
    return coda