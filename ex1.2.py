def grand (a : int, b : int) -> int :
    """
    fonction qui renvoie la valeur la plus grande
    """
    return a if a>b else b

def limite (a : int, seuil : int=10) -> bool :
    """
    fonction qui renvoie True si a est supérieur au seuil indiqué
    """
    if a>seuil:
        return True
    else:
        return False

def Grandliste(*args):
    max = args[0]

    for valeur in args:
        if valeur > max:
            max = valeur

    return max

def compter_inferieur(*args, seuil: float= 3) -> int:
    nb = 0
    for valeur in args:
        if valeur < seuil:
            nb += 1

    return nb

def affiche_dictionnaire(prefixe: str, **kwargs) -> None:
    for cle, valeur in kwargs.items():
        print(f"{prefixe} {cle} : {valeur}")