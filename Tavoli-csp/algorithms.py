from utili import *
from copy import *

def Backtracking(variabili, dominio, conflitti, assegnati):
    ausiliaria = deepcopy(variabili)

    #Lista contenente gli oggetti regione con i possibili valori del dominio modificati durante il forwarding
    dom = ''

    #Verifico se ho assegnato tutte le variabili
    #Se la dimensione delle variabili è uguale a 0, significa che ho assegnato tutte le variabili
    if len(variabili) == 0:
        return assegnati

    #AC3verifica = AC3(variabili, conflitti)  # Commentare questa linea per farlo funzionare

#if AC3verifica == True:
    #Assegno valore alla variabile
    var_aux = assegna_var(variabili) #Assegna variabili standard
    #var_aux = grado(variabili, conflitti)


    #Per ogni valore che può assumere la variabile, verifico che sia consistente
    for i in range(0, len(var_aux.valore)):
        vuoto = False
        aux = verifica_vincoli(var_aux.variabile, conflitti, var_aux.valore[i], assegnati)
        if aux == True:
            assegnati.append([var_aux.variabile, var_aux.valore[i]])
            #Variabile che mi serve per riaggiungere il colore alle regioni vicine nel caso faccio backtracking
            dom = var_aux.valore[i]
            #Passo alla funzione la variabile e il colore appena assegnati e la lista dei conflitti
            #forwarding(var_aux.variabile, var_aux.valore[i], conflitti, variabili, 1, ausiliaria)
            #Richiamo BackTracking
            back_track = Backtracking(variabili, dominio, conflitti, assegnati)
            #Se mi restituisce false, significa che devo considerare un altro colore
            if back_track != False:
                return assegnati
            else:
                #Rimuovo l'ultima tupla da assegnati
                assegnati.pop()
                #forwarding(var_aux.variabile, var_aux.valore[i], conflitti, variabili, 2, ausiliaria)

    #Inserisco nuovamente la regione in variabili in quanto non esiste nessuna soluzione per quella regione
    variabili.append(var_aux)

    #Devo inserire nuovamente il colore della variabile che ho ripristinato a tutti i domini delle variabili confinanti
    # if dom != '':
    #     if dom not in var_aux.valore:
    #         forwarding(var_aux.variabile, dom, conflitti, variabili, 2, ausiliaria)

    return False

