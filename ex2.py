class Tasse:
    matiere : str = "ceramique"
    def __init__(self, couleur : str, contenance : float, marque : str) -> None:
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def remplir(self, contenu: str) -> None:
        self.contenu = contenu

    def boire(self) -> None:
        del self.contenu

    def __str__(self) -> str:
        return f"la tasse de matiere {self.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} mL"

tasse1 = Tasse("bleue", 50, "Duralex")
'''il faut respecter l'ordre des instances lorsque l'on veut ajouter un objet à la classe'''
print(tasse1)
