import personne as file
Personne = file.Personne

class Auteur(Personne):
    def __init__(self, nom,prenom, oeuvre):
        super().__init__(nom,prenom,)
        self.oeuvre = oeuvre
    def listerOeuvre(self):
        for i in range(len(self.oeuvre)):
            print("Oeuvre de l'auteur : {} ".format(self.oeuvre[i]))

    def ecrireUnLivre(self, titre):
        self.oeuvre.append(titre)
        print("L'auteur a écrit un nouveau livre : {} ".format(titre))

    
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = Auteur(auteur.nom,auteur.prenom, auteur.oeuvre)
    
    def print(self):
        print("Le titre du livre est : ", self.titre)

livre1 = Livre("Le seigneur des anneaux", Auteur("Tolkien", "John Ronald Reuel", ["Le seigneur des anneaux", "Le hobbit"]))

livre1.print()
livre1.auteur.listerOeuvre()
livre1.auteur.ecrireUnLivre("Le silmarillion")
print("___________________")
livre1.auteur.listerOeuvre()
