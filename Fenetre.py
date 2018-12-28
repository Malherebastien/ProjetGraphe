from tkinter import *

from Stats import *

from algorithms.Prim import *
from algorithms.Glouton import *
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
        nb_iterations = IntVar()
        nb_points = IntVar()
        label1 = Label(to_fill, text="Nombre d'itérations", textvariable=nb_iterations)
        label2 = Label(to_fill, text="Nombre de points", textvariable=nb_points)
        button1 = Button(to_fill, text="Lancer", command=self.lancer_graphes(nb_iterations, nb_points))
        return to_fill

    def lancer_graphes(self, nb_iterations, nb_points):
            stat = Stats(nb_iterations, nb_points)
