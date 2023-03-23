#Exo 1:
def maxliste(tab):
    """
    Renvoie numéro max de la liste
    param: tab (liste) liste de numéros entiers
    return: max (int) numéro max
    """
    assert len(tab) > 0, "Liste vide"
    max = tab[0]
    for i in range(1, len(tab)):
        if max < tab[i]:
            max = tab[i]
    return max


#Test
print("Test fonction maxliste:")
print(maxliste([98, 12, 104, 23, 131, 9]))
print(maxliste([-27, 24, -3, 15]))


#Exo 2:
class Pile:
    """
    Classe definissant une pile
    """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """
        Renvoie True si la pile est vide, False sinon
        """
        return self.valeurs == []

    def empiler(self, c):
        """
        Place l'element c au sommet de la pile
        """
        self.valeurs.append(c)

    def depiler(self):
        """
        Supprime l'element place au sommet de la pile, a condition qu'elle soit non vide
        """
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage(ch):
    """
    Renvoie True si la chaine ch est bien parenthesee et False sinon
    """
    p = Pile()
    for c in ch:
        if c == "(":
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()


#Test
print("\nTest fonction parenthesage")
print(parenthesage("((()())(()))"))
print(parenthesage("())(()"))
print(parenthesage("(())(()"))
