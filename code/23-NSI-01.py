#Exo 1:
def verifie(tab):
    """
    Vérifie si la liste est trié dans l'ordre croissant
    param: tab (list) liste de numéros
    return: True ou False (bool)
    """
    assert len(tab) > 0, "Tableau vide"
    value = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < value:
            return False
        value = tab[i]
    return True


#Test:
print("test fonction verifie:")
print(verifie([0, 1, 3, 7, 10, 27, 17]))
print(verifie([0, 1, 3, 7, 10, 27, 27]))


#Exo 2:
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B', 'A']

def depouille(urne):
    """depouille une urne"""
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat


def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


#Test
print("Test fonction dépouille et vainqueur")
election = depouille(urne)
print(election)
print(vainqueur(election))