def fichier_sommets(nom_fichier):
    lst_f = []
    # with open(nom_fichier, "r") as filin :
    for ligne in nom_fichier:
        lst = ligne.split(";")
        dico = {"numero_sommet" : int(lst[1]), "nom_sommet" : lst[2].strip(), "ligne" : lst[3].strip(), "terminus" : lst[4].strip(), "branchement" : int(lst[5])}
        lst_f.append(dico)
    return lst_f
