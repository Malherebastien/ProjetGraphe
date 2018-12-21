import numpy as np
from algorithms.Point import *

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
        self.chemins = []

    def glouton(self, sommet):
        """
        L’algorithme glouton consiste, en partant d’un sommets tiré au hasard, à rejoindre
        systématiquement le sommet le plus proche que l’on n’a pas encore
        visité
        :param sommet : Un sommet aléatoire duquel on commence, représenté par son indice dans le tableau
        :return : La liste L correspondant au circuit hamiltonien obtenu à partir du sommet
        """
        self.chemins = [sommet]
        prochain_sommet = sommet
        somme = 0
        for i in range(0, self.nb_point):
            for x in self.plus_proche_sommet(prochain_sommet):
                if not self.chemins.__contains__(x):
                    self.chemins.append(x)
                    prochain_sommet = x
                    print(prochain_sommet)
                    break
        print(self.chemins)
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[self.chemins[i]].x - self.points[self.chemins[i+1]].x)**2 +
                                  (self.points[self.chemins[i]].y - self.points[self.chemins[i+1]].y)**2)
        print(somme)
        return self.optimise_glou()

    def plus_proche_sommet(self, sommet):
        """
        parcours pour trouver les sommets les plus proches et renvoi un tableau des sommets (en excluant lui-même)
        :param sommet: Point
        :return: liste de sommet, rangés dans l'ordre croissant de leur distance
        """
        sommets = []
        dimensions = sorted(self.matrice_dimension[sommet])
        print(self.matrice_dimension[sommet])
        for i in dimensions:
            for j in self.matrice_dimension[sommet]:
                if i == j:
                    sommets.append(self.matrice_dimension[sommet].tolist().index(i))
        return sommets

    def optimise_glou(self):
        """
        Prends en entrée le circuit L et décroise, si le décroisement est avantageux, tous
        les couples d’indices envisageables (a, b) jusqu’`a ce qu’il n’y ait plus aucun
        couple d’arêtes croisées.
        :param circuit: La liste correspondant au circuit hamiltonien obtenu à partir du sommet (obtenu via glouton())
        :return: void
        """
        somme = 0
        changement = 1
        while changement != 0:
            changement = 0
            for i in range(0, len(self.chemins)-1):
                for j in range(0, len(self.chemins)-1):
                    if abs(i -j) > 1:
                        if self.est_croise(i, j):
                            print("application")
                            self.chemins = self.echange_sommet(i, j)
                            changement += 1
            #break
        print(self.chemins)
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[self.chemins[i]].x - self.points[self.chemins[i+1]].x)**2 +
                                  (self.points[self.chemins[i]].y - self.points[self.chemins[i+1]].y)**2)
        print(somme)
        return self.chemins

    def est_croise(self, i, j):
        """
        Prend en entrée l'index d'un sommet et renvoit regarde si les arcs formés avec ses dus successeurs sont croisée
        :param index: index du sommet
        :return: 1 si les arcs sont croisés, 0 sinon
        """
        abx = self.points[self.chemins[i+1]].x - self.points[self.chemins[i]].x
        aby = self.points[self.chemins[i+1]].y - self.points[self.chemins[i]].y
        acx = self.points[self.chemins[j]].x - self.points[self.chemins[i]].x
        acy = self.points[self.chemins[j]].y - self.points[self.chemins[i]].y
        adx = self.points[self.chemins[j + 1]].x - self.points[self.chemins[i]].x
        ady = self.points[self.chemins[j + 1]].y - self.points[self.chemins[i]].y

        det1 = abx * acy - aby * acx
        det2 = abx * ady - aby * adx

        cdx = self.points[self.chemins[j + 1]].x - self.points[self.chemins[j]].x
        cdy = self.points[self.chemins[j + 1]].y - self.points[self.chemins[j]].y
        cax = -acx
        cay = -acy
        cbx = self.points[self.chemins[i + 1]].x - self.points[self.chemins[j]].x
        cby = self.points[self.chemins[i + 1]].y - self.points[self.chemins[j]].y
        det3 = cdx * cay - cdy * cax
        det4 = cdx * cby - cdy * cbx

        if det1 * det2 < 0 and det3 * det4 < 0:
            print("entrée dans le if")
            if self.long_chemin(self.chemins) > self.long_chemin(self.echange_sommet(i, j)):
                print(self.long_chemin(self.chemins), " > ", self.long_chemin(self.echange_sommet(i, j)), " vrai")
                self.echange_sommet(i, j)
                return 1
            else:
                return 0
        else:
            return 0


    def echange_sommet(self, index1, index2):
        """
        Prends en entrée le tableau de sommets et un index, la valeur de l'index donné est inversé avec le suivant
        :param sommets: Tableau des sommets triés par glouton
        :param index: index de la valeur à échanger avec la suivante
        :return: liste des sommets réarangée
        """
        tab = self.chemins
        print("lol -> ", self.chemins)
        temp = tab[index1]
        tab[index1] = tab[index2]
        tab[index2] = temp
        print("lol -> ", self.chemins)
        return tab

    def long_chemin(self, tab):
        """
        Donne la longueur totale du chemin
        :param tab: tableau de l'ordre des points
        :return:longueur du chemin passant par tous les points du tableau
        """
        somme = 0
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[tab[i]].x - self.points[tab[i+1]].x)**2 +
                                  (self.points[tab[i]].y - self.points[tab[i+1]].y)**2)
        return somme


    def pvc_prim(self, sommet):
        """
        Il consiste à choisir un sommet au hasard parmi les N sommets et à construire
        un arbre couvrant de poids minimun, en utilisant l’algorithme de Prim
        :param sommet: Un sommet s du graphe
        :return: Le cycle hamiltonien du graphe [0, 2, 6, 3, 9, 1, 5, 7, 4, 8]
        """