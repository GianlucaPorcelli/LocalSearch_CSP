from KNode import*
import numpy

a=[2,3,40]
print(a**2)

def genetic(root,litigi,famiglia1,famiglia2,all):
    path=root
    TAVrnd = random.randint(0, 2)
    POSrnd = random.randint(0, len(path.state[TAVrnd]) - 1)
    coda = fringe(path, TAVrnd, POSrnd, litigi, famiglia1, famiglia2, all)
    fringeNUM(coda, coda[0], TAVrnd, POSrnd, litigi, famiglia1, famiglia2, all)
    [coda, bol] = minNUM(coda, litigi, 4, famiglia1, famiglia2, all)
    for i in range (0,len(coda)):
        print("Nodo: ",coda[i].heuristic,coda[i].state)

    prob=[]
    sum=0
    for i in range(0,4):
        sum+=coda[i].heuristic
        prob.append(coda[i].heuristic)
    for i in range(0,len(prob)):
        prob[i]/=sum
        prob[i]=float(format(prob[i],'.2f'))
    print(sum,prob)
    codaG=[]
    #for i in range(0,4):
    codaG=random.choices(coda,weights=prob,k=4)
    for i in range(0, len(codaG)):
        print("Nodo: ",codaG[i].heuristic,coda[i].state)
    aux=[]
    new=[]
    i=0
    while i<len(codaG)-1:
        aux=codaG[i].state[2]
        codaG[i].state[2]=codaG[i+1].state[2]
        codaG[i+1].state[2]=aux
        new.append(codaG[i].state)
        new.append(codaG[i+1].state)
        i+=2
    for i in range(0,len(new)):
        print(new[i])