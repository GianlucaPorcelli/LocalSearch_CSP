from node import *
from copy import *

def stampa(griglia):
    for i in range(0, len(griglia)):
        if i == 3 or i == 6 or i == 9:
            print("= ", "= ", "= ", "||", "= ", "= ", "= ", "||", "= ", "= ", "= ")
        for j in range(0, len(griglia[i])):
            if j== 3 or j==6 or j == 9:
                print("||", griglia[i][j], " ", end='')
            else:
                print(griglia[i][j], " ", end='')
        print(" ")



def assegna_var(variabili):
    #Restituisce una lista con la variabile, e il dominio
    return variabili.pop()

def MRV(variabili, conflitti):

    print("Todo")

def grado(variabili, conflitti):
    grad = []
    for i in range(0, len(variabili)):
        grado = 0
        #Verifico la variabile in quante liste dei conflitti è presente
        for j in range(0, len(conflitti)-1):
            for z in range(0, len(conflitti[j])):
                if variabili[i].valore in conflitti[j][z]:
                    grado += 1
                # Memorizzo il grado dell'elemento in posizione i all'interno della lista grad
        grad.append(grado)
    # Memorizzati i gradi di tutte le variabili all'interno della lista, vado a vedere in quale posizione si trova
    # la variabile con grado più alto
    position = grad.index(max(grad))
    val = variabili[position]
    variabili.pop(position)
    return val

def meno_vincolante():
    print("Todo")

def verifica_vincoli(variabile, valore, var_assegnate, griglia):
    #Verifico che non ci siano gli stessi numeri sulla riga
    for j in range(0, len(griglia[variabile[0]])):
      #Verifico che non controllo la posizione della variabile che sto considerando
      if j != variabile[1]:
        if griglia[variabile[0]][j] == valore:
            return False

    #Verifico che non ci siano gli stessi numeri sulla colonna
    for i in range(0, len(griglia[variabile[1]])):
        # Verifico che non controllo la posizione della variabile che sto considerando
        if i != variabile[0]:
            if griglia[i][variabile[1]] == valore:
                return False

    # Verifico che non ci siano gli stessi numeri nel quadrato
    #Calcolo il primo elemento del quadrato che devo controllare
    r = int(variabile[0] / 3) * 3
    c = int(variabile[1] / 3) * 3

    for i in range(r, r+3):
        for j in range(c, c+3):
            if griglia[i][j] == valore:
                return False

    return True

def crea_griglia(assegnati, griglia):
    for i in range(0, len(assegnati)):
        #print(assegnati[i].variabile, assegnati[i].valore)
        griglia[assegnati[i].variabile[0]][assegnati[i].variabile[1]] = assegnati[i].valore

    return griglia


    # #Verifico che il tavolo non abbia raggiunto dimensione massima
    # #Vado a contare quante var_assegnate hanno come dominio il tavolo in esame
    # contatore = 0
    # for i in range(0, len(var_assegnate)):
    #     #Se il valore della variabile già assegnata è uguale al valore che sto considerando
    #     if var_assegnate[i][1] == valore:
    #         contatore += 1
    # #Visto che non posso avere un valore maggiore di 6, se contatore è uguale a 6 restituisco False in quanto ha già
    # #raggiunto dimensione massima
    # if contatore == conflitti[2]:
    #     return False
    #
    # #Controllo tutte le tuple appartenenti alla lista delle famiglie che a sua volta è presente nella lista vincoli
    # for j in range(0, len(conflitti[0])):
    #     #Se la variabile in esame è presente nella lista, significa che ho trovato la famiglia di appartenenza
    #     if variabile in conflitti[0][j]:
    #         # Verifico che non ci siano elementi della stessa famiglia in un altro tavolo
    #         for i in range(0, len(var_assegnate)):
    #             #Verifico che la variabile già assegnata che sto considerando appartenga alla stessa famiglia
    #             if var_assegnate[i][0] in conflitti[0][j]:
    #                 #Se ha valore diverso rispetto a quello che sto considerando, restituisco False, altrimenti passo a
    #                 #considerare la variabile successiva presente in quelle già assegnate
    #                 if var_assegnate[i][1] != valore:
    #                     return False
    #
    # #Verifico se compaio nella lista delle persone che hanno litigato
    # for j in range(0, len(conflitti[1])):
    #     #Se la variabile è presente nella lista, significa che ha litigato con qualcuno e quindi devo verificare che non
    #     #sia allo stesso tavolo
    #     if variabile in conflitti[1][j]:
    #         #Verifico che alla persona con cui ha litigato, non sia stato assegnato lo stesso tavolo
    #         for i in range(0, len(var_assegnate)):
    #             #Se la persona che sto controllando, appartiene alla lista, devo verificare che abbia un valore assegnato diverso
    #             if var_assegnate[i][0] in conflitti[1][j]:
    #                 if var_assegnate[i][1] == valore:
    #                     return False
    #
    # return True

