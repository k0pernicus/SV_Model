class Reaction (object):
    """docstring for Reaction """

    def __init__(self, entree, sortie, vitesse):

        super(Reaction, self).__init__()
        self.entree = entree
        self.sortie = sortie
        self.vitesse = vitesse

    def get_entree(self):
        return self.entree

    def get_sortie(self):
        return self.sortie

    def get_vitesse(self):
        return self.vitesse
