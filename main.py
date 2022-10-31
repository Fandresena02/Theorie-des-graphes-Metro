import lire_fichier_aretes
import lire_fichier_sommets

fichier_aretes = open("aretes.txt", "r")
fichier_sommets = open("sommets.txt", 'r')

stations=lire_fichier_sommets.fichier_sommets(fichier_sommets)

voisins_sommets=lire_fichier_aretes.fichier_aretes(fichier_aretes)
voisins_sommets_keys = sorted(voisins_sommets.keys())

voisins_sommets_tries = {}
for key in voisins_sommets_keys:
    voisins_sommets_tries[key] = voisins_sommets[key]


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
        durees_min[sommet]=None
        peres[sommet]=None
    
    
    #definition du numéro de départ
    for station in stations:
        if station['nom_sommet']==depart: num_dep=station['numero_sommet']    
    
    # boucle jusqu'à trouver la station
    station_courante=[num_dep,0]
    durees_min[num_dep]=station_courante[1]
    chemin=[]
    
    while len(chemin)<len(stations):
        chemin.append(station_courante);
        for sommet in voisins_sommets_tries:
            
            if sommet==station_courante[0]:
                for voisin in list(voisins_sommets_tries.values())[sommet]:
                    addition_durees=durees_min[sommet]+list(voisins_sommets_tries.values())[sommet][voisin]
                    
                    if (is_station_in_chemin(chemin, voisin)==0) or \
                        (durees_min[voisin]==None) or \
                        (addition_durees < durees_min[voisin]):
                        
                        if durees_min[voisin]==None: stations_vues.append(voisin)
                    
                        durees_min[voisin]=addition_durees
                        
                        peres[voisin]=sommet
                        
        station_courante=station_duree_min(durees_min, stations_vues, chemin)
           
    return durees_min, peres

def get_station(num_station):
    for station in stations:
        if station['numero_sommet']==num_station: 
            return station
    return None

def get_station_de_ligne(nom_station, ligne):
    for station in stations:
        #print(station['ligne'], station['ligne']==ligne)
        if station['nom_sommet']==nom_station and station['ligne']==ligne: 
            return station
    return None

def get_ligne_lien(station1, station2):
    stations1=[]
    stations2=[]
    
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
        
def get_direction(station1, station2, ligne):
    
    stationPrecedente = get_station_de_ligne(station1['nom_sommet'], ligne)
    
    station = get_station_de_ligne(station2['nom_sommet'], ligne)
    
    while station['terminus'].strip()=='False':
        
        for voisin in list(voisins_sommets_tries.values())[station['numero_sommet']]:
            station_voisine = get_station(voisin)
                
            # pour etre dans le bon sens
            if (station_voisine['nom_sommet']!=stationPrecedente['nom_sommet']) and \
            (station_voisine['ligne']==ligne):
                                
                stationPrecedente = station
                station = station_voisine
                break
    

    return station['nom_sommet']       
          
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
    station_precedente=None
    
    # pendant
    while station['numero_sommet'] != num_dep:
        if not((station_precedente!=None) and (station['nom_sommet']==station_precedente['nom_sommet'])):
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
    changement = False
    
    for station in reversed(itineraire):

        #depart
        if station['numero_sommet']==num_dep: 
            print('Vous êtes à', station['nom_sommet'])
        
        # détermination de la ligne
        elif station_precedente['numero_sommet']==num_dep: 
            ligne = get_ligne_lien(station_precedente, station)
            print('Prenez la ligne', ligne, 'en direction de', get_direction(station_precedente, station, ligne))
        
        #indication de changement de ligne   
        if changement :
            ligne = get_ligne_lien(station_precedente, station)
            print('A', station_precedente['nom_sommet'], 'changez et prenez la ligne', station_precedente['ligne'], 'en direction de', get_direction(station_precedente, station, ligne))
            changement = False
        
        # reperage de changement de ligne
        if station['numero_sommet']!=num_dep and station_precedente['ligne']!=station['ligne'] and station['numero_sommet']!=num_arr:
            changement = True
        
        #arrivee
        if station['numero_sommet']==num_arr: 
            print('Vous devriez arriver à', station['nom_sommet'], 'dans environ', round((durees_min[station['numero_sommet']]/60),2), 'minutes')
        
        station_precedente=station

if __name__ == '__main__':
    fichier_aretes.close()
    fichier_sommets.close()
