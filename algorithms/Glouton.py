import numpy as np

from algorithms.Graphes import Graphes


class Glouton:
    def __init__(self, graphe: Graphes):
        self.graphe = graphe

    def glouton(self, sommet):  # glouton
        """
        L’algorithme glouton consiste, en partant d’un sommets tiré au hasard, à rejoindre
        systématiquement le sommet le plus proche que l’on n’a pas encore visité
        :param sommet : Un sommet aléatoire duquel on commence, représenté par son indice dans le tableau
        :return : La liste L correspondant au circuit hamiltonien obtenu à partir du sommet
        """
        self.graphe.sortie_glou = [sommet]
        prochain_sommet = sommet
        somme = 0
        for i in range(0, self.graphe.nb_point):
            for x in self.graphe.plus_proche_sommet(prochain_sommet):
                if not self.graphe.sortie_glou.__contains__(x):
                    self.graphe.sortie_glou.append(x)
                    prochain_sommet = x
                    break
        for i in range(0, self.graphe.nb_point-1):
            somme += np.math.sqrt((self.graphe.points[self.graphe.sortie_glou[i]].x -
                                   self.graphe.points[self.graphe.sortie_glou[i+1]].x)**2 +
                                  (self.graphe.points[self.graphe.sortie_glou[i]].y -
                                   self.graphe.points[self.graphe.sortie_glou[i+1]].y)**2)
        print(somme)
        return self.graphe.sortie_glou
