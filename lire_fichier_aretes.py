def fichier_aretes(fichier):
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
            if int(numero[2]) in liste:

                dic.update(
                    {int(numero[2]): {**(dic.get(int(numero[2]))), **{int(numero[1]): int(numero[3])}}})
            else:
                dic.update({int(numero[2]): {int(numero[1]): int(numero[3])}})

        else:
            dic.update({int(numero[1]): {int(numero[2]): int(numero[3])}})
            dic.update({int(numero[2]): {int(numero[1]): int(numero[3])}})

        if numero[1] not in liste:
            liste.append(int(numero[1]))
        if numero[2] not in liste:
            liste.append(int(numero[2]))

    return dic
