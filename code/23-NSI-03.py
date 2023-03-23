#Exo 1:
def moyenne(tab):
    """
    Calcule la moyenne des note de la liste
    param: tab (liste) liste de tuple qui contient les notes et leurs coef
    return: moyenne (float) ou None si coef egal 0
    """
    assert len(tab) > 0, "Liste vide"
    total_coef = 0
    total_note = 0
    for note in tab:
        total_note += note[0] * note[1]
        total_coef += note[1]
    if total_coef > 0:
        return total_note / total_coef
    else:
        return None


#Test
print("Test fonction moyenne:")
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))


#Exo 2:
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        des " *" , les 0 par deux espaces "  " 
        La valeur "" donnée au paramètre end permet 
        de ne pas avoir de  saut de ligne. '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(" *", end="")
            else:
                print("  ", end="")
        print()


def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
       élément de liste_depart'''
    liste_zoom = []
    for elt in  liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    '''renvoie une grille ou les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoom=[]
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom


#Test
print("Test fonction exo 2:")
affiche(coeur)
affiche(zoomDessin(coeur, 3))
