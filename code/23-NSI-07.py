#Exo 1:
def fusion(tab1, tab2):
    tab = tab1 + tab2
    return sorted(tab)


#Version artisanal
def fusion_2(tab1, tab2):
    tab = []
    n1, n2 = 0, 0
    len1, len2 = len(tab1) - 1, len(tab2) - 1
    while n1 <= len1 and n2 <= len2:
        if tab1[n1] <= tab2[n2]:
            tab.append(tab1[n1])
            n1 += 1
        else:
            tab.append(tab2[n2])
            n2 += 1
    if n1 != len1:
        return tab + tab2[n2:]
    else:
        return tab + tab1[n1:]

#Test
print("Test fonction fusion")
print(fusion([3, 5], [2, 5]))
print(fusion_2([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion_2([-2, 4], [-3, 5, 10]))

#Exo 2:
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre) :
    """ Renvoie l'ecriture decimale du nombre donné en chiffres romains """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]] :
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return (romains[nombre[1]] - romains[nombre[0]]) + traduire_romain(nombre[2:]) if len(nombre) > 2 else (romains[nombre[1]] - romains[nombre[0]])

"""
version modifier mais plus lisible: vers la fin

def traduire_romain(nombre) :
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]] :
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        if len(nombre) > 2:
            return (romains[nombre[1]] - romains[nombre[0]]) + traduire_romain(nombre[2:])
        else:
            return (romains[nombre[1]] - romains[nombre[0]])
"""

#Test
print("\nTest fonction traduire_romain:")
print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))
