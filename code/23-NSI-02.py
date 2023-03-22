#Exo 1
def indices_maxi(tab):
    """
    Trouve le plus grand numéro et les indices de ce numéro
    param: tab (list) liste de numéros
    return: (tuple) numéros max et ces indices
    """
    assert len(tab) > 0, "Tableau vide"
    maxi = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
    tab_final = []
    for i in range(len(tab)):
        if tab[i] == maxi:
            tab_final.append(i)
    return (maxi, tab_final)


#Test
print("Test fonction indices_maxi:")
print(indices_maxi([0, 3, 1, 4, 7, 2, 5, 7]))


#Exo 2:
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

#Test
print("Test fonction positif")
print(positif([-1, 2, -3, 4, -5, 6, -7, 8, -9]))