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
        return self.sortie_glou
