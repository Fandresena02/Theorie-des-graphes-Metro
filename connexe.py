import lire_fichier_sommets
import lire_fichier_aretes


def chemin_existe(matrice, nombre_sommets, u, v):
    #nombre_sommets = len(lire_fichier_sommets.fichier_sommet(fichier))
    # matrice = lire_fichier_aretes.fichier_arete(fichier1)
    file = []
    sommets_visites = [False] * nombre_sommets
    file.append(u)
    while(file):
        actuel = file.pop(0)
        sommets_visites[actuel] = True
        for i in range(nombre_sommets):
            if matrice.get(actuel, {}).get(i) and sommets_visites[i] == False:
                file.append(i)
                sommets_visites[i] = True
                if i == v:
                    return True
            elif matrice.get(actuel, {}).get(i) and (i == v):
                return True
    return False


def connexe(fichier, fichier1):
    nombre_sommets = len(lire_fichier_sommets.fichier_sommet(fichier))
    matrice = lire_fichier_aretes.fichier_arete(fichier1)
    for i in range(nombre_sommets):
        for j in range(i+1, nombre_sommets):
            if i != j:
                # print(chemin_existe(matrice, nombre_sommets, i, j), i, j)
                if chemin_existe(matrice, nombre_sommets, i, j) == False:
                    return False
    return True


fichier = open("sommets.txt", 'r')
fichier1 = open("aretes.txt", 'r')
print(connexe(fichier, fichier1))
# print(chemin_existe(lire_fichier_aretes.fichier_arete(fichier1),
#       len(lire_fichier_sommets.fichier_sommet(fichier)), 1, 364))
fichier.close()
fichier1.close()
