import numpy as np
from algorithms.Point import *


class Graphes:
    """La classe principale :"""

    def __init__(self, nb_point, points, matrice_dimension):
        """
        nb_point : le nombre de point
        points : liste de points
        matrice_dimension : La matrice des dimensions N*N définie par D[i,j]
        contenant la distance euclidiènne en Pi et Pj
        """
        self.nb_point = nb_point
        self.points = points
        self.matrice_dimension = matrice_dimension

    def glouton(self, sommet: Point):
        """
        L’algorithme glouton consiste, en partant d’un sommets tiré au hasard, à rejoindre
        systématiquement le sommet le plus proche que l’on n’a pas encore
        visité
        :param sommet : Un sommet aléatoire
        :return : La liste L correspondant au circuit hamiltonien obtenu à partir du sommet
        """
        visite = np.zeros((self.nb_point, self.nb_point))
        print(self.plus_proche_sommet(sommet))

    def plus_proche_sommet(self, sommet: Point):
        """
        parcours pour trouver les sommets les plus proches et renvoi un tableau des sommets (en excluant lui-même)
        :param sommet: Point
        :return: liste de sommet, rangés dans l'ordre croissant de leur distance
        """
        print(self.matrice_dimension[sommet.point_id])
        sommets = []
        dimensions = sorted(self.matrice_dimension[sommet.point_id])
        print(dimensions)
        for i in dimensions:
            for j in self.matrice_dimension[sommet.point_id]:
                if i == j:
                    sommets.append(self.matrice_dimension[sommet.point_id].tolist().index(i))
        return sommets

    def optimise_glou(self, circuit):
        """
        Prends en entrée le circuit L est décroise, si le décroisement est avantageux, tous
        les couples d’indices envisageables (a, b) jusqu’`a ce qu’il n’y ait plus aucun
        couple d’arêtes croisées.
        :param circuit: La liste correspondant au circuit hamiltonien obtenu à partir du sommet (obtenu via glouton())
        :return: void
        """

    def pvc_prim(self, sommet):
        """
        Il consiste à choisir un sommet au hasard parmi les N sommets et à construire
        un arbre couvrant de poids minimun, en utilisant l’algorithme de Prim
        :param sommet: Un sommet s du graphe
        :return: Le cycle hamiltonien du graphe
        """
