from math import sqrt   # import de la fonction racine carree
#Exo 1:
def recherche(tab, n):
    """
    recherche n dans tab et retour l'indice de sa dernière occurence ou la longueur de la liste
    param:  tab (list) liste de uméros
            n (int) numéros a rchercher
    return: nb_final (int) indice de n ou longueur de la liste
    """
    nb_final = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            nb_final = i
    return nb_final


#Test
print("Test fonction recherche:")
print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))


#Exo 2:
def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(tab[0], depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


#Test 
print("\nTest fonction exo 2:")
print(distance((1, 0), (5, 3)))
print(distance((1, 0), (0, 1)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))