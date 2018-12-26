from algorithms.Graphes import *
from algorithms.Fenetre import*
import numpy as np

points = []
nb_point = 20

x = 0
while x < nb_point:
    points.append(Point(x, np.random.randint(0, 1000) / 1000, np.random.randint(0, 1000) / 1000))
    x = x + 1


def remplir_matrice():
    matrice = np.full((nb_point, nb_point), np.inf)
    i = 0
    while i < nb_point:
        j = 0 + i
        while j < nb_point:
            if i == j:
                matrice[i][j] = np.inf
            else:
                matrice[i][j] = np.math.sqrt((points[i].x - points[j].x)**2 + (points[i].y - points[j].y)**2)
                matrice[j][i] = np.math.sqrt((points[i].x - points[j].x)**2 + (points[i].y - points[j].y)**2)
            j = j + 1
        i = i + 1
    return matrice


fenetre = Fenetre(points)
graphe = Graphes(nb_point, points, remplir_matrice())
fenetre.afficher_totale(graphe.pvc_prim(0))
