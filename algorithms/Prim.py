from algorithms.Graphes import Graphes
import numpy as np


class Prim:

    def __init__(self, graphe: Graphes, sommet_depart):
        self.graphe = graphe
        self.nb_point = graphe.nb_point
        self.points = graphe.points
        self.matrice_dimension = graphe.matrice_dimension
        self.poids_total = 0
        self.sortie_glou = graphe.sortie_glou
        self.sortie_opti = graphe.sortie_opti
        self.matrice_lien = self.pvc_prim(sommet_depart)

    def pvc_prim(self, sommet):
        """
        Il consiste à choisir un sommet au hasard parmi les N sommets et à construire
        un arbre couvrant de poids minimun, en utilisant l’algorithme de Prim
        :param sommet: Un sommet s du graphe
        :return: Le cycle hamiltonien du graphe
        """

        tab_visited = []
        matrice_lien = np.full((self.nb_point, self.nb_point), 0)
        r = sommet
        s_actuel = 0
        tab_visited.append(r)
        while len(tab_visited) < self.nb_point:
            change = 0
            for x in self.graphe.plus_proche_sommet(r):
                if not tab_visited.__contains__(x):
                    tab_visited.append(x)
                    matrice_lien[r][x] = 1
                    r = x
                    print(r)
                    s_actuel = len(tab_visited) - 1
                    change = 1
                    break
            if change == 0:
                if s_actuel != 0:
                    s_actuel -= 1
                r = tab_visited[s_actuel]

        return matrice_lien
