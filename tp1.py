class Produit:
    nbre_produits = 0
    def __init__(self, reference, designation, prix_achat, prix_vente):
        self.reference = reference
        self.designation = designation
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.nbre_exemplaires = 0
        Produit.nbre_produits += 1

    def get_nbre_produits(self):
        return Produit.nbre_produits
    
    def afficher_informations(self):
        print(
            f"Reference: {self.reference} - Designation: {self.designation} - Prix d'achat: {self.prix_achat} - Prix de vente: {self.prix_vente} - Nombres d'exemplaires: {self.nbre_exemplaires}")

    def set_prix_achat(self, nouveau_prix):
        if nouveau_prix > 0:
            self.prix_achat = nouveau_prix
    
    def set_prix_vente(self, nouveau_prix):
        if nouveau_prix > 0:
            self.prix_vente = nouveau_prix
    
    def augmente_nbre_exemplaires(self, qte):
        self.nbre_exemplaires += qte

    def diminue_nbre_exemplaires(self, qte):
        if self.nbre_exemplaires >= qte:
            self.nbre_exemplaires -= qte

class Commande:
    def __init__(self, date_creation):
        self.date_creation = date_creation
        self.lignes_commande = []
    
    def ajouter_ligne_commande(self, ligne_commande:LigneCommande):
        self.lignes_commande.append(ligne_commande)

class LigneCommande:
    def __init__(self, produit:Produit, qte_livre):
        self.produit = produit
        self.qte_livre = qte_livre
        # Diminuer la quantite livre de la quatite de produit
        produit.diminue_nbre_exemplaires(qte_livre)
    
    def get_produit(self):
        return self.produit
    
    def get_qte_livre(self):
        return self.qte_livre

if "__main__" == __name__:
    
    # Cree des produits
    p1 = Produit("A758", "Shampoo", 150, 250)
    p2 = Produit("B785", "Savon", 100, 150)
    p3 = Produit("C485", "Smartphone", 1000, 2500)

    p1.afficher_informations()
    p2.afficher_informations()
    p3.afficher_informations()

    p1.augmente_nbre_exemplaires(200)
    p2.augmente_nbre_exemplaires(500)
    p3.augmente_nbre_exemplaires(800)

    # Cree des lignes de commandes
    l1 = LigneCommande(p1, 30)
    l2 = LigneCommande(p2, 120)
    l3 = LigneCommande(p3, 340)

    # Cree une commande
    c1 = Commande("10/01/2026")
    c1.ajouter_ligne_commande(l1)
    c1.ajouter_ligne_commande(l2)
    c1.ajouter_ligne_commande(l3)

    print(p3.nbre_exemplaires)

