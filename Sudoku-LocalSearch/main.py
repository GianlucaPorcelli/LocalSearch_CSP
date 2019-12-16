from algorithms import *
from node import*
from HillClimbing import *
import random
# ---------------------------------------------------------Parameters--------------------------------------------------------------


root=inizio()
stampa(root.tabella)

# ---------------------------------------------------------HillClimbing--------------------------------------------------------------

path=HillClimbing(root)
if path!=None:
    print("\nSoluzione sudoku TROVATA:\n")
    stampa(path.tabella)

    print("\nSudoku da risolvere:\n")
    tag=taglia(path)
    stampa(tag.tabella)
    #print(path.tabella)
# ------------------------------------------------------------------------------------------------------------------------------

#stampa(root)
