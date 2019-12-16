import random
from node import*
from copy import*
import random
def taglia(root):
    assegnati=[]
    rnd=0
    for i in range(0, 51):
        while rnd in assegnati:
            rnd = random.randint(0, 80)
        assegnati.append(rnd)
        root.tabella[rnd] = "-"
    return Node(root.tabella)

def stampa(root):
    print("righe:")
    for i in range(0,9):
        print(root.righe[i])

    print("colonne:")
    for i in range(0,9):
        print(root.colonne[i])

    print("quadrati:\n")
    for i in range(0,9):
        print(root.quadrati[i])
def inizio():
    i=1
    tabella=[]
    for j in range(0,81):
        tabella.append(i)
        if i==9:
            i=0
        i+=1
    root=Node(tabella)
    print(root.heuristic)
    #limit=100
    # while limit>0:
    #     tabella = []
    #     for i in range(0, 81):
    #         tabella.append("-")
    #     assegnati = []
    #     rnd = 0
    #     for i in range(0, 25):
    #         while rnd in assegnati:
    #             rnd = random.randint(0, len(tabella) - 1)
    #         assegnati.append(rnd)
    #         tabella[rnd] = random.randint(1, 9)
    #     root = Node(tabella)
    #     limit=root.heuristic-root.distance

    for i in range(0, 81):
        print("|", tabella[i], "|", end='')
        if (i + 1) % 9 == 0:
            print(" ")
    print("Euristica: ", root.heuristic)
    #print("posizioni: \n",root.posizioni)
    return root

def inserisci(root):
    rnd=random.randint(0,9)


