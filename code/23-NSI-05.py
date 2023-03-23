#Exo 1:
from random import randint

def lancer(n):
    """
    Renvoie une liste de longueur n avec des chiffre aléatoire de 1 à 6 
    param: n (int) longueur de la liste
    return: tab (liste) liste de numéros
    """
    assert type(n) == int and n > 0, "Mauvais paramètre"
    tab = []
    for i in range(n):
        tab.append(randint(1, 6))
    return tab


def lancer_6(tab):
    """
    Vérifie si il ya plus de 6 ou de 2 dans une liste de numéros
    param: tab (liste) liste de numéros de 1 à 6
    return: (bool) True si plus de 6 que de 2 sinon False
    """
    nb_2, nb_6 = 0, 0
    for nb in tab:
        if nb == 2:
            nb_2 += 1
        elif nb == 6:
            nb_6 += 1
    if nb_6 >= nb_2:
        return True
    else:
        return False


#Test
print("Test fonction lancer et lancer_6")
tab = lancer(6)
print(tab)
print(lancer_6(tab))


#Exo 2:
img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 0
    return L


def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''
    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


#Test
print("\nTest fonction exo 2")
print(binaire(img, 100))
print(negatif(img))