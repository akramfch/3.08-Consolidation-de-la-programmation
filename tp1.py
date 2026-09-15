import math


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x et y doivent être des nombres")
        self.__x = x
        self.__y = y

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"Point : ({self.__x}, {self.__y})"

    def distanceCoord(self, x: float, y: float) -> float:
        distance = math.sqrt(math.pow(self.__x - x, 2) + math.pow(self.__y - y, 2))
        return distance

    def distancePoint(self, camarade: "Point") -> float:
        return self.distanceCoord(camarade.__x, camarade.__y)


class Cercle:
    def __init__(self, rayon: float, centre: Point = None) -> None:
        self.__rayon = rayon

        if centre is None:
            self.__centre = Point()
        else:
            self.__centre = centre

    def diametre(self) -> float:
        return self.__rayon * 2

    def perimetre(self) -> float:
        return self.__rayon * 2 * math.pi

    def surface(self) -> float:
        return self.__rayon * self.__rayon * math.pi

    def intersection(self, autre: "Cercle") -> bool:
        distance = self.__centre.distancePoint(autre.__centre)

        if distance > self.__rayon + autre.__rayon:
            return False
        else:
            return True

    def contientPoint(self, A: Point) -> bool:
        distance = self.__centre.distancePoint(A)

        if distance <= self.__rayon:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, pointInit: Point = Point(), longueur: float = 1, hauteur: float = 1, pointHautDroit : Point=None) -> None:

        self.__pointInit = pointInit
        if pointHautDroit is None:
            self.__longueur = longueur
            self.__hauteur = hauteur
        else:
            self.__longueur = pointHautDroit.get_x() - pointInit.get_x()
            self.__hauteur = pointHautDroit.get_y() - pointInit.get_y()

    def surface(self) -> float:
        return self.__longueur * self.__hauteur

    def perimetre(self) -> float:
        return self.__longueur * 2 + self.__hauteur * 2

    def pointBasGauche(self) -> Point:
        return self.__pointInit

    def pointBasDroit(self) -> Point:
        return  Point(self.__pointInit.get_x() + self.__longueur, self.__pointInit.get_y())

    def pointHautGauche(self) -> Point:
        return Point(self.__pointInit.get_x(), self.__pointInit.get_y() + self.__hauteur)

    def pointHautDroite(self) -> Point:
        return Point(self.__pointInit.get_x() + self.__longueur, self.__pointInit.get_y() + self.__hauteur)

    def contientPoint(self, A: Point) -> bool:
        if self.__pointInit.get_x() < A.get_x() < self.__pointInit.get_x() + self.__longueur and self.__pointInit.get_y() < A.get_y() < self.__pointInit.get_y() + self.__hauteur:
            return True
        else:
            return False

class triangle:
    def __init__(self, cote1 : float, cote2 : float, angledroit : Point=Point()) -> None:
        self.__cote1 = cote1
        self.__cote2 = cote2
        self.__angledroit = angledroit

    def hypotenuse(self) -> float:
        return  math.sqrt(math.pow(self.__cote1, 2) + math.pow(self.__cote2, 2))

    def perimetretri(self) -> float:
        return self.hypotenuse() + self.__cote1 + self.__cote2

    def surfacetri(self) -> float:
        return (self.__cote1 * self.__cote2) / 2

    def isocele(self) -> bool:
        if self.__cote1 == self.__cote2:
            return True
        else:
            return False













if __name__ == "__main__":
    P1 = Point()
    P2 = Point(3, 4)

    print(P1)
    print(P2)
    print(P1.distancePoint(P2))

    C1 = Cercle(5)
    C2 = Cercle(3, Point(4, 0))

    print(C1.diametre())
    print(C1.perimetre())
    print(C1.surface())
    print(C1.intersection(C2))
    print(C1.contientPoint(P2))