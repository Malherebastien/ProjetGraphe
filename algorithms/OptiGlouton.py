import numpy as np
from algorithms.Graphes import Graphes
from algorithms.Glouton import Glouton


class OptiGlouton:

    def __init__(self, graphe: Glouton):
        self.graphe = graphe.graphe
        self.nb_point = graphe.nb_point
        self.points = graphe.points
        self.matrice_dimension = graphe.matrice_dimension
        self.poids_total = 0
        self.sortie_glou = graphe.sortie_glou
        self.sortie_opti = self.optimise_glou()

    def optimise_glou(self):
        """
        Prends en entrée le circuit L et décroise, si le décroisement est avantageux, tous
        les couples d’indices envisageables (a, b) jusqu’`a ce qu’il n’y ait plus aucun
        couple d’arêtes croisées.
        :return: void
        """
        sortie_opti = []
        for i in range(0, len(self.sortie_glou)):
            sortie_opti.append(self.sortie_glou[i])

        somme = 0
        changement = 1
        while changement != 0:
            changement = 0
            for i in range(0, len(sortie_opti)-1):
                for j in range(0, len(sortie_opti)-1):
                    if abs(i - j) > 1:
                        if self.est_croise(i, j, sortie_opti):
                            sortie_opti = self.echange_sommet(i, j, sortie_opti)
                            changement += 1
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[sortie_opti[i]].x - self.points[sortie_opti[i+1]].x)**2 +
                                  (self.points[sortie_opti[i]].y - self.points[sortie_opti[i+1]].y)**2)
        self.poids_total = self.graphe.long_chemin(self.sortie_glou)
        return sortie_opti

    def est_croise(self, i, j, sortie_opti):
        """
        Prend en entrée l'index d'un sommet et renvoit regarde si les arcs formés avec ses dus successeurs sont croisée
        :param i: index du sommet
        :param j: index du sommet
        :param sortie_opti : ce qu'on retourne
        :return: 1 si les arcs sont croisés, 0 sinon
        """
        abx = self.points[sortie_opti[i+1]].x - self.points[sortie_opti[i]].x
        aby = self.points[sortie_opti[i+1]].y - self.points[sortie_opti[i]].y
        acx = self.points[sortie_opti[j]].x - self.points[sortie_opti[i]].x
        acy = self.points[sortie_opti[j]].y - self.points[sortie_opti[i]].y
        adx = self.points[sortie_opti[j + 1]].x - self.points[sortie_opti[i]].x
        ady = self.points[sortie_opti[j + 1]].y - self.points[sortie_opti[i]].y

        det1 = abx * acy - aby * acx
        det2 = abx * ady - aby * adx

        cdx = self.points[sortie_opti[j + 1]].x - self.points[sortie_opti[j]].x
        cdy = self.points[sortie_opti[j + 1]].y - self.points[sortie_opti[j]].y
        cax = -acx
        cay = -acy
        cbx = self.points[sortie_opti[i + 1]].x - self.points[sortie_opti[j]].x
        cby = self.points[sortie_opti[i + 1]].y - self.points[sortie_opti[j]].y
        det3 = cdx * cay - cdy * cax
        det4 = cdx * cby - cdy * cbx

        if det1 * det2 < 0 and det3 * det4 < 0:
            l1 = self.graphe.long_chemin(sortie_opti)
            l2 = self.graphe.long_chemin(self.echange_sommet(i, j, sortie_opti))
            if l1 > l2:
                return 1
        return 0

    def echange_sommet(self, index1, index2, sortie_opti):
        """
        Prends en entrée le tableau de sommets et un index, la valeur de l'index donné est inversé avec le suivant
        :param index1: index du premier sommet du premier arc
        :param index2: index du premier sommet du second arc
        :return: liste des sommets réarangée
        """
        tab = []
        for i in range(0, len(sortie_opti)):
            tab.append(sortie_opti[i])
        if index1 < index2:
            i = index1+1
            k = index2
        else:
            i = index2+1
            k = index1
        temp = tab[i]
        tab[i] = tab[k]
        tab[k] = temp
        i += 1
        k -= 1
        while abs(i-k) > 1:
            temp = tab[i]
            tab[i] = tab[k]
            tab[k] = temp
            i += 1
            k -= 1

        return tab
