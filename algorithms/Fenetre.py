from tkinter import *
from algorithms.Graphes import *

class Fenetre:

    def __init__(self, tab_point):
        """
        :type tab_point: list[Point]
        :param tab_point: liste des points
        """
        self.fenetre = Tk()
        self.fenetre.title("In Dubernard we trust")
        self.canvas = Canvas(self.fenetre, height=310, width=310)
        self.tab_point = tab_point
        self.color_arc = "red"

    def afficher_totale(self, mat):
        self.relier_arc_matrice(mat)
        #bouton = Button(self.fenetre, text="Appliquer opti", command=self.relier_arc_opti(tab_liaisons, Graphes.optimise_glou(tab_liaisons)))
        #bouton.pack()
        self.canvas.pack()
        self.fenetre.mainloop()

    def relier_arc(self, tab_liaisons):
        for i in range(1, len(tab_liaisons)):
            if i == 1:
                self.canvas.create_line(self.tab_point[tab_liaisons[i]].x * 300,
                                        self.tab_point[tab_liaisons[i]].y * 300,
                                        self.tab_point[tab_liaisons[i - 1]].x * 300,
                                        self.tab_point[tab_liaisons[i - 1]].y * 300, fill="red")
            else:
                self.canvas.create_line(self.tab_point[tab_liaisons[i]].x * 300,
                                        self.tab_point[tab_liaisons[i]].y * 300,
                                        self.tab_point[tab_liaisons[i - 1]].x * 300,
                                        self.tab_point[tab_liaisons[i - 1]].y * 300, fill="black")
        self.placer_points()

    def relier_arc_matrice(self, mat):
        for i in range(0, len(mat)):
            for j in range(0, len(mat)):
                if mat[i][j] == 1:
                    self.canvas.create_line(self.tab_point[i].x * 300,
                                            self.tab_point[i].y * 300,
                                            self.tab_point[j].x * 300,
                                            self.tab_point[j].y * 300, fill="black")
        self.placer_points()

    def relier_arc_opti(self, tab_liaisons, tab_opti):
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

    def placer_points(self):
        for point in self.tab_point:
            self.canvas.create_oval(point.x * 300 - 7, point.y * 300 - 7, point.x * 300 + 7, point.y * 300 + 7,
                                    fill="black")
            self.canvas.create_text(point.x * 300, point.y * 300, text=point.point_id, fill="white")
