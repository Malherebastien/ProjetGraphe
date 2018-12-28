import numpy as np

class Graphes:
    """La classe principale :"""

    def __init__(self, nb_point, points, matrice_dimension):
        """
        nb_point : le nombre de point
        points : liste de points
        matrice_dimension : La matrice des dimensions N*N définie par D[i,j]
        contenant la distance euclidienne en Pi et Pj
        """
        self.nb_point = nb_point
        self.points = points
        self.matrice_dimension = matrice_dimension
        self.poids_total = 0
        self.sortie_glou = []
        self.sortie_opti = []

    def long_chemin(self, tab):
        """
        Donne la longueur totale du chemin
        :param tab: tableau de l'ordre des points
        :return:longueur du chemin passant par tous les points du tableau
        """
        print("somme -> ", tab)
        somme = 0
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[tab[i]].x - self.points[tab[i+1]].x)**2 +
                                  (self.points[tab[i]].y - self.points[tab[i+1]].y)**2)
        return somme

    def plus_proche_sommet(self, sommet):
        """
        parcours pour trouver les sommets les plus proches et renvoi un tableau des sommets (en excluant lui-même)
        :param sommet: Point
        :return: liste de sommet, rangés dans l'ordre croissant de leur distance
        """
        sommets = []
        dimensions = sorted(self.matrice_dimension[sommet])
        # print(self.matrice_dimension[sommet])
        for i in dimensions:
            for j in self.matrice_dimension[sommet]:
                if i == j:
                    sommets.append(self.matrice_dimension[sommet].tolist().index(i))

        return sommets