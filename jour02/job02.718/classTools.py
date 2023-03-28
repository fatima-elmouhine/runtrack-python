class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print("Je m'appelle", self.prenom, self.nom)
        
    def getNom(self):
        return self.nom
    
    def setNom(self, nom):
        self.nom = nom
        
    def getPrenom(self):
        return self.prenom
    
    def setPrenom(self, prenom):
        self.prenom = prenom

class Auteur(Personne):
    def __init__(self, nom,prenom):
        super().__init__(nom,prenom,)
        self.oeuvre = []
    def listerOeuvre(self):
        for i in range(len(self.oeuvre)):
            print("Oeuvre de l'auteur : {} ".format(self.oeuvre[i]))

    def ecrireUnLivre(self, titre):
        self.oeuvre.append(titre)
        print("L'auteur {} {} a écrit un nouveau livre : {} ".format(self.prenom, self.nom, titre))

    
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = Auteur(auteur.nom,auteur.prenom, auteur.oeuvre)
    
    def print(self):
        print("Le titre du livre est : ", self.titre)
