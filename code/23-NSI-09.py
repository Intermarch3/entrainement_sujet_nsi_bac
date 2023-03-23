#Exo 1:
def multiplication(n1, n2):
    total, n = 0, 0
    while n != n2:
        if n2 > 0:
            total += n1
            n += 1
        else:
            total -= n1
            n -= 1
    return total


#Test
print("Test fonction multiplication:")
print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))


#Exo 2:
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m)
    else:
        return m


#Test
print("\nTestion fonction chercher")
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
#Ne fonctionne pas pour cette exemple (impossible sans changer le programme de base)
#print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))