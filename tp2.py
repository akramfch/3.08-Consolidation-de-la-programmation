import math


class Point:
    def __init__(self, x : float = 0, y : float = 0) -> None:
        self.__x = x
        self.__y = y
    def __str__(self) -> str:
        return f"Point : ({self.__x}, {self.__y})"

    def distanceCoord(self,x : float, y : float) -> float:
        distance = math.sqrt(math.pow(self.__x-x,2)+math.pow(self.__y-y,2))
        return distance
    def distancePoint (self, camarade : "Point") -> float:
        return self.distanceCoord(camarade.__x,camarade.__y)

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

    def intersection(self, autre : "Cercle") -> bool:
        distance = self.__centre.distancePoint(autre.__centre)
        if distance > self.__rayon + autre.__rayon:
            return False

    def contientPoint(self, A: Point) -> bool:
        distance = self.__centre.distancePoint(A)
        if distance <= self.__rayon:
            return True


if __name__ == "__main__":

