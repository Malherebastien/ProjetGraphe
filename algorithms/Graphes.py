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
        self.chemins = []

    def glouton(self, sommet):
        """
        L’algorithme glouton consiste, en partant d’un sommets tiré au hasard, à rejoindre
        systématiquement le sommet le plus proche que l’on n’a pas encore
        visité
        :param sommet : Un sommet aléatoire duquel on commence, représenté par son indice dans le tableau
        :return : La liste L correspondant au circuit hamiltonien obtenu à partir du sommet
        """
        visite = [sommet]
        prochain_sommet = sommet
        for i in range(0, self.nb_point):
            for x in self.plus_proche_sommet(prochain_sommet):
                if not visite.__contains__(x):
                    visite.append(x)
                    prochain_sommet = x
        print(visite)
        return visite

    def plus_proche_sommet(self, sommet):
        """
        parcours pour trouver les sommets les plus proches et renvoi un tableau des sommets (en excluant lui-même)
        :param sommet: Point
        :return: liste de sommet, rangés dans l'ordre croissant de leur distance
        """
        sommets = []
        dimensions = sorted(self.matrice_dimension[sommet])
        print(dimensions)
        for i in dimensions:
            for j in self.matrice_dimension[sommet]:
                if i == j:
                    sommets.append(self.matrice_dimension[sommet].tolist().index(i))
        return sommets

    def optimise_glou(self, circuit):
        """
        Prends en entrée le circuit L et décroise, si le décroisement est avantageux, tous
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
