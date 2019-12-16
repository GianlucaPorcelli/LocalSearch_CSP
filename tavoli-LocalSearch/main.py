#from algorithms import *
from node import*
from HillClimbing import *
from KNode import*

# ---------------------------------------------------------Parameters--------------------------------------------------------------
N=3 #numero tavoli
capienza=6
all=['Antonella','Domenico', 'Raffella', 'Tommaso', 'Vincenzo', 'Azzurra', 'Cristiano', 'Francesca', 'Luigi', 'Giovanni','Marcella', 'Daniela', 'Nunzio', 'Leonardo', 'Silvia']
famiglia1=['Antonella', 'Domenico', 'Raffella', 'Tommaso', 'Vincenzo']
famiglia2=['Azzurra', 'Cristiano', 'Francesca', 'Luigi']
litigi=[['Giovanni','Marcella'],['Marcella','Daniela'],['Luigi','Leonardo']]

# all=['Antonella','Domenico', 'Raffella', 'Tommaso', 'Vincenzo', 'Azzurra', 'Cristiano', 'Francesca', 'Luigi', 'Giovanni','Marcella', 'Daniela','NIC0']
# litigi=[]
# all.remove("Marcella")
# for i in range (0,len(all)):
#     litigi.append(['Marcella',all[i]])
# #print (litigi)
# all.append("Marcella")

# # ---------------------------------------------------------------------------------------------------------------------------------
#
# #-----------------------------------------------------------HillClimbing-----------------------------------------------------------
while True:
    state=initial(N,capienza,all)   #genero casualmente uno stato iniziale
    root=Node(state,litigi,famiglia1,famiglia2,all)
    print("Lo stato CASUALE iniziale è il seguente: \n",root.state[:N],"\nEuristica: ",root.heuristic,"\n")
    path=HillClimbing(root,litigi,famiglia1,famiglia2,all)
    if path!=None:
        print("Soluzione algoritmo Hill climbing:\n",path.state[:N],"\nEuristica: ",path.heuristic)
        break

# # ---------------------------------------------------------------------------------------------------------------------------------
#
#
#
# #----------------------------------------------------------LocalBeamSearch---------------------------------------------------------
# state=initial(N,capienza,all)   #genero casualmente uno stato iniziale
# root=Node(state,litigi,famiglia1,famiglia2,all)
# LocalBeamSearchPROVA(root,litigi,capienza,6,famiglia1,famiglia2,all)

#--------------------------------------------------------------------------------------------------------------------------------------
path=root
#il numero di nodi da espandere deve essere almeno pari a 3
path=LocalBeamSearch(path,litigi,capienza,10,famiglia1,famiglia2,all)
if path!=None:
    print("\nAssegnazione finale Local Beam Search: \n",path.state[:N])                           #stampo la disposizione dei tavoli trovata
    print("Euristica: ",path.heuristic)
else:
    print("Soluzione non trovata")

#
#----------------------------------------------------------------------------------------------------------------------------------

# #--------------------------------------------------------SimulatedAnnealing--------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------------------------------