import numpy as np

from algorithms.Graphes import Graphes


class OptiGlouton(Graphes):
    def optimise_glou(self): #opti_glou
        """
        Prends en entrée le circuit L et décroise, si le décroisement est avantageux, tous
        les couples d’indices envisageables (a, b) jusqu’`a ce qu’il n’y ait plus aucun
        couple d’arêtes croisées.
        :param circuit: La liste correspondant au circuit hamiltonien obtenu à partir du sommet (obtenu via glouton())
        :return: void
        """

        for i in range(0, len(self.sortie_glou)):
            self.chemins.append(self.sortie_glou[i])

        somme = 0
        changement = 1
        while changement != 0:
            changement = 0
            for i in range(0, len(self.chemins)-1):
                for j in range(0, len(self.chemins)-1):
                    if abs(i - j) > 1:
                        if self.est_croise(i, j):
                            print("application", i, " et ", j)
                            self.chemins = self.echange_sommet(i, j)
                            changement += 1
        # print(self.chemins)
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[self.chemins[i]].x - self.points[self.chemins[i+1]].x)**2 +
                                  (self.points[self.chemins[i]].y - self.points[self.chemins[i+1]].y)**2)
        print(somme)
        return self.chemins

    def est_croise(self, i, j): #opti_glou
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
            l1 = self.long_chemin(self.chemins)
            l2 = self.long_chemin(self.echange_sommet(i, j))
            print("l1 = ", l1, " l2 = ", l2)
            if l1 > l2:
                return 1
        return 0

    def echange_sommet(self, index1, index2): #opti_glou
        """
        Prends en entrée le tableau de sommets et un index, la valeur de l'index donné est inversé avec le suivant
        :param sommets: Tableau des sommets triés par glouton
        :param index: index de la valeur à échanger avec la suivante
        :return: liste des sommets réarangée
        """
        tab = []
        for i in range(0, len(self.chemins)):
            tab.append(self.chemins[i])
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
            i+=1
            k-=1

        return tab
