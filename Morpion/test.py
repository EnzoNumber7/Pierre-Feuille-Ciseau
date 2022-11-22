from tkinter import *
from tkinter import ttk

#création grille
class Morpion(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Plateau ")
 
        self.can = Canvas(self, width = 420, height = 420)
        self.can.pack()
        self.tracer_plateau()
        self.croix_image = PhotoImage(file='Morpion\img\croix.png')
        self.cercle_image = PhotoImage(file='Morpion\img\cercle.png')
        self.croixWin_image = PhotoImage(file='Morpion\img\croix_win.png')
        self.cercleWin_image = PhotoImage(file='Morpion\img\cercle_win.png')

        self.bind("<Button>", self.analyser_position_clic)
        self.plateau = [0] * 10
        self.joueur = 1
 
    def changement_de_joueurs(self):
        if self.joueur == 1: 
            self.joueur = 2
        else:
            self.joueur = 1
 
    def tracer_plateau(self):
        self.can.create_line(140, 20, 140, 400, width = 4)
        self.can.create_line(280, 20, 280, 400, width = 4)
        self.can.create_line(20, 140, 400, 140, width = 4)
        self.can.create_line(20, 280, 400, 280, width = 4)

    def tracer_croix(self, x, y):
        self.can.create_image(x,y,image=self.croix_image)
 
    def tracer_rond(self, x, y):
        self.can.create_image(x,y,image=self.cercle_image)


    
    def analyser_position_clic(self, event):
        #Detection de la position de la souris dans le Canvas en fonction des cases
        # 1 | 2 | 3
        # - + - + -
        # 4 | 5 | 6
        # - + - + -
        # 7 | 8 | 9 
 
        if self.plateau[0] == 0:
            if event.x > 20 and event.x < 140:
                if event.y > 20 and event.y < 140:
                    i = 1
                    self.x = 70
                    self.y = 70
                if event.y > 140 and event.y < 280:
                    i = 4
                    self.x = 70
                    self.y = 210
                if event.y > 280 and event.y < 400:
                    i = 7
                    self.x = 70
                    self.y = 350
            elif event.x > 140 and event.x < 280:
                if event.y > 20 and event.y < 140:
                    i = 2
                    self.x = 210
                    self.y = 70
                if event.y > 140 and event.y < 280:
                    i = 5
                    self.x = 210
                    self.y = 210
                if event.y > 280 and event.y < 400:
                    i = 8
                    self.x = 210
                    self.y = 350
            elif event.x > 280 and event.x < 400:
                if event.y > 20 and event.y < 140:
                    i = 3
                    self.x = 350
                    self.y = 70
                if event.y > 140 and event.y < 280:
                    i = 6
                    self.x = 350
                    self.y = 210
                if event.y > 280 and event.y < 400:
                    i = 9
                    self.x = 350
                    self.y = 350
 
        if self.plateau[i] == 0:
            if self.joueur == 1:
                self.plateau[i] = "✖"
                self.tracer_croix(self.x, self.y)
                self.test_gagnant("✖")
            else:
                self.plateau[i] = "⭘"
                self.tracer_rond(self.x, self.y)
                self.test_gagnant("⭘")
            self.changement_de_joueurs()

    def test_gagnant(self,symbole):
        if self.plateau[1] == self.plateau[2] == self.plateau[3] == symbole and self.plateau[1]!= 0:
            if symbole == "✖":
                self.can.create_image(70,70,image=self.croixWin_image)
                self.can.create_image(210,70,image=self.croixWin_image)
                self.can.create_image(350,70,image=self.croixWin_image)
            else:
                self.can.create_image(70,70,image=self.cercleWin_image)
                self.can.create_image(210,70,image=self.cercleWin_image)
                self.can.create_image(350,70,image=self.cercleWin_image)
 
        elif self.plateau[4] == self.plateau[5] == self.plateau[6] == symbole and self.plateau[4]!= 0:
            if symbole == "✖":
                self.can.create_image(70,210,image=self.croixWin_image)
                self.can.create_image(210,210,image=self.croixWin_image)
                self.can.create_image(350,210,image=self.croixWin_image)
            else:
                self.can.create_image(70,210,image=self.cercleWin_image)
                self.can.create_image(210,210,image=self.cercleWin_image)
                self.can.create_image(350,210,image=self.cercleWin_image)

        elif self.plateau[7] == self.plateau[8] == self.plateau[9] == symbole and self.plateau[7]!= 0:
            if symbole == "✖":
                self.can.create_image(70,350,image=self.croixWin_image)
                self.can.create_image(210,350,image=self.croixWin_image)
                self.can.create_image(350,350,image=self.croixWin_image)
            else:
                self.can.create_image(70,350,image=self.cercleWin_image)
                self.can.create_image(210,350,image=self.cercleWin_image)
                self.can.create_image(350,350,image=self.cercleWin_image)

        elif self.plateau[1] == self.plateau[5] == self.plateau[9] == symbole and self.plateau[1]!= 0:
            if symbole == "✖":
                self.can.create_image(70,70,image=self.croixWin_image)
                self.can.create_image(210,210,image=self.croixWin_image)
                self.can.create_image(350,350,image=self.croixWin_image)
            else:
                self.can.create_image(70,70,image=self.cercleWin_image)
                self.can.create_image(210,210,image=self.cercleWin_image)
                self.can.create_image(350,350,image=self.cercleWin_image)

        elif self.plateau[3] == self.plateau[5] == self.plateau[7] == symbole and self.plateau[3]!= 0:
            if symbole == "✖":
                self.can.create_image(70,350,image=self.croixWin_image)
                self.can.create_image(210,210,image=self.croixWin_image)
                self.can.create_image(350,70,image=self.croixWin_image)
            else:
                self.can.create_image(70,350,image=self.cercleWin_image)
                self.can.create_image(210,210,image=self.cercleWin_image)
                self.can.create_image(350,70,image=self.cercleWin_image)

        elif self.plateau[1] == self.plateau[4] == self.plateau[7] == symbole and self.plateau[1]!= 0:
            if symbole == "✖":
                self.can.create_image(70,70,image=self.croixWin_image)
                self.can.create_image(70,210,image=self.croixWin_image)
                self.can.create_image(70,350,image=self.croixWin_image)
            else:
                self.can.create_image(70,70,image=self.cercleWin_image)
                self.can.create_image(70,210,image=self.cercleWin_image)
                self.can.create_image(70,350,image=self.cercleWin_image)

        elif self.plateau[2] == self.plateau[5] == self.plateau[8] == symbole and self.plateau[2]!= 0:
            if symbole == "✖":
                self.can.create_image(210,70,image=self.croixWin_image)
                self.can.create_image(210,210,image=self.croixWin_image)
                self.can.create_image(210,350,image=self.croixWin_image)
            else:
                self.can.create_image(210,70,image=self.cercleWin_image)
                self.can.create_image(210,210,image=self.cercleWin_image)
                self.can.create_image(210,350,image=self.cercleWin_image)

        elif self.plateau[3] == self.plateau[6] == self.plateau[9] == symbole and self.plateau[3]!= 0:
            if symbole == "✖":
                self.can.create_image(350,70,image=self.croixWin_image)
                self.can.create_image(350,210,image=self.croixWin_image)
                self.can.create_image(350,350,image=self.croixWin_image)
            else:
                self.can.create_image(350,70,image=self.cercleWin_image)
                self.can.create_image(350,210,image=self.cercleWin_image)
                self.can.create_image(350,350,image=self.cercleWin_image)

 

if __name__ == "__main__":
    fenetre = Morpion()
fenetre.mainloop()