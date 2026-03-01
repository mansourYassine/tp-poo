class Employe:
    salaire_base = 3000
    def __init__(self, nom, poste):
        self.nom = nom
        self.poste = poste
    
    @staticmethod
    def calculer_prime(poste):
        if poste == "Manager":
            return 500
        elif poste == "Développeur":
            return 300
        else:
            return 200
    
    def calcul_salaire(self):
        salaire = Employe.salaire_base + Employe.calculer_prime(self.poste)
        return salaire
    