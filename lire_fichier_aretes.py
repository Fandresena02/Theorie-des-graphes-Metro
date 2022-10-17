fichier = open("aretes.txt", "r")


def fichier_arete(fichier):
    dic = {}
    liste = []
    lignes = fichier.readlines()

    for ligne in lignes:

        numero = ligne.split()

        if (liste):
            if int(numero[1]) in liste:

                dic.update(
                    {int(numero[1]): {**(dic.get(int(numero[1]))), **{int(numero[2]): int(numero[3])}}})
            else:
                dic.update({int(numero[1]): {int(numero[2]): int(numero[3])}})

        else:
            dic.update({int(numero[1]): {int(numero[2]): int(numero[3])}})

        if numero[1] not in liste:
            liste.append(int(numero[1]))

    return dic


for cle, valeur in fichier_arete(fichier).items():
    print("L'élément de clé", cle, "vaut", valeur)
fichier.close()
