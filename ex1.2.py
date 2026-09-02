def grand (a : int, b : int) -> int :
    """
    fonction qui renvoie la valeur la plus grande
    """
    return a if a>b else b

def limite (a : int, seuil : int=10) -> bool :
    """
    fonction qui renvoie la valeur la plus grande
    """
    if a>seuil:
        return True
    else:
        return False

def Grandliste (liste :list,)