def forwarding(variabile, valore, zeri, griglia, num):

    #Per ogni variabile presente nella lista degli zeri(ancora da assegnare)
    for i in range(0, len(zeri)):
        #Elimino dal dominio degli zeri che si trovano sulla stessa riga della variabile che sto assegnando, il valore appena assengato
        for j in range(0, len(griglia[0])):
            # Se l'attributo variabile dell' oggetto corrisponde con le coordinate che sto controllando
            if zeri[i].variabile == [variabile[0], j]:
                if num == 1:
                    #Rimuovo il valore dal suo dominio
                    if valore in zeri[i].valore:
                        zeri[i].valore.remove(valore)
                else:
                    if valore not in zeri[i].valore:
                        #Aggiungo il valore
                        zeri[i].valore.append(valore)

        # Elimino dal dominio degli zeri che si trovano sulla stessa colonna della variabile che sto assegnando, il valore appena assengato
        for z in range(0, len(griglia[1])):
            if zeri[i].variabile == [z, variabile[1]]:
                if num == 1:
                    # Rimuovo il valore dal suo dominio
                    if valore in zeri[i].valore:
                        zeri[i].valore.remove(valore)
                else:
                    if valore not in zeri[i].valore:
                        # Aggiungo il valore
                        zeri[i].valore.append(valore)

        # Elimino dal dominio degli zeri che si trovano nello stesso quadrato della variabile che sto assegnando, il valore appena assengato
        # Calcolo il primo elemento del quadrato che devo controllare
        r = int(variabile[0] / 3) * 3
        c = int(variabile[1] / 3) * 3

        for z in range(r, r + 3):
            for j in range(c, c + 3):
                if zeri[i].variabile == [z, j]:
                    if num == 1:
                        # Rimuovo il valore dal suo dominio
                        if valore in zeri[i].valore:
                            zeri[i].valore.remove(valore)
                    else:
                        if valore not in zeri[i].valore:
                            # Aggiungo il valore
                            zeri[i].valore.append(valore)

















    #
    # for j in range(0, len(conflitti[0])):
    #     # Se la variabile in esame è presente nella lista, significa che ho trovato la famiglia di appartenenza
    #     if variabile in conflitti[0][j]:
    #         # Elimino da tutte le altre variabili appartenenti alla stessa famiglia, tutti i valori eccetto quello che ho
    #         # scelto per la variabile che sto considerando
    #         for i in range(0, len(var_assegnare)):
    #             # Verifico che la variabile appartenga alla stessa famiglia
    #             if var_assegnare[i].variabile in conflitti[0][j]:
    #                 # Elimino dal dominio
    #                 for z in range(0, len(var_assegnare[i].valore)):
    #                     #Diversifico in quanto nel caso abbia fatto backtracking devo aggiungere invece di eliminare
    #                     if num == 1:
    #                         if var_assegnare[i].valore[z] != valore:
    #                             #Aggiungo a rimossi l'elemento che sto eliminando
    #                             var_assegnare[i].rimossi.remove(var_assegnare[i].valore[z])
    #                             delete.append(var_assegnare[i].valore[z])
    #
    #                     else:
    #                         # print("shshakDSKJDHSDHoiAUHDOIABDHADBKBdAJHBDKJABDkajHBDHABDjkAHBDKHABDkHABDKHABDkjABDJK")
    #                         # print(variabile)
    #                         for k in range(0, len(var_assegnare[i].rimossi)):
    #                             if var_assegnare[i].rimossi[k] not in var_assegnare[i].valore:
    #                                 var_assegnare[i].valore.append(var_assegnare[i].rimossi[k])
    #
    #                 for b in range(0, len(delete)):
    #                     var_assegnare[i].valore.remove(delete[b])
    #                 delete.clear()
    #
    # # Verifico se compaio nella lista delle persone che hanno litigato
    # for j in range(0, len(conflitti[1])):
    #     # Se la variabile è presente nella lista, significa che ha litigato con qualcuno e quindi devo verificare che non
    #     # sia allo stesso tavolo
    #     if variabile in conflitti[1][j]:
    #         # Verifico che alla persona con cui ha litigato, non sia stato assegnato lo stesso tavolo
    #         for i in range(0, len(var_assegnare)):
    #             # Se la persona che sto controllando, appartiene alla lista, devo verificare che abbia un valore assegnato diverso
    #             if var_assegnare[i].variabile in conflitti[1][j]:
    #                 #Elimino dal dominio della variabile nella lista assegnare il valore che ho scelto per il nodo in esame
    #                 if num == 1:
    #                     if valore in var_assegnare[i].valore:
    #                         var_assegnare[i].valore.remove(valore)
    #                 else:
    #                         if valore not in var_assegnare[i].valore:
    #                             var_assegnare[i].valore.append(valore)

