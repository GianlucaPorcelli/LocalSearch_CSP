from node import *
from copy import *

def assegna_var(variabili):
    #Restituisce una lista con la variabile, e il dominio
    return variabili.pop()


def verifica_vincoli(variabile, conflitti, valore, var_assegnate):
    print("var", variabile)
    print("valore", valore)
    print("--------------")

    #Controllo capienza
    contatore = 0
    for i in range(0, len(var_assegnate)):
        #Se il valore della variabile già assegnata è uguale al valore che sto considerando
        if var_assegnate[i][1] == valore:
            contatore += 1
    #Visto che non posso avere un valore maggiore di 6, se contatore è uguale a 6 restituisco False in quanto ha già
    #raggiunto dimensione massima
    if contatore == conflitti[4]:
        print("conflitto capienza")
        return False

    #Controllo che i surgelati appartengano tutti allo stesso container
    if variabile in conflitti[2]:
        for i in range(0, len(var_assegnate)):
            #Verifico che la variabile già assegnata che sto considerando appartenga ai surgelati
            if var_assegnate[i][0] in conflitti[2]:
                #Se ha valore diverso rispetto a quello che sto considerando, restituisco False, altrimenti passo a
                #considerare la variabile successiva presente in quelle già assegnate
                if var_assegnate[i][1] != valore:
                    print("conflitto surgelati")
                    return False

    #Controllo esplosivo
    if variabile in conflitti[1]:
        #Verifico che alla persona con cui ha litigato, non sia stato assegnato lo stesso tavolo
        for i in range(0, len(var_assegnate)):
            #Se la persona che sto controllando, appartiene alla lista, devo verificare che abbia un valore assegnato diverso
            if var_assegnate[i][0] in conflitti[1]:
                if var_assegnate[i][1] == valore:
                    print("conflitto esplosivo")
                    return False

    #Controllo che rifiuti non stanno con derrate
    if variabile in conflitti[0][0]:
        for j in range(0, len(var_assegnate)):
            if var_assegnate[j][0] in conflitti[0][1]:
                if var_assegnate[j][1] == valore:
                    print("conflitto rifiuti 1")
                    return False

    if variabile in conflitti[0][1]:
        for j in range(0, len(var_assegnate)):
            if var_assegnate[j][0] in conflitti[0][0]:
                if var_assegnate[j][1] == valore:
                    print("conflitto rifiuti2")
                    return False

    #Controllo che freschi e surgelati non stiano nello stesso container
    if variabile in conflitti[3][0]:
        for j in range(0, len(var_assegnate)):
            if var_assegnate[j][0] in conflitti[3][1]:
                if var_assegnate[j][1] == valore:
                    print("conflitto freschi sur 1")
                    return False

    if variabile in conflitti[3][1]:
        for j in range(0, len(var_assegnate)):
            if var_assegnate[j][0] in conflitti[3][0]:
                if var_assegnate[j][1] == valore:
                    print("conflitto freschi sur 2")
                    return False


    return True

# def forwarding(variabile, valore, conflitti, var_assegnare, num, aux):
#     delete = []
#     #print("Variabile che sto considerando: ", variabile, valore)
#     #Controllo tutte le tuple appartenenti alla lista delle famiglie che a sua volta è presente nella lista vincoli
#
#
#
#     for j in range(0, len(conflitti[0])):
#         # Se la variabile in esame è presente nella lista, significa che ho trovato la famiglia di appartenenza
#         if variabile in conflitti[0][j]:
#             # Elimino da tutte le altre variabili appartenenti alla stessa famiglia, tutti i valori eccetto quello che ho
#             # scelto per la variabile che sto considerando
#             for i in range(0, len(var_assegnare)):
#                 # Verifico che la variabile appartenga alla stessa famiglia
#                 if var_assegnare[i].variabile in conflitti[0][j]:
#                     # Elimino dal dominio
#                     for z in range(0, len(var_assegnare[i].valore)):
#                         #Diversifico in quanto nel caso abbia fatto backtracking devo aggiungere invece di eliminare
#                         if num == 1:
#                             if var_assegnare[i].valore[z] != valore:
#                                 #Aggiungo a rimossi l'elemento che sto eliminando
#                                 var_assegnare[i].rimossi.append(var_assegnare[i].valore[z])
#                                 delete.append(var_assegnare[i].valore[z])
#
#                         else:
#                             # print("shshakDSKJDHSDHoiAUHDOIABDHADBKBdAJHBDKJABDkajHBDHABDjkAHBDKHABDkHABDKHABDkjABDJK")
#                             # print(variabile)
#                             for k in range(0, len(var_assegnare[i].rimossi)):
#                                 if var_assegnare[i].rimossi[k] not in var_assegnare[i].valore:
#                                     var_assegnare[i].valore.append(var_assegnare[i].rimossi[k])
#
#                     for b in range(0, len(delete)):
#                         var_assegnare[i].valore.remove(delete[b])
#                     delete.clear()
#
#     # Verifico se compaio nella lista delle persone che hanno litigato
#     for j in range(0, len(conflitti[1])):
#         # Se la variabile è presente nella lista, significa che ha litigato con qualcuno e quindi devo verificare che non
#         # sia allo stesso tavolo
#         if variabile in conflitti[1][j]:
#             # Verifico che alla persona con cui ha litigato, non sia stato assegnato lo stesso tavolo
#             for i in range(0, len(var_assegnare)):
#                 # Se la persona che sto controllando, appartiene alla lista, devo verificare che abbia un valore assegnato diverso
#                 if var_assegnare[i].variabile in conflitti[1][j]:
#                     #Elimino dal dominio della variabile nella lista assegnare il valore che ho scelto per il nodo in esame
#                     if num == 1:
#                         if valore in var_assegnare[i].valore:
#                             var_assegnare[i].valore.remove(valore)
#                     else:
#                             if valore not in var_assegnare[i].valore:
#                                 var_assegnare[i].valore.append(valore)

