import numpy.random as rd
import math

from algorithms.Point import *
from algorithms.Graphes import *

points = []
nb_point = 10

x = 0
while x < nb_point:
    points.append(Point(rd.randint(0, 1000) / 1000, rd.randint(0, 1000) / 1000))
    x = x + 1

for p in points:
    print(str(p.x) + " , " + str(p.y))


def remplir_matrice():
    matrice = [nb_point][nb_point]
    i = 0
    while i < nb_point:
        j = 0
        while j < nb_point - i:
            if i == j:
                matrice[i][j] = 0
            else:
                matrice[i][j] = math.sqrt((points[i].x - points[j].x) ^ 2 + (points[i].y - points[j].y) ^ 2)
                matrice[j][i] = math.sqrt((points[i].x - points[j].x) ^ 2 + (points[i].y - points[j].y) ^ 2)
            j = j + 1
        i = i + 1
    return matrice


graphe = Graphes(nb_point, points, remplir_matrice())
