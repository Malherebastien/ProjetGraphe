from algorithms.Graphes import Graphes


class Primm(Graphes):
    def pvc_prim(self, sommet): #prim
        """
        Il consiste à choisir un sommet au hasard parmi les N sommets et à construire
        un arbre couvrant de poids minimun, en utilisant l’algorithme de Prim
        :param sommet: Un sommet s du graphe
        :return: Le cycle hamiltonien du graphe
        """
