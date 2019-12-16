from utili import *
from node import *
from copy import *

def Backtracking(griglia, dominio, assegnati, zeri):
    #Lista contenente tutti gli 0 all'interno della griglia
    # ausiliaria = deepcopy(variabili)
    #
    #Lista contenente gli oggetti regione con i possibili valori del dominio modificati durante il forwarding
    dom = ''

    # Verifico se ho assegnato tutte le variabili
    # Se in tutte le liste che compongono la griglia non sono presenti 0 significa che ho completato


    #Se non ho trovato 0 restituisco la griglia
    if len(zeri) == 0:
        return griglia


    #Assegno valore alla variabile
    var_aux = assegna_var(zeri) #Assegna variabili standard
    #var_aux = grado(variabili, conflitti)


    #Per ogni valore che può assumere la variabile, verifico che sia consistente
    for i in range(0, len(var_aux.valore)):
        vuoto = False
        aux = verifica_vincoli(var_aux.variabile, var_aux.valore[i], assegnati, griglia)
        if aux == True:
            assegnati.append(Node([var_aux.variabile[0], var_aux.variabile[1]], var_aux.valore[i], []))
            griglia_finale = deepcopy(crea_griglia(assegnati, griglia))
            #Variabile che mi serve per riaggiungere il colore alle regioni vicine nel caso faccio backtracking
            dom = var_aux.valore[i]
            #Passo alla funzione la variabile e il colore appena assegnati e la lista dei conflitti
            forwarding(var_aux.variabile, var_aux.valore[i], zeri, griglia, 1)
            #Richiamo BackTracking
            back_track = Backtracking(griglia_finale, dominio, assegnati, zeri)
            #Se mi restituisce false, significa che devo considerare un altro colore
            if back_track != False:
                return back_track
            else:
                #Rimuovo l'ultima tupla da assegnati
                assegnati.pop()
                forwarding(var_aux.variabile, var_aux.valore[i], zeri, griglia, 2)

    #Inserisco nuovamente la regione in variabili in quanto non esiste nessuna soluzione per quella regione
    zeri.append(var_aux)
    #Devo inserire nuovamente il colore della variabile che ho ripristinato a tutti i domini delle variabili confinanti
    if dom != '':
        if dom not in var_aux.valore:
            forwarding(var_aux.variabile, var_aux.valore[i], zeri, griglia, 2)

    return False