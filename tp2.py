class CompteBancaire:
    taux_interet = 0.03
    def __init__(self, nom, solde):
        self.nom_client = nom
        self.solde = solde
    
    @classmethod
    def modifier_taux(cls, nouveau_taux):
        if nouveau_taux >= 0:
            cls.taux_interet = nouveau_taux
        
    def afficher_info(self):
        print(self.nom_client, self.solde)
    
    @staticmethod
    def valider_montant(montant):
        if montant >= 0:
            return True
        else:
            return False
    
    @classmethod
    def calculer_interets(cls, montant, annee):
        interet = montant * (((1 + cls.taux_interet) ** annee)-1)
        return interet