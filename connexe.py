import lire_fichier_sommets
import lire_fichier_aretes


def exist_chemin(matrice, nombre_sommets, u, v):
    #nombre_sommets = len(lire_fichier_sommets.fichier_sommet(fichier))
    # matrice = lire_fichier_aretes.fichier_arete(fichier1)
    file = []
    visites = [False] * nombre_sommets
    file.append(u)
    while(file):
        actuel = file.pop(0)
        visites[actuel] = True
        for i in range(nombre_sommets):
            if matrice.get(actuel, {}).get(i) and visites[i] == False:
                file.append(i)
                visites[i] = True
                if i == v:
                    return True
            elif matrice.get(actuel, {}).get(i) and (i == v):
                return True
    return False


def connexe(fichier, fichier1):
    nombre_sommets = len(lire_fichier_sommets.fichier_sommets(fichier))
    matrice = lire_fichier_aretes.fichier_aretes(fichier1)
    for i in range(nombre_sommets):
        for j in range(i+1, nombre_sommets):
            if i != j:
                # print(exist_chemin(matrice, nombre_sommets, i, j), i, j)
                if exist_chemin(matrice, nombre_sommets, i, j) == False:
                    return False
    return True

#TESTS
fichier = open("sommets.txt", 'r')
fichier1 = open("aretes.txt", 'r')
print(connexe(fichier, fichier1))
fichier.close()
fichier1.close()