# def coda(variabili, conflitti):
#     list1 = [] #Prima famiglia
#     list2 = [] #Seconda famiglia
#     list3 = [] #Persone che non parlano
#     list4 = []
#
#     #Creo coppie di nodi per le liste famiglia
#     for i in range(0, len(variabili)-1):
#         for j in range(i+1, len(variabili)):
#             #Verifico se i due nodi appartengono alla stessa famiglia e nel caso li memorizzo nella lista corrispondente
#             if variabili[i].variabile in conflitti[0][0] and variabili[j].variabile in conflitti[0][0]:
#                 list1.append([variabili[i], variabili[j]])
#             if variabili[i].variabile in conflitti[0][1] and variabili[j].variabile in conflitti[0][1]:
#                 list2.append([variabili[i], variabili[j]])
#
#     #Creo coppie di nodi per quelli che hanno litigatp
#     for i in range(0, len(variabili)-1):
#         for j in range(i+1, len(variabili)):
#             for k in range(0, len(conflitti[1])):
#                 if variabili[i].variabile in conflitti[1][k] and variabili[j].variabile in conflitti[1][k]:
#                     list3.append([variabili[i], variabili[j]])
#     list4.append(list1)
#     list4.append(list2)
#     list4.append(list3)
#     return list4
#
#
# def AC3(variabili, conflitti):
#     aux = coda(variabili, conflitti)
#     controllare = []
#     controllati = []
#
#     for i in range(0, len(aux)):
#         aux_temp = aux[i]
#         for item in aux_temp:
#             controllare.append(item)
#
#     while len(controllare) != 0:
#         #Prendo la prima coppia
#         x = controllare.pop()
#         #Li aggiungo a controllati
#         controllati.append(x)
#
#         #Verifico inconsistenza con i vicini
#         contr = rimuovo_inconsistenza(x, conflitti)
#         if contr == True:
#             #Se è stato effettuato un cambio devo reinserire i nodi vicini nella lista da controllare
#             for item in controllati:
#                 print("item", item)
#                 print("controllati", controllati)
#         else:
#             #Restituisco False se non ho consistenza
#             return False
#
#     #Restituisco True se ho consistenza
#     return True
#
# def rimuovo_inconsistenza(xi, conflitti):
#     # Variabile che mi indica che è stata effettuata una modifica
#     print(xi[0].variabile)
#     #Verifico se devo gestire il dominio in base al fatto che appartengano alla stessa famiglia
#     if (xi[0].variabile in conflitti[0][0] and xi[1].variabile in conflitti[0][0]) or (xi[0].variabile in conflitti[0][1] and xi[1].variabile in conflitti[0][1]):
#         #Per ogni elemento del dominio di xi
#         for item in xi[0].valore:
#             buono = False
#             #PConfronto con tutti gli elementi del dominio di xj
#             for item2 in xi[1].valore:
#                 if item == item2:
#                     buono = True
#                     break
#             #Se non ho trovato il valore nel dominio del nodo xj, lo vado a rimuovere dal dominio del nodo xi
#             if buono == False:
#                 xi[0].valore.delete(item)
#                 #Restituisco vero perchè devo inserire tutti i nodi legati al nodo che ho modificato
#                 return True
#
#     #Verifico se devo gestire il dominio in base al fatto che non si parlano tra di loro
#     if (xi[0].variabile in conflitti[1][0] and xi[1].variabile in conflitti[1][0]) or (xi[0].variabile in conflitti[1][1] and xi[1].variabile in conflitti[1][1]) or(xi[0].variabile in conflitti[1][2] and xi[1].variabile in conflitti[1][2]):
#         # Per ogni elemento del dominio di xi
#         #Se xj ha un solo valore all'interno del proprio dominio
#         if len(xi[1].valore) == 1:
#             for item in xi[0].valore:
#                 if item == xi[1].valore:
#                     xi[0].valore.delete(item)
#                     # Restituisco vero perchè devo inserire tutti i nodi legati al nodo che ho modificato
#                     return True
#
#     return False



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
