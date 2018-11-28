from tkinter import *


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

        for point in tab_point:
            self.canvas.create_oval(point.x * 300 - 5, point.y * 300 - 5, point.x * 300 + 5, point.y * 300 + 5,
                                    fill="black")

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
        self.canvas.pack()
        self.fenetre.mainloop()
