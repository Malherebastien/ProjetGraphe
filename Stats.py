from algorithms.Graphes import *
from algorithms.Glouton import Glouton
from algorithms.OptiGlouton import OptiGlouton
from algorithms.Prim import Prim
from Laucher import remplir_matrice


class Stats:
    def __init__(self, nb_test, nb_pts):
        self.nb_test = nb_test
        self.nb_pts = nb_pts
        self.amelio_glou_opti = 0
        self.amelio_opti_prim = 0
        self.moy_lg = 0
        self.moy_lo = 0
        self.moy_lp = 0

    def tests_en_chaine(self):
        res_glou_opti = []
        res_opti_prim = []
        lg = []
        lo = []
        lp = []
        for n in range(1, self.nb_test):
            points = []
            x = 0
            while x < self.nb_pts:
                points.append(Point(x, np.random.randint(0, 1000) / 1000, np.random.randint(0, 1000) / 1000))
                x += 1
            graphe = Graphes(self.nb_pts, points, remplir_matrice())

            sommet_depart = np.random.randint(0, graphe.nb_point)
            graphe_glouton = Glouton(graphe, sommet_depart)
            graphe_opti = OptiGlouton(graphe_glouton)
            graphe_prim = Prim(graphe, sommet_depart)

            res_glou_opti.append((graphe_glouton.poids_total - graphe_opti.poids_total)
                                 / graphe_glouton.poids_total * 100)
            res_opti_prim.append((graphe_opti.poids_total - graphe_prim.poids_total)
                                 / graphe_opti.poids_total * 100)

            lg.append(graphe_glouton.poids_total)
            lo.append(graphe_opti.poids_total)
            lp.append(graphe_prim.poids_total)

        self.moy_lg = sum(lg) / len(lg)
        self.moy_lo = sum(lo) / len(lo)
        self.moy_lp = sum(lp) / len(lp)
        self.amelio_glou_opti = sum(res_glou_opti) / len(res_glou_opti)
        self.amelio_opti_prim = sum(res_opti_prim) / len(res_opti_prim)
