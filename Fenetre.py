from tkinter import *

from Stats import Stats

from algorithms.Prim import Prim
from algorithms.Glouton import Glouton
from algorithms.Graphes import *
from algorithms.OptiGlouton import OptiGlouton


class Fenetre:

    def __init__(self, tab_point):
        """
        :type tab_point: list[Point]
        :param tab_point: liste des points
        """
        self.fenetre = Tk()
        self.tab_point = tab_point
        self.color_arc = "red"
        self.stat = 0

    def afficher_tout(self, graphe: Graphes):
        settings = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        stats_global = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        canvas1 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        canvas2 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        canvas3 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        stat1 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        stat2 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        stat3 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)

        self.affiche_settings(settings)
        settings.grid(column=0, row=0)

        sommet_depart = np.random.randint(0, graphe.nb_point)

        graphe_glouton = Glouton(graphe, sommet_depart)
        self.affiche_glouton(graphe_glouton, canvas1)
        canvas1.grid(column=1, row=0)

        graphe_opti = OptiGlouton(graphe_glouton)
        self.affiche_opti(graphe_opti, canvas2)
        canvas2.grid(column=2, row=0)

        prim = Prim(graphe, sommet_depart)
        self.affiche_prim(prim, canvas3)
        canvas3.grid(column=3, row=0)


        self.create_stat(graphe, stat1)
        stat1.grid(column=0, row=1)
        self.fenetre.mainloop()

    def create_stat(self, graphe: Graphes, to_fill):
        to_fill.create_text(100, 100, text=graphe.poids_total)
        return to_fill

    def create_global_stats(self, to_fill):
        stat1 = Canvas(self.fenetre, height=320, width=320, borderwidth=3, relief=GROOVE)
        stat1.grid(column=0, row=1)
        stat1.create_text(100, 100, text="Longueur moyenne de glouton :")
        stat1.create_text(225, 100, text=self.stat.moy_lg)
        stat1.create_text(100, 120, text="Longueur moyenne de opti-glouton :")
        stat1.create_text(225, 120, text=self.stat.moy_lo)
        stat1.create_text(100, 140, text="Longueur moyenne de prim :")
        stat1.create_text(225, 140, text=self.stat.moy_lp)
        stat1.create_text(100, 160, text="Pourcentage d'amélioration glouton/opti-glou :")
        stat1.create_text(225, 160, text=self.stat.amelio_glou_opti)
        stat1.create_text(100, 180, text="Pourcentage d'amélioration opti-glou/prim :")
        stat1.create_text(225, 180, text=self.stat.amelio_opti_prim)
        return to_fill

    def affiche_glouton(self, graphe: Glouton, to_fill):
        tab_liaisons = graphe.sortie_glou
        for i in range(1, len(tab_liaisons)):
            if i == 1:
                to_fill.create_line(self.tab_point[tab_liaisons[i]].x * 300 + 10,
                                    self.tab_point[tab_liaisons[i]].y * 300 + 10,
                                    self.tab_point[tab_liaisons[i - 1]].x * 300 + 10,
                                    self.tab_point[tab_liaisons[i - 1]].y * 300 + 10, fill="red", width=3.0)
            else:
                to_fill.create_line(self.tab_point[tab_liaisons[i]].x * 300 + 10,
                                    self.tab_point[tab_liaisons[i]].y * 300 + 10,
                                    self.tab_point[tab_liaisons[i - 1]].x * 300 + 10,
                                    self.tab_point[tab_liaisons[i - 1]].y * 300 + 10, fill="black", width=3.0)
        self.placer_points(to_fill)
        return to_fill

    def affiche_prim(self, graphe: Prim, to_fill):
        for i in range(0, graphe.nb_point):
            for j in range(0, graphe.nb_point):
                if graphe.matrice_lien[i][j] == 1:
                    to_fill.create_line(self.tab_point[i].x * 300 + 10,
                                        self.tab_point[i].y * 300 + 10,
                                        self.tab_point[j].x * 300 + 10,
                                        self.tab_point[j].y * 300 + 10, fill="black", width=3.0)
        self.placer_points(to_fill)
        return to_fill

    def affiche_opti(self, graphe: OptiGlouton, to_fill):
        tab_liaisons = graphe.sortie_glou
        tab_opti = graphe.sortie_opti
        for i in range(1, len(tab_opti)):
            if i == 1:
                to_fill.create_line(self.tab_point[tab_opti[i]].x * 300 + 10,
                                    self.tab_point[tab_opti[i]].y * 300 + 10,
                                    self.tab_point[tab_opti[i - 1]].x * 300 + 10,
                                    self.tab_point[tab_opti[i - 1]].y * 300 + 10, fill="red", width=3.0)
            else:
                if tab_liaisons[i] != tab_opti[i]:
                    self.color_arc = "blue"
                else:
                    self.color_arc = "black"
                to_fill.create_line(self.tab_point[tab_opti[i]].x * 300 + 10,
                                    self.tab_point[tab_opti[i]].y * 300 + 10,
                                    self.tab_point[tab_opti[i - 1]].x * 300 + 10,
                                    self.tab_point[tab_opti[i - 1]].y * 300 + 10, fill=self.color_arc, width=3.0)
        self.placer_points(to_fill)
        return to_fill

    def placer_points(self, to_fill):
        for point in self.tab_point:
            to_fill.create_oval(point.x * 300 - 7 + 10, point.y * 300 - 7 + 10, point.x * 300 + 7 + 10,
                                point.y * 300 + 7 + 10, fill="black")
            to_fill.create_text(point.x * 300 + 10, point.y * 300 + 10, text=point.point_id, fill="white")

    def affiche_settings(self, to_fill):
        e1 = Entry(to_fill)
        e1.insert(0, 100)
        e2 = Entry(to_fill)
        e2.insert(0, 20)
        button1 = Button(to_fill, text="Lancer", command=lambda: self.lancer_graphes(e1.get(), e2.get(), to_fill))

        to_fill.create_text(100, 100, text="Nombre d'iterations :")
        to_fill.create_window(225, 100, window=e1)
        to_fill.create_text(100, 200, text="Nombre de points   :")
        to_fill.create_window(225, 200, window=e2)

        to_fill.create_window(160, 300, window=button1)
        return to_fill

    def lancer_graphes(self, nb_iterations, nb_points, to_fill):
        self.stat = Stats(nb_iterations, nb_points)
        self.create_global_stats(to_fill)