def coda(variabili, conflitti):
    list1 = [] #Prima famiglia
    list2 = [] #Seconda famiglia
    list3 = [] #Persone che non parlano
    list4 = []

    #Creo coppie di nodi per le liste famiglia
    for i in range(0, len(variabili)-1):
        for j in range(i+1, len(variabili)):
            #Verifico se i due nodi appartengono alla stessa famiglia e nel caso li memorizzo nella lista corrispondente
            if variabili[i].variabile in conflitti[0][0] and variabili[j].variabile in conflitti[0][0]:
                list1.append([variabili[i], variabili[j]])
            if variabili[i].variabile in conflitti[0][1] and variabili[j].variabile in conflitti[0][1]:
                list2.append([variabili[i], variabili[j]])

    #Creo coppie di nodi per quelli che hanno litigatp
    for i in range(0, len(variabili)-1):
        for j in range(i+1, len(variabili)):
            for k in range(0, len(conflitti[1])):
                if variabili[i].variabile in conflitti[1][k] and variabili[j].variabile in conflitti[1][k]:
                    list3.append([variabili[i], variabili[j]])
    list4.append(list1)
    list4.append(list2)
    list4.append(list3)
    return list4


def AC3(variabili, conflitti):
    controllare = coda(variabili, conflitti)
    print(controllare)
    # controllati = []
    #
    # while len(controllare) != 0:
    #     x = controllare.pop()
    #     controllati.append(x)
    #
    #     #Verifico inconsistenza con i vicini
    #     list = rimuovo_inconsistenza(x, conflitti)
    #     if list != False:
    #         #Se è stato effettuato un cambio devo reinserire i nodi vicini nella lista da controllare
    #         for item in list:
    #             if item not in controllare:
    #                 controllare.append(item)
    #     else:
    #         #Restituisco False se non ho consistenza
    #         return False
    #
    # #Restituisco True se ho consistenza
    # return True

def rimuovo_inconsistenza(xi, conflitti):
    # Variabile che mi indica che è stata effettuata una modifica
    var = 0
    list = []

    if xi.variabile in conflitti[0][0]:
        for item in conflitti[0][0]:
            print(item[0])
            if len(item.valore) == 1:
                xi.valore.delete(item[0].valore)

    return []
    # if xi in conflitti[0][1]:
    #
    #
    #
    # for item in conflitti[0]:
    #     if item[1] == xi:
    #         #Aggiungo la regione confinante alla lista che dovrò restituire
    #         list.append(item[0])
    #         #Se il dominio della regione confinante ha un solo elemento, devo eliminare quell'elemento dal dominio del nodo in esame
    #         if len(item[0].valore) == 1:
    #             xi.valore.delete(item[0].valore)
    #             if len(xi.valore) != 0:
    #                 #Variabile che mi indica che è stata effettuata una modifica
    #                 var = 1
    #             else:
    #                 return False
    #
    # #Se var = 1 restituisco list piena, altrimenti vuota
    # if var == 1:
    #     return list
    # else:
    #     return []
    #
    #




    #Vado
# #Funzione per la rimozione dei valori inconsistenti
# def verifica_vincoli_AC3(variabile, confini, var):
#     #Se var è vuoto, prendo la prima variabile e il primo elemento del dominio e inserisco in var
#     if len(var) == 0:
#         var.append([variabile[0], variabile[1].pop()])
#         #Ritorno al backtracking
#         return True
#
#     #Se var non è vuoto
#     #Vado a controllare la variabile in esame con quali città confina
#     for item in confini:
#         #Se la variabile coincide con uno degli elementi della tupla presente in confini
#         if item[0] == variabile[0]:
#             #Controllo se lo stato confinante è presente in var
#             #Se lo è tolgo il colore assegnato allo stato confinante dalla lista dei colori disponibili
#             #item[1] contiene la nazione con cui confina la variabile in esame
#             #Se item[1] è contenuto in var
#             #Per tutti gli elementi presenti in var
#             for item2 in var:
#                 #controllo se sono uguali ad item[1]
#                 if item2[0] == item[1]:
#                     #Se il colore non è ancora stato rimosso, vado a rimuoverlo
#                     if item2[1] in variabile[1]:
#                         #Rimuovo valori inconsistenti
#                         variabile[1].remove(item2[1])
#
#         #Come per item[0] però al contrario
#         if item[1] == variabile[0]:
#             for item2 in var:
#                 if item2[0] == item[0]:
#                     if item2[1] in variabile[1]:
#                         # Rimuovo valori inconsistenti
#                         variabile[1].remove(item2[1])
#
#     #Se ci sono ancora colori a disposizione ne assegno uno, altrimeni restituisco False
#     if len(variabile[1]) == 0:
#         return False
#     else:
#         var.append([variabile[0], variabile[1].pop()])
#         return True
#
#
#
#
# def verifica_vincoli(variabile, confini, var):
#     print("Todo")
#
#
#
#
#
#
#
#
#
# #Funzione per verificare se l'obiettivo è stato raggiunto
# def verifica_obiettivo(variabili):
#     if len(variabili) == 0:
#         return True
#     else:
#         return False
#
# #Funzione per stampare la soluzione
# def stampa_soluzione(stato):
#     print(stato)