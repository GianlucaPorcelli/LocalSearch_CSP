from algorithms import *
from utili import *
from node import*
from copy import *


#Variabili
cap_container = 6 #Capienza Container
variabile = ['t1', 't2', 't3', 't4', 't5', 'f1', 'f2', 'f3', 'e1', 'e2', 'fz1', 'fz2', 'fz3', 'fs1']
dominio = ['C1', 'C2', 'C3', 'C4']

vincoli = [[['t1', 't2', 't3', 't4', 't5'], ['f1', 'f2', 'f3']], #Rifiuti e derrate non stesso container
            ['e1', 'e2'], #Esplosivi
            ['fz1', 'fz2', 'fz3'], #Suregelati devono stare tutti insieme
            [['fs1'],['fz1', 'fz2', 'fz3']], #Freschi e surgelati non possono stare nello stesso container
            cap_container]

#Lista delle variabili con valore assegnato
var = []
variabili = []

#Assegno a ciascuna variabile i possibili colori
for i in range(0, len(variabile)):
    oggetto = Node(variabile[i], deepcopy(dominio), [])
    variabili.append(oggetto)


#Assegnazione(variabili, color)

aux = Backtracking(variabili, dominio, vincoli, var)
if aux == False:
    print("Non esiste soluzione")
else:
    print("Soluzione: ", aux)


