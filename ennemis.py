


class Ennemis:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400,400)
        self.taille = 10
        self.couleur = (255,0,0)
        self.masse = 10
        self.vel = Vector2(0,0)
        self.maxAcc = 300
        self.maxVel = 440
        self.count = 0