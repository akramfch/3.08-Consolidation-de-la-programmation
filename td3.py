def division(a : float, b : float) -> float:
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("Mauvais type de valeur")
    if b == 0:
        raise ZeroDivisionError("Division par zero impossible")
    return a / b

try:
    resultat = division(10, 2)
except ZeroDivisionError:
    print("Division par zéro impossible")

except TypeError:
    print("Mauvais type de valeur")

