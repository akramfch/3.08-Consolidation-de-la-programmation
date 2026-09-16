class Personnage():
    def __init__(self, pseudo: str, niveau: int=1) -> None:
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau

    def attaque(self, autre : "Personnage") -> None:
        if self.__initiative > autre.__initiative:
            autre.__pv -= self.degats()
            if autre.__pv > 0:
                self.__pv -=  autre.degats()
        elif self.__initiative < autre.__initiative:
            self.__pv -= autre.degats()
            if self.__pv > 0:
                autre.__pv -= self.degats()
        else:
            self.__pv -= autre.degats()
            autre.__pv -= self.degats()

    def combat (self, autre : "Personnage") -> None:
        while self.__pv > 0 and autre.__pv > 0:
            self.attaque(autre)
            print(f"Le joueur {self.__pseudo} a {self.__pv} PV")
            print(f"Le joueur {autre.__pseudo} a {autre.__pv} PV")

    def soigner (self) -> None:
        self.__pv = self.__niveau

    def get_pv(self) -> int:
        return self.__pv

    def set_pv(self, valeur: int) -> None:
        self.__pv = valeur

    def get_initiative(self) -> int:
        return self.__initiative

    def set_initiative(self, valeurinit: int) -> None:
        self.__initiative = valeurinit

    def get_niveau(self) -> int:
        return self.__niveau

    def get_pseudo(self) -> str:
        return self.__pseudo

    def __eq__(self, autre : "Personnage") -> bool:
        if self.get_pseudo() == autre.get_pseudo():
            return True
        else:
            return False

    def degats(self) -> int:
        return self.get_niveau()

class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        super().__init__(pseudo, niveau)
        self.set_pv(niveau * 8 + 4)
        self.set_initiative(niveau * 4 + 6)

    def degats(self) -> int:
        return self.get_niveau()*2

class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int=1) -> None:
        super().__init__(pseudo, niveau)
        self.set_initiative(niveau*6 + 4)
        self.set_pv(niveau*5 + 10)
        self.__mana = niveau*5

    def degats(self) -> int:
        if self.__mana > 0:
            self.__mana -= 4
            return self.get_niveau()+3
        else:
            return self.get_niveau()

class Joueur():
    def __init__(self, nom: str, nbmaxperso : int) -> None:
        self.__nom = nom
        self.__personnages = []
        self.__nbmaxperso = nbmaxperso

    def ajtperso(self, perso : Personnage) -> None:
        if len(self.__personnages) < self.__nbmaxperso:
            self.__personnages.append(perso)

    def get_personum(self, num: int) -> Personnage:
        return self.__personnages[num]

    def get_pseudoperso(self, pseudo :str) -> Personnage:
        for perso in self.__personnages:
            if pseudo == perso.get_pseudo():
                return perso

    def get_perso_objet(self, persorecherche: "Personnage") -> Personnage:
        for perso in self.__personnages:
            if perso == persorecherche:
                return perso

    def supp_personum(self, num : int) -> None:
        self.__personnages.pop(num)

    def supp_pseudoperso(self, pseudo :str) -> None:
        for perso in self.__personnages:
            if pseudo == perso.get_pseudo():
                self.__personnages.remove(perso)

    def supp_perso_objet(self, persorecherche: "Personnage") -> None:
        for perso in self.__personnages:
            if perso == persorecherche:
                self.__personnages.remove(perso)
                return 
