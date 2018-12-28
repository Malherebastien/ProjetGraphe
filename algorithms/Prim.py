import numpy as np

from algorithms.Graphes import Graphes


class Prim(Graphes):
    def pvc_prim(self, sommet):  # prim
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
            for x in self.plus_proche_sommet(r):
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
