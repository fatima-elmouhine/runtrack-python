import classTools as file 
Personne = file.Personne
Auteur = file.Auteur

class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = {}

    def inventaire(self):
        print(f"Les livres en possession de {self.prenom} {self.nom} sont :")
        for livre, quantite in self.collection.items():
            print(f"{livre} ({quantite})")

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        
        if titre in auteur.oeuvre:
            if titre in self.catalogue:
                self.catalogue[titre] += quantite
            else:
                self.catalogue[titre] = quantite
            print(f"x{quantite} - '{titre}' a/ont été ajouté(s) au catalogue.")
        else:
            print(f"Le livre '{titre}' n'est pas été écrit par {auteur.prenom} {auteur.nom}.")

    def inventaire(self):
        print(f"Inventaire bibliothèque {self.nom} :")
        for livre, quantite in self.catalogue.items():
            print(f"{livre} - x{quantite}")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            if titre in client.collection:
                client.collection[titre] += 1
            else:
                client.collection[titre] = 1
            self.catalogue[titre] -= 1
            print(f"{client.prenom} {client.nom} a emprunté le livre '{titre}'.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible dans la bibliothèque.")

    def rendreLivres(self, client):
        for livre, quantite in client.collection.items():
            if livre in self.catalogue:
                self.catalogue[livre] += quantite
            else:
                self.catalogue[livre] = quantite
        client.collection.clear()
        print(f"{client.prenom} {client.nom} a rendu tous ses livres.")

print("__"*10 + " PARTIE AUTEUR " + "__"*10)
auteur1 = Auteur("Mahmoud", "Jean")
auteur2 = Auteur("Zak", "Bal")
auteur1.ecrireUnLivre("Les Misérables le retour")
auteur2.ecrireUnLivre("Illusions perdues 2 : la revanche des illusions")

print("__"*10 + " PARTIE BIBLIOTHEQUE " + "__"*10)

bibliotheque1 = Bibliotheque("Merlan")
bibliotheque2 = Bibliotheque("Alcazar")
bibliotheque1.acheterLivre(auteur1, "Les Misérables le retour", 5)
bibliotheque2.acheterLivre(auteur2, "Illusions perdues 2 : la revanche des illusions", 3)
bibliotheque1.acheterLivre(auteur1, "Les Misérables le retour", 5)
bibliotheque1.inventaire()
bibliotheque2.inventaire()

print("__"*10 + " PARTIE CLIENT " + "__"*10)
client1 = Client("Doe", "Jane")
bibliotheque1.louer(client1, "Les Misérables le retour")
bibliotheque2.louer(client1, "Illusions perdues 2 : la revanche des illusions")
client1.inventaire()
bibliotheque1.rendreLivres(client1)
