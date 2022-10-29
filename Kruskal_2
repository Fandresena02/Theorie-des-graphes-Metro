# Une classe pour représenter un ensemble disjoint
class DisjointSet:
    parent = {}
 
    # effectue l'opération MakeSet
    def makeSet(self, n):
        # créer `n` ensembles disjoints (un pour chaque sommet)
        for i in range(n):
            self.parent[i] = i
 
    # Trouver la racine de l'ensemble auquel appartient l'élément `k`
    def find(self, k):
        # si `k` est racine
        if self.parent[k] == k:
            return k
 
        # se reproduisent pour le parent jusqu'à ce que nous trouvions la racine
        return self.find(self.parent[k])
 
    # Perform Union de deux sous-ensembles
    def union(self, a, b):
        # trouver la racine des ensembles auxquels appartiennent les éléments `x` et `y`
        x = self.find(a)
        y = self.find(b)
 
        self.parent[x] = y
 
 
# Fonction pour construire pcm en utilisant l'algorithme de Kruskal
def kruskal(sommets, n):
 
    # stocke les arêtes présentes dans pcm
    pcm = []
 
    # Initialise la classe `DisjointSet`.
    # Créer un ensemble singleton pour chaque élément de l'univers.
    ds = DisjointSet()
    ds.makeSet(n)
 
    index = 0
 
    # trier les arêtes par poids croissant
    sommets.sort(key=lambda x: x[2])
 
    # pcm contient exactement les arêtes `V-1`
    while len(pcm) != n - 1:
 
        # considère le bord suivant avec un poids minimum du graph
        (src, dest, weight) = sommets[index]
        index = index + 1
 
        # trouver la racine des ensembles auxquels deux extrémités
        # sommets de l'arête suivante appartiennent
        x = ds.find(src)
        y = ds.find(dest)
 
        # si les deux points de terminaison ont des parents différents, ils appartiennent à
        # différents composants connectés et peuvent être inclus dans pcm
        if x != y:
            pcm.append((src, dest, weight))
            ds.union(x, y)
 
    return pcm

fichier_aretes = open("aretes.txt", "r")
fichier_sommets = open("sommets.txt", 'r')

def lire_fichier_aretes(fichier):
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

def lire_fichier_sommets(nom_fichier):
    lst_f = []
    # with open(nom_fichier, "r") as filin :
    for ligne in nom_fichier:
        lst = ligne.split(";")
        dico = {"numero_sommet" : int(lst[1]), "nom_sommet" : lst[2].strip(), "ligne" : lst[3].strip(), "terminus" : lst[4].strip(), "branchement" : int(lst[5])}
        lst_f.append(dico)
    return lst_f

def getLiaisons():
    liaisons = []
    
    #initialisation du tableau liaisons contenant des éléments de format (sommet1, sommet2, temps)
    for sommet in voisins_sommets_tries:
        for voisin in list(voisins_sommets_tries.values())[sommet]:
            liaisons.append((sommet,voisin,list(voisins_sommets_tries.values())[sommet][voisin]))
    return liaisons 
    

stations=lire_fichier_sommets(fichier_sommets)

voisins_sommets=lire_fichier_aretes(fichier_aretes)
voisins_sommets_keys = sorted(voisins_sommets.keys())

voisins_sommets_tries = {}
for key in voisins_sommets_keys:
    voisins_sommets_tries[key] = voisins_sommets[key]
    
sommets = getLiaisons()

# nombre total de sommets dans le graphe
n = len(voisins_sommets)

# graphe de construction
graphe_kruskal = kruskal(sommets, n)

print(graphe_kruskal)

fichier_aretes.close()
fichier_sommets.close()
