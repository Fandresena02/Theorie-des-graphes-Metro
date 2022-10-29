

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
def runKruskalAlgorithm(edges, n):
 
    # stocke les arêtes présentes dans pcm
    pcm = []
 
    # Initialise la classe `DisjointSet`.
    # Créer un ensemble singleton pour chaque élément de l'univers.
    ds = DisjointSet()
    ds.makeSet(n)
 
    index = 0
 
    # trier les arêtes par poids croissant
    edges.sort(key=lambda x: x[2])
 
    # pcm contient exactement les arêtes `V-1`
    while len(pcm) != n - 1:
 
        # considère le bord suivant avec un poids minimum du graph
        (src, dest, weight) = edges[index]
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

 
# (u, v, w) triplet représente le bord non orienté de
# sommet `u` au sommet `v` de poids `w`
edges = [
    (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
    (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
]

# nombre total de nœuds dans le graphe (étiquetés de 0 à 6)
n = 7

# graphe de construction
e = runKruskalAlgorithm(edges, n)

print(e)


