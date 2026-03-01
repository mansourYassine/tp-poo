class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nvnom):
        self.__nom = nvnom

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, nvprix):
        self.__prix = nvprix
    
    def afficher_details(self):
        return f"Nom: {self.nom}, Prix: {self.prix}"
    
    # def __str__(self):
    #     return self.afficher_details()
    
class Commande:
    nbre_commande = 0
    def __init__(self, statut = "en attente"):
        Commande.nbre_commande += 1
        self.num_commande = Commande.nbre_commande
        self.statut = statut
        self.produits = []
    
    def ajouter_produit(self, produit, quantite=1):
        if quantite == 1:
            self.produits.append((produit, 1))
        elif quantite >= 0 and quantite != 1:
            self.produits.append((produit, quantite))
        else:
            print("Error")
    
    def calculer_total(self):
        prix_total = 0
        for produit in self.produits:
            prix_total += produit[0].prix * produit[1]
        
        return prix_total

    def afficher_details(self):
        for produit in self.produits:
            print(f"{produit[0].afficher_details()}, Quantity: {produit[1]}")

class CommandeExpress(Commande):
    def calculer_total(self):
        frais_livraison = 15
        return super().calculer_total() + frais_livraison
    
    def afficher_details(self):
        print("Une commande express:")
        super().afficher_details()
    
if __name__ == "__main__":
    p1 = Produit("Genova", 3)
    p2 = Produit("Merandina", 20)
    p3 = Produit("Tonic", 1)

    c1 = Commande()
    c1.ajouter_produit(p1, 50)
    c1.ajouter_produit(p2, 5)
    c1.ajouter_produit(p3)

    c1.afficher_details()
    print(f"Le prix Total de commande: {c1.calculer_total()}")

    c2 = CommandeExpress()
    c2.ajouter_produit(p1, 50)
    c2.ajouter_produit(p2, 5)
    c2.ajouter_produit(p3)
    c2.afficher_details()
    print(f"Le prix Total de commande: {c2.calculer_total()}")