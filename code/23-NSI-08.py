#Exo 1:
def max_dico(dico):
    """
    Renvoie la clée et sa valeur la plus élevé du dico
    param: dico (dict)
    return: (tuple) clée et valeur la plus élevé
    """
    maxi = list(dico.keys())[0]
    for key in dico.keys():
        if dico[key] > dico[maxi]:
            maxi = key
    return (maxi, dico[maxi])


#Test
print("Test fonction max_dico:")
print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))


#Exo 2:
class Pile:
    """
    Classe definissant une structure de pile.
    """
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """
        Renvoie le booleen True si la pile est vide, False sinon.
        """
        return self.contenu == []

    def empiler(self, v):
        """
        Place l'element v au sommet de la pile
        """
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'element place au sommet de la pile,
        si la pile n'est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return resultat


#Test
print("\nTest fonction eva_expression:")
print(eval_expression([2, 3, '+', 5, '*']))