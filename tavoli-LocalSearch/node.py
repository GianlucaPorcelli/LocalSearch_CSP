class Node(object):
    def __init__(self, state, litigi, famiglia1,famiglia2,all):
        # state = stato attuale in quel nodo
        self.state = state
        self.litigi = litigi
        self.heuristic = vincoli(state,litigi)+myFamily(state,famiglia1,famiglia2,all)


def vincoli(state,litigi):
    num=0
    for i in range(0,len(state)-1):
        for j in range (0,len(state[i])):
            vincoli = ricerca(state[i][j], litigi)
            if vincoli!=None:
                for k in range(0,len(vincoli)):
                    if vincoli[k] in state[i]:
                        #print("stato: ",state)
                        #print(vincoli[k]," è allo stesso tavolo di qualcuno con cui ha litigato\n")
                        num+=1
    return num      #per l'algoritmo implementato se io ho litigato con te e tu con me il numero di errori è pari a 2
                            # quindi la metà di num rappresenta i vincoli non rispettati

def ricerca(obj,litigi):
    vincoli=[]              #la lista è necessaria in caso di più litigi di una persona
    for i in range (0,len(litigi)):
        if obj==litigi[i][0]:
            vincoli.append(litigi[i][1])    #se il primo elemento è quello cercato, il secondo sarà colui con cui ha litgato
        if obj==litigi[i][1]:
            vincoli.append(litigi[i][0])      #se il secondo elemento è quello cercato, il primo sarà colui con cui ha litgato
    return vincoli

def myFamily(state,famiglia1,famiglia2,all):
    count=0
    #variabili contenenti gli elementi di ciascuno dei 3 tavoli
    S0=set(state[0])
    S1=set(state[1])
    S2=set(state[2])

    #Variabili contenenti i componenti della famiglia
    F1=set(famiglia1)
    F2=set(famiglia2)
    tutti=set(all)
    #Se qualcuno della famiglia1 è ad un tavolo per ognuno della famiglia stessa seduto ad un'altro tavolo è previsto un aumento dell'euristica
    if (len(S0.intersection(F1)))>0:
        if (len(S1.intersection(F1))+len(S2.intersection(F1)))>0: #quanti della mia famiglia sono seduti ad altri tavoli
            count += 1
    if (len(S1.intersection(F1)))>0:
        if (len(S0.intersection(F1))+len(S2.intersection(F1)))>0:
            count += 1
    if len(S2.intersection(F1))>0:
        if (len(S0.intersection(F1))+len(S1.intersection(F1)))>0:
            count += 1

    # Se qualcuno della famiglia2 è ad un tavolo per ognuno della famiglia stessa seduto ad un'altro tavolo è previsto un aumento dell'euristica
    if (len(S0.intersection(F2)))>0:
        if (len(S1.intersection(F2))+len(S2.intersection(F2)))>0:                          #quanti della mia famiglia sono seduti ad altri tavoli
            count += 1
    if (len(S1.intersection(F2)))>0:
        if (len(S0.intersection(F2))+len(S2.intersection(F2)))>0:
            count += 1
    if len(S2.intersection(F2))>0:
        if (len(S0.intersection(F2))+len(S1.intersection(F2)))>0:
            count += 1
    return count