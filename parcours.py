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
        dico = {"numero_sommet" : int(lst[1]), "nom_sommet" : lst[2].strip(), "ligne" : lst[3].strip(), "terminus" : lst[4], "branchement" : int(lst[5])}
        lst_f.append(dico)
    return lst_f

stations=lire_fichier_sommets(fichier_sommets)

voisins_sommets=lire_fichier_aretes(fichier_aretes)
voisins_sommets_keys = sorted(voisins_sommets.keys())

voisins_sommets_tries = {}
for key in voisins_sommets_keys:
    voisins_sommets_tries[key] = voisins_sommets[key]

#print(voisins_sommets_tries)

def is_station_in_chemin(chemin, num_station):
    for station in chemin:
        if station[0]==num_station: return 1;
    return 0;


def station_duree_min(durees_min, stations_vues, chemin):
    station_duree_min=None

    for num_station in stations_vues:
        
        # si la station n'a pas déjà été traitée
        if is_station_in_chemin(chemin, num_station)==0:
            
            if station_duree_min == None or durees_min[num_station] < station_duree_min[1]: 
                station_duree_min=[num_station, durees_min[num_station]]
            
    return station_duree_min

def algo_durees_min(depart):
    
    stations_vues=[]
    peres=dict()
    durees_min= dict()
    num_dep=0

    #initialisation du tableau de distances_min
    for sommet in voisins_sommets_tries:
        #print(list(voisins_sommets_tries.values())[station-1])
        #print(sommet)
        durees_min[sommet]=None
        peres[sommet]=None
    
    
    #definition du numéro de départ
    for station in stations:
        #print(station['nom_sommet'])
        if station['nom_sommet']==depart: num_dep=station['numero_sommet']    
    
    #print(num_dep)
    # boucle jusqu'à trouver la station
    station_courante=[num_dep,0]
    durees_min[num_dep]=station_courante[1]
    chemin=[]
    
    while len(chemin)<len(stations):
        chemin.append(station_courante);
        for sommet in voisins_sommets_tries:
            
            if sommet==station_courante[0]:
                #print(list(voisins_sommets_tries.values())[sommet])
                for voisin in list(voisins_sommets_tries.values())[sommet]:
                    #print(voisin)
                    addition_durees=durees_min[sommet]+list(voisins_sommets_tries.values())[sommet][voisin]
                    
                    if (is_station_in_chemin(chemin, voisin)==0) or \
                        (durees_min[voisin]==None) or \
                        (addition_durees < durees_min[voisin]):
                        
                        #print(get_station(sommet)['nom_sommet'],'===>',get_station(voisin)['nom_sommet'])
                        #if(durees_min[voisin]==None): 
                        #    print('durees_min[', voisin,'] == none')
                        #elif(addition_durees < durees_min[voisin]): 
                        #    #print(addition_durees, '<', durees_min[voisin],'==',(addition_durees < durees_min[voisin]))
                        
                        #print(voisin)
                        if durees_min[voisin]==None: stations_vues.append(voisin)
                    
                        durees_min[voisin]=addition_durees
                        #print('durees_min[', voisin,'] ==', durees_min[voisin], '\n')
                        
                        peres[voisin]=sommet
                        
        station_courante=station_duree_min(durees_min, stations_vues, chemin)
           
    return durees_min, peres

def get_station(num_station):
    for station in stations:
        if station['numero_sommet']==num_station: 
            return station
    return None

def get_ligne_lien(station1, station2):
    stations1=[]
    stations2=[]
    #print(station1)
    #print(station2)
    # implémentation des tableaux
    for station in stations:
        if station['nom_sommet']==station1['nom_sommet']: stations1.append(station)
        if station['nom_sommet']==station2['nom_sommet']: stations2.append(station)
    
    # recherche de la ligne commune
    for station1 in stations1:
        for station2 in stations2:
            if station1['ligne']==station2['ligne']:
                return station1['ligne']
        
    return None    
        
def parcours_chemin(durees_min, peres, depart, arrivee):
    
    # définition des numéros de départ et d'arrivée
    for station in stations:
        if station['nom_sommet']==depart: num_dep=station['numero_sommet']
        if station['nom_sommet']==arrivee: num_arr=station['numero_sommet'] 
            
    # parcours du chemin à l'envers (par le bas)
    itineraire=[]
    
    # remplissage du tableau itinéraire
    # fin
    station=get_station(num_arr)
    
    # pendant
    while station['numero_sommet'] != num_dep:
        itineraire.append(station)
        num_station=peres[station['numero_sommet']]
        
        station_precedente=station
        station=get_station(num_station)
        
    # début
    station=get_station(num_dep)
    itineraire.append(station)
    
    # affichage de l'itinéraire
    station=get_station(num_dep)
    station_precedente=station
    
    for station in reversed(itineraire):
        #depart
        if station['numero_sommet']==num_dep: 
            print('Vous êtes à', station['nom_sommet'])
        
        # détermination de la ligne
        elif station_precedente['numero_sommet']==num_dep: 
            print('Prenez la ligne', get_ligne_lien(station_precedente, station))
        
        #indication de changement de ligne   
        if station['numero_sommet']!=num_dep and station_precedente['ligne']!=station['ligne'] and station['numero_sommet']!=num_arr:
            print('A', station['nom_sommet'], 'changez et prenez la ligne ', station['ligne'])
        
        #arrivee
        if station['numero_sommet']==num_arr: 
            print('Vous devriez arriver à', station['nom_sommet'], 'dans environ', round((durees_min[station['numero_sommet']]/60),2), 'minutes')
        
        station_precedente=station

depart='Carrefour Pleyel'
arrivee='Rue Montmartre, Grands Boulevards'

durees_min,peres=algo_durees_min(depart)

parcours_chemin(durees_min, peres, depart, arrivee)

#print('\nPPC:')
#for station in durees_min:
#    print(get_station(peres[station])['nom_sommet'], '->', get_station(station)['nom_sommet'], '\t tps:', durees_min[station]/60, 'min')

fichier_aretes.close()
fichier_sommets.close()
