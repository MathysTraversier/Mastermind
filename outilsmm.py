# -*- coding: utf-8 -*-

from math import *

from random import random,randint


#Fonctions obligatoires#

def affiche(jeu):
    print(18*'-')
    for i in range(0,len(jeu)):
        C=[]
        for k in jeu[i][0]:
            C.append(k)
        print("{} : {} {} {} {} @{} #{}".format(i+1,C[0],C[1],C[2],C[3],jeu[i][1],jeu[i][2]))
    print(18*'-')

def tirage():
    a = str(randint(1,8))
    b = str(randint(1,8))
    c = str(randint(1,8))
    d = str(randint(1,8))
    solution = a+b+c+d
    return solution

def valide(combinaison):
    for i in combinaison:
        if i!="1" and i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8":
            return 'Faux'
    if len(combinaison)!=4:
        return "Faux"
    else:
        return "Vrai"

def essai():
    combinaison=input('Essai: ')
    if valide(combinaison)=="Vrai":
        return combinaison
    else:
        return '****'

def bienplace(combinaison,solution):
    Bcompteur=0
    for j in range(0,4):
        if solution[j]==combinaison[j]:
            Bcompteur=Bcompteur+1
    return Bcompteur

def malplace(combinaison,solution):
    Mcompteur=0
    P=commun(combinaison,solution)
    for l in P:
        B=0
        for m in range(0,4):
            if combinaison[m]==solution[m] and l==combinaison[m]:
                B=B+1
        cc=combinaison.count(l)
        cs=solution.count(l)
        Mcompteur=Mcompteur+(min(cc,cs)-B)
    return Mcompteur
    
def ajout(combinaison,solution,jeu):
    Bcompteur=bienplace(combinaison,solution)
    Mcompteur=malplace(combinaison,solution)
    jeu.append([combinaison,Bcompteur,Mcompteur])
    return None

def victoire(combinaison,solution):
    if combinaison==solution:
        return "Vrai"
    else:
        return "Faux"
    
    
#Fonctions facultatives#
        
#Permet de tirer de deux listes leurs éléments communs en un seul exemplaire#
def commun(L1,L2):
    L3=[]
    k=0
    for element in L1:
        if element in L2:
            L3.append(element)
    L3.sort()
    while k<=len(L3)-2:
        if L3[k]==L3[k+1]:
            L3.remove(L3[k])
        k=k+1
    return L3

def validepartie(partie):
    partie=partie.lower()
    while partie!='oui' and partie!='non':
        partie=input("Je n'ai pas compris, voulez-vous rejouer ? ")
        partie=partie.lower()
    return partie