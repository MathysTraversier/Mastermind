# -*- coding: utf-8 -*-

import outilsmm as mm
from outilsmm import *

print(17*"=")
print("Mastermind")
print("by Cece et Mathys")
print(17*"=")
print("Vous disposerez de 10 essais pour deviner la combinaison de 4 pions")
print("Les pions peuvent être de 8 couleurs : 1,2,3,4,5,6,7,8")
print(17*"=")

partie='oui'
while partie=='oui':
    solution=mm.tirage()
    compteur=1
    jeu=[]
    combinaison="0"

    while compteur<=10 and combinaison!=solution:
        combinaison=mm.essai()
        if combinaison=='****':
            print("Combinaison incorrecte, vous avez perdu un essai pour rien !")
        mm.ajout(combinaison,solution,jeu)
        mm.affiche(jeu)
        if mm.victoire(combinaison,solution)=="Vrai":
            print("C'est gagné en {} essais ! Bravo !".format(compteur))
        else:
            compteur=compteur+1
        
    if compteur>10:
        print("C'est perdu ! :(")
        print("La solution était {}".format(solution))
    
    partie=input("Voulez-vous rejouer ? Répondre par OUI ou par NON : ")
    if validepartie(partie)=='oui':
        print('Très bien, je relance une partie.')
        partie='oui'
    else:
        print("D'accord, très bien... Au plaisir de vous revoir pour une nouvelle partie !")