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

personne1 = Personne("Doe", "Jane")
personne1.setNom("Dos")
personne1.SePresenter()
print(personne1.getPrenom())

personne2 = Personne("Clooney", "Georges")
personne2.setNom("Clown")
personne2.SePresenter()
print(personne2.getPrenom())