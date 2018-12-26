from tkinter import *
from matplotlib import *
from algorithms.Graphes import *


class Fenetre:

    def __init__(self, tab_point):
        """
        :type tab_point: list[Point]
        :param tab_point: liste des points
        """
        self.fenetre = Tk()
        self.fenetre.title("In Dubernard we trust")
        self.tab_point = tab_point
        self.color_arc = "red"

    # def init_ui(self):

    def afficher_totale(self, graphe : Graphes, tab_liaisons):
        canvas1 = Canvas(self.fenetre, height=310, width=310)
        canvas2 = Canvas(self.fenetre, height=310, width=310)
        stat1 = Canvas(self.fenetre, height=310, width=310)
        self.relier_arc(tab_liaisons, canvas1)
        self.relier_arc(tab_liaisons, canvas2)
        self.createStat(graphe, stat1)
        # bouton = Button(self.fenetre, text="Appliquer opti", command=self.relier_arc_opti(tab_liaisons,
        # Graphes.optimise_glou(tab_liaisons)))
        # bouton.pack()
        canvas1.grid(column=0, row=0)
        canvas2.grid(column=1, row=0)
        stat1.grid(column=0, row=1)
        self.fenetre.mainloop()

    def createStat(self, graphe : Graphes, to_fill):
        to_fill.create_text(100, 100, text=graphe.poids_total)
        return to_fill

    def relier_arc(self, tab_liaisons, to_fill):
        for i in range(1, len(tab_liaisons)):
            if i == 1:
                to_fill.create_line(self.tab_point[tab_liaisons[i]].x * 300,
                                    self.tab_point[tab_liaisons[i]].y * 300,
                                    self.tab_point[tab_liaisons[i - 1]].x * 300,
                                    self.tab_point[tab_liaisons[i - 1]].y * 300, fill="red")
            else:
                to_fill.create_line(self.tab_point[tab_liaisons[i]].x * 300,
                                    self.tab_point[tab_liaisons[i]].y * 300,
                                    self.tab_point[tab_liaisons[i - 1]].x * 300,
                                    self.tab_point[tab_liaisons[i - 1]].y * 300, fill="black")
        self.placer_points(to_fill)
        return to_fill

    '''def relier_arc_opti(self, tab_liaisons, tab_opti):
        for i in range(1, len(tab_opti)):
            if i == 1:
                self.canvas.create_line(self.tab_point[tab_opti[i]].x * 300,
                                        self.tab_point[tab_opti[i]].y * 300,
                                        self.tab_point[tab_opti[i - 1]].x * 300,
                                        self.tab_point[tab_opti[i - 1]].y * 300, fill="red")
            else:
                if tab_liaisons[i] != tab_opti[i]:
                    self.color_arc = "blue"
                else:
                    self.color_arc = "black"
                self.canvas.create_line(self.tab_point[tab_opti[i]].x * 300,
                                        self.tab_point[tab_opti[i]].y * 300,
                                        self.tab_point[tab_opti[i - 1]].x * 300,
                                        self.tab_point[tab_opti[i - 1]].y * 300, fill=self.color_arc)
        self.placer_points()
        self.canvas.pack()
        self.fenetre.mainloop()
    '''

    def placer_points(self, to_fill):
        for point in self.tab_point:
            to_fill.create_oval(point.x * 300 - 7, point.y * 300 - 7, point.x * 300 + 7, point.y * 300 + 7,
                                fill="black")
            to_fill.create_text(point.x * 300, point.y * 300, text=point.point_id, fill="white")
