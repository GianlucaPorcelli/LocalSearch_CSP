# coding=utf-8
alfa=0
beta=0
gamma=0
class Node(object):
    def __init__(self,tabella):
        # state = stato attuale in quel nodo
        self.tabella = tabella
        self.righe = righe(self.tabella)
        self.colonne = colonne(self.tabella)
        self.quadrati = quadrati(self.tabella)
        #[eur,pos]=euristica(tabella)
        self.heuristic = vincoli(self.righe) + vincoli(self.colonne) + vincoli(self.quadrati)
        #self.distance = eur
        #self.posizioni=pos

def righe(tabella):
    righe = []
    sum = 0
    for i in range(0, 9):
        righe.append(tabella[sum:sum + 9])
        sum += 9
    return righe

def colonne(tabella):
    colonne = []
    for j in range(0, 9):
        sum = 0
        colonna = []
        for i in range(0, 9):
            colonna.append(tabella[sum + j])
            sum += 9
        colonne.append(colonna)
    return colonne

def quadrati(tabella):
    quadrati = []
    salto = 0
    riga=0
    for k in range(0, 9):
        quadrato = []
        if k==3 or k==6:
            riga+=18
        sum = 0
        for i in range(0, 3):
            for j in range(0, 3):
                quadrato.append(tabella[j +sum + salto + riga])
            sum += 9
        quadrati.append(quadrato)
        salto += 3
        #print("jump: ",salto)
    return quadrati


def euristica(tabella):
    eur = 0
    posizioni=[]
    for i in range(0,len(tabella)):
        if tabella[i]=="-":
            posizioni.append(i)
            eur+=1
    return (eur,posizioni)

def vincoli(control):
    k=0
    for i in range (0,9):
        if (control[i].count(1))>1:
            k+=control[i].count(1)
        if (control[i].count(2))>1:
            k+=control[i].count(2)
        if (control[i].count(3))>1:
            k+=control[i].count(3)
        if (control[i].count(4))>1:
            k+=control[i].count(4)
        if (control[i].count(5))>1:
            k+=control[i].count(5)
        if (control[i].count(6))>1:
            k+=control[i].count(6)
        if (control[i].count(7))>1:
            k+=control[i].count(7)
        if (control[i].count(8))>1:
            k+=control[i].count(8)
        if (control[i].count(9))>1:
            k+=control[i].count(9)
    return k
