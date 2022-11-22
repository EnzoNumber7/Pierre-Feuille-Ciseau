from tkinter import *
 
class Morpion(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Morpion")
         
        self.label_j1 = Label(self, text="Joueur 1", bg = "green")
        self.label_j2 = Label(self, text="Joueur 2")
        self.label_j1.pack(padx =20, side =LEFT)
        self.label_j2.pack(padx =20, side =RIGHT)
         
        self.can = Canvas(self, width = 300, height = 300, bg = "ivory", bd =1, relief =SUNKEN)
        self.can.pack(padx = 5, pady = 5)
        self.tracer_plateau()
         
        self.bind("<Button-1>", self.analyser_position_clic)
         
        self.b1 = Button(self, text='Recommencer', command=self.recommencer)
        self.b1.pack(pady = 5)
         
        self.grille = [0] * 9
        self.joueur = 1
         
    def tracer_plateau(self):
        self.can.create_line(105, 10, 105, 290, width = 10)
        self.can.create_line(205, 10, 205, 290, width = 10)
        self.can.create_line(10, 105, 290, 105, width = 10)
        self.can.create_line(10, 205, 290, 205, width = 10)
     
    def recommencer(self):
        self.can.delete(ALL)
        self.tracer_plateau()
        self.grille = [0] * 9
         
    def tracer_croix(self, x, y):
        self.can.create_line(x-35, y-35, x+35, y+35, width = 5, fill = "blue")
        self.can.create_line(x-35, y+35, x+35, y-35, width = 5, fill = "blue")
 
    def tracer_rond(self, x, y):
        self.can.create_oval(x - 35, y - 35, x + 35, y + 35, fill = "red")
        self.can.create_oval(x - 30, y - 30, x+30, y+30, fill = "ivory")
     
    def alterner_joueurs(self):
        if self.joueur == 1:
            self.joueur = 2
        else:
            self.joueur = 1
         
    def analyser_position_clic(self, event):
        #Detection de la position de la souris dans le Canvas en fonction des cases
        # 0 | 1 | 2
        # - + - + -
        # 3 | 4 | 5
        # - + - + -
        # 6 | 7 | 8
         
         
        if event.x > 0 and event.x < 100:
            if event.y > 0 and event.y < 100:
                i = 0
                self.grille[i] = self.joueur
                self.x = 55
                self.y = 55
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
            if event.y > 100 and event.y < 200:
                i = 3
                self.grille[i] = self.joueur
                self.x = 55
                self.y = 155
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
            if event.y > 200 and event.y < 300:
                i = 6
                self.grille[i] = self.joueur
                self.x = 55
                self.y = 255
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
        elif event.x > 100 and event.x < 200:
            if event.y > 0 and event.y < 100:
                i = 1
                self.grille[i] = self.joueur
                self.x = 155
                self.y = 55
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
            if event.y > 100 and event.y < 200:
                i = 4
                self.grille[i] = self.joueur
                self.x = 155
                self.y = 155
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
            if event.y > 200 and event.y < 300:
                i = 7
                self.grille[i] = self.joueur
                self.x = 155
                self.y = 255
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
        elif event.x > 200 and event.x < 300:
            if event.y > 0 and event.y < 100:
                i = 2
                self.grille[i] = self.joueur
                self.x = 255
                self.y = 55
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
            if event.y > 100 and event.y < 200:
                i = 5
                self.grille[i] = self.joueur
                self.x = 255
                self.y = 155
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
            if event.y > 200 and event.y < 300:
                i = 8
                self.grille[i] = self.joueur
                self.x = 255
                self.y = 255
                if self.joueur == 1:
                    self.tracer_croix(self.x, self.y)
                else:
                    self.tracer_rond(self.x, self.y)
                self.alterner_joueurs()
 
if __name__ == "__main__":
    fenetre = Morpion()
    fenetre.resizable(width=False, height=False)
     
    fenetre.mainloop()