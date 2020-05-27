# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:47:17 2020

@author: Matthias
"""

# Magik : True
# 
# TODO : V3 afficher les sommes des diagonales
# TODO : V4 + verification somme diagonale
# TODO : V5 verifier qu'on utilise tous les nombres de 1 à n**2 sans répétition
def displayMagicSquare(square):
    """display the square with all its sums and its magic character"""
    n = len(square)
    sommeMagique = n*(n**2+1)//2
    magik = True
    # V0 : afficher les valeurs uniquement en mode carré
    for i in range(n):
        for j in range(n):
            print("{:>3}".format(square[i][j]), end=' ')
        # V1 : afficher les sommes de lignes 
        sommeLigne = sum(square[i])
        if (sommeLigne != sommeMagique):
            magik = False
        print(f" : {sommeLigne:>3}")
    # V2 : afficher les sommes des colonnes
    for j in range(n):
        sommeColonne = sum(square[i][j] for i in range(n))
        if sommeColonne != sommeMagique:
            magik = False
        print(f"{sommeColonne:>3}", end=' ')
    # V4 : afficher le caractère magique du carré
    print()
    print("Magik:", magik)
    
# algorithme valable en taille impaire
def makeMagikSquare(n):
    square = [[0]*n for _ in range(n)]
    row = 0
    column = n // 2
    square[row][column] = 1
    # placer les nombres de 2 à n**2
    for v in range(2, n**2+1):
        # calculer nouvelles positions
        row2 = (row + 2) % n
        column2 = (column + 1) % n
        # verifier si la case est occupée et corriger le déplacement
        if square[row2][column2] != 0:
            row = (row + 1) % n
        else:
            row, column = row2, column2
        # placer la nouvelle valeur
        square[row][column] = v
    return square

c3 = makeMagikSquare(3)
c5 = makeMagikSquare(5)

displayMagicSquare(c3)
displayMagicSquare(c5)






















