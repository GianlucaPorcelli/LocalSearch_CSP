from algorithms import *
from utili import *
from node import*
from copy import *

#Variabili
#Creo griglia di partenza
griglia = [[3,0,6,5,0,8,4,0,0],
            [5,2,0,0,0,0,0,0,0],
            [0,8,7,0,0,0,0,3,1],
            [0,0,3,0,1,0,0,8,0],
            [9,0,0,8,6,3,0,0,5],
            [0,5,0,0,9,0,6,0,0],
            [1,3,0,0,0,0,2,5,0],
            [0,0,0,0,0,0,0,7,4],
            [0,0,5,2,0,6,3,0,0]]

#Lista delle variabili assegnate
assegnati = []
#Vado ad inserire nella lista dei nodi assegnati quelli che mi vengono già dati dal problema
for i in range(0, len(griglia)):
    for j in range(0, len(griglia[i])):
        if griglia[i][j] != 0:
            assegnati.append(Node([i, j], griglia[i][j], []))

dominio = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_zeri = []
completo = True
for i in range(0, len(griglia)):
    for j in range(0, len(griglia[i])):
        if griglia[i][j] == 0:
            completo = False
            lista_zeri.append(Node([i, j], deepcopy(dominio), []))


# #Lista delle variabili con valore assegnato
# var = []
# variabili = []
#
# #Assegno a ciascuna variabile i possibili colori
# for i in range(0, len(variabile)):
#     oggetto = Node(variabile[i], deepcopy(dominio), [])
#     variabili. append(oggetto)


#Assegnazione(variabili, color)
#variabili = AC3(variabili, vincoli)

aux = Backtracking(griglia, dominio, assegnati, lista_zeri)

if aux == False:
    print("Non esiste soluzione")
else:
    stampa(aux)


