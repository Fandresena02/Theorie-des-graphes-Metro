import operator

fichier_sommets= open("sommets.txt", "r")
fichier_aretes = open("aretes.txt", "r")

class UnionFind : 
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
 
 
    def union(self, parent, rang, x, y):
        if rang[x] < rang[y]:
            parent[x] = y

        elif rang[x] > rang[y]:
            parent[y] = x
 
        else:
            parent[y] = x
            rang[x] += 1

class Graphe :

    def __init__(self, aretes):
        self.V = aretes  
        self.Graphe = []

    def ajouter_arete(self, u, v, p):
        self.Graphe.append([u, v, p])

    def kruskal(self):

        un = UnionFind()
        resultat = []
        i = 0
        index_in_resultat = 0

        self.Graphe = sorted(self.Graphe, key=lambda x: x[2])
        parent = []
        rang = []
 
        for sommet in range(self.V):
            parent.append(sommet)
            rang.append(0)
 
        while index_in_resultat < self.V - 1:
            u, v, w = self.Graphe[i]
            i = i + 1

            x = un.find(parent, u)
            y = un.find(parent, v)

            if x != y:
                index_in_resultat = index_in_resultat + 1
                resultat.append([u, v, w])
                un.union(parent, rang, x, y)

        poids_totale_apcm = 0

        for u, v, poids in resultat:
            poids_totale_apcm += poids

        print("\nLe poids du plus court chemin est de ", poids_totale_apcm)
        print("\n\nOn obtient un resultat : \n", resultat)



def fichier_arete_list_triee_par_duree(fichier):
    liste = []
    liste_triee = []
    lignes = fichier.readlines()

    for ligne in lignes:
        numero = ligne.split()
        numero[1]= int(numero[1])
        numero[2]= int(numero[2])
        numero[3]= int(numero[3])
        liste.append(numero)
        
    liste_triee = sorted(liste, key=operator.itemgetter(3))

    return liste_triee


if __name__ == '__main__':
    
    liste_triee = fichier_arete_list_triee_par_duree(fichier_aretes)

    nb_sommets = 0
    for ligne in fichier_sommets:
        nb_sommets+=1

    g2 = Graphe(nb_sommets)
    
    for element in liste_triee:
        g2.ajouter_arete(element[1],element[2],element[3])

    g2.kruskal()
