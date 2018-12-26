import numpy as np

from algorithms.Graphes import Graphes


class Glouton(Graphes):
    def glouton(self, sommet): #glouton
        """
        L’algorithme glouton consiste, en partant d’un sommets tiré au hasard, à rejoindre
        systématiquement le sommet le plus proche que l’on n’a pas encore
        visité
        :param sommet : Un sommet aléatoire duquel on commence, représenté par son indice dans le tableau
        :return : La liste L correspondant au circuit hamiltonien obtenu à partir du sommet
        """
        self.sortie_glou = [sommet]
        prochain_sommet = sommet
        somme = 0
        for i in range(0, self.nb_point):
            for x in self.plus_proche_sommet(prochain_sommet):
                if not self.sortie_glou.__contains__(x):
                    self.sortie_glou.append(x)
                    prochain_sommet = x
                    # print(prochain_sommet)
                    break
        # print(self.chemins)
        for i in range(0, self.nb_point-1):
            somme += np.math.sqrt((self.points[self.sortie_glou[i]].x - self.points[self.sortie_glou[i+1]].x)**2 +
                                  (self.points[self.sortie_glou[i]].y - self.points[self.sortie_glou[i+1]].y)**2)
        print(somme)
        return self.optimise_glou()

    def plus_proche_sommet(self, sommet): #glouton
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
                    # self.poids_total += self.matrice_dimension[sommet].tolist().index(i)
                    # print(self.poids_total)
        return sommets
