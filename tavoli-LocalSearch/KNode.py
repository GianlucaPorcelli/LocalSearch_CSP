from HillClimbing import*

import random

def initial(N,capienza,all):
    state = []
    for i in range(0, N):  # carico nello stato tante liste quanti sono i tavoli
        state.append([])
    state.append(all)  # l'ultimo elemento dello stato è rappresentato dalle persone da sistemare

    # -----------------------------------------------------------------------------------------------------------
    #DIMENSIONE DEI TAVOLI CASSUALE (<6) che non varierà durante il processo di ricerca
    if len(all) < N * capienza:  # se ho più persone da sistemare dei posti a disposizione il problema nn è risolvibile
        while (len(all) > 0):
            tavolo=random.randint(0,2)          #scelgo un tavolo casuale a cui aggiungere un invitato
            if (len(state[tavolo]) < capienza):
                x = random.choice(all)  # selezione un componente casuale dalla lista
                state[tavolo].append(x)  # aggiungo al tavolo i-esimo il componente scelto
                all.remove(x)  # elimino dalla lista il componente scelto
    #-----------------------------------------------------------------------------------------------------------
    #I primi tavoli saranno riempiti completamente lasciando l'ultimo tavolo parzialmente riempito
    # i=0
    # while (len(all) > 0):
    #     if len(state[i]) < capienza:
    #             x=all[random.randint(0,len(all)-1)]
    #             state[i].append(x)  # aggiungo al tavolo i-esimo il componente scelto
    #             all.remove(x)  # elimino dalla lista il componente scelto
    #     else:
    #         i+=1
    #-----------------------------------------------------------------------------------------------------------
    return state

def LocalBeamSearch(root,litigi,capienza,NUM,famiglia1,famiglia2,all):
    #print("\nInizio LocalBeamSearch:\n")
    coda = []
    # for i in range (0,NUM):
    #     coda.append(100)
    path=root
    TAVrnd = random.randint(0, 2)
    POSrnd = random.randint(0, len(path.state[TAVrnd]) - 1)
    coda = fringe(path, TAVrnd, POSrnd, litigi, famiglia1, famiglia2, all)
    #j=0
    while True:
        #print("HOP")
        #j+=1
        if (coda.count(coda[0]))==len(coda)-1:
            return None         #se in coda ci sono tutti nodi uguali non potrò continuare la ricerca
        TAVrnd = random.randint(0, 2)
        POSrnd = random.randint(0, len(path.state[TAVrnd]) - 1)#la dimensione dei tavoli non varia mai
        for i in range(0,len(coda)):
            fringeNUM(coda,coda[i],TAVrnd,POSrnd,litigi, famiglia1, famiglia2,all)
        # for i in range(0, len(coda)):
        #     print("coda",coda[i].heuristic, coda[i].state)
        # print("prima",len(coda))
        [coda,bol] = minNUM(coda, litigi, NUM,famiglia1,famiglia2,all)    #continuo l'espansione parallela degli NUM migliori nodi
        if bol==0:
            return coda
        #print("dopo",len(coda),bol)
    return None

def minNUM(coda,litigi,NUM,famiglia1,famiglia2,all):            #fa ritornare una lista contenente i migliori NUM nodi
    nodi=[]
    Nodo=None
    j=0
    if NUM > len(coda):
        return coda
    while j<NUM and len(coda)>0:
        min = 100
        for i in range(0,len(coda)):
            #print(coda[i].heuristic,coda[i].state)
            if coda[i].heuristic<=min:
                if coda[i].heuristic==0:
                    #print("yes")
                    return [coda[i],0]
                if coda[i].heuristic==min:
                    sorteggio=random.randint(0,1)
                    if sorteggio==1:
                        #print("yes")
                        stato=deepcopy(coda[i].state)
                        Nodo=Node(stato,litigi,famiglia1,famiglia2,all)
                        k=i
                        min=coda[i].heuristic
                else:
                    stato=deepcopy(coda[i].state)
                    Nodo=Node(stato,litigi,famiglia1,famiglia2,all)
                    k=i
                    min=coda[i].heuristic

        nodi.append(Nodo)
        #print(k,len(coda))
        del coda[k]
        j+=1
    return [nodi,1]


def fringeNUM(coda,path,TAV,POS, litigi, famiglia1, famiglia2,all):

    for i in range(0, len(path.state) - 1):
        for j in range(0, len(path.state[i])):
            stato = deepcopy(path.state)  # faccio una copia dello stato padre
            aux = stato[i][j]
            stato[i][j] = stato[TAV][POS]  # aggiungo al tavolo i-esimo il rossimo da sistemare
            stato[TAV][POS] = aux  # rimuovo la persona sistemata da quelle in attesa di posto
            NODO = Node(stato, litigi, famiglia1, famiglia2,all)  # instanzio un nodo figlio aggiungendo la persona "next" al tavolo i-esimo
            coda.append(NODO)  # aggiungo il nodo ad una coda dal quale estrarrò i nodo con euristica minore
            # if NODO.litigate>0:
            #     print("Nodo: ",NODO.litigate,NODO.state)

