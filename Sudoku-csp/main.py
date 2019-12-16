from algorithms import *
from node import*
from HillClimbing import *
import random
# ---------------------------------------------------------Parameters--------------------------------------------------------------


root=inizio()

# ---------------------------------------------------------HillClimbing--------------------------------------------------------------

path=HillClimbing(root)
if path!=None:
    print("\nSoluzione sudoku TROVATA:\n")
    for i in range(0, 81):
        print("|", path.tabella[i], "|", end='')
        if (i + 1) % 9 == 0:
            print(" ")

    print("\nSudoku da risolvere:\n")
    tag=taglia(path)
    for i in range(0, 81):
        print("|", tag.tabella[i], "|", end='')
        if (i + 1) % 9 == 0:
            print(" ")
# ------------------------------------------------------------------------------------------------------------------------------

#stampa(root)
