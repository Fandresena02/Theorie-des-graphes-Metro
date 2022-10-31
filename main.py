#!/usr/bin/env python3
import parcours
import lire_fichier_aretes
import lire_fichier_sommets
from connexe import *
from kruskal import *


def recup_nom_station(fichier):
    matrice = lire_fichier_sommets.fichier_sommets(fichier)
    nombre_sommets = len(matrice)
    lst_sommet = []
    for i in range(nombre_sommets):
        if (matrice[i]["nom_sommet"] not in lst_sommet):
            lst_sommet.append(matrice[i]["nom_sommet"])
    return lst_sommet


if __name__ == '__main__':

    while (True):

        fichier_aretes = open("aretes.txt", "r")
        fichier_sommets = open("sommets.txt", 'r')
        choix_possible = [1, 2, 3, 4]
        choix = int(input(
            "Bienvenue dans Metro-Boulo-Dodo.Le menu :\n1-Chemin\n2-Connexe\n3-ACPM\n4-Quitter\nVotre choix: "))
        while (choix not in choix_possible):
            choix = int(input(
                "CHOIX INVALIDE\nEntrez votre choix:\n1-Chemin\n2-Connexe\n3-ACPM\n4-Quitter\nVotre choix: "))

        if (choix == 1):
            liste_nom_station = recup_nom_station(fichier_sommets)
            depart = input("Indiquez la station de départ : ")
            while (depart not in liste_nom_station):
                depart = input("Indiquez la station de départ : ")
            arrivee = input("Indiquez la station d'arrivée : ")
            while (arrivee not in liste_nom_station):
                arrivee = input("Indiquez la station de arrivée : ")

            durees_min, peres = parcours.algo_durees_min(depart)

            parcours.parcours_chemin(durees_min, peres, depart, arrivee)
        elif (choix == 2):
            print(connexe(fichier_sommets, fichier_aretes))
        elif (choix == 3):
            Compiler(fichier_aretes, fichier_sommets)
        elif (choix == 4):
            break
        choix = 0
        fichier_aretes.close()
        fichier_sommets.close()
