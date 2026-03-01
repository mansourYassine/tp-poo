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
        self.listeProduits = []
    
    def ajouter_produit(self, produit, quantite=1):
        if quantite >= 1:
            is_existe = False
            for elm in self.listeProduits:
                if elm[0] == produit:
                    elm[1] += quantite
                    is_existe = True
            if is_existe == False:
                self.listeProduits.append([produit, quantite])
    
    def calculer_total(self):
        prix_total = 0
        for elm in self.listeProduits:
            prix_total += elm[0].prix * elm[1]

        return prix_total

    def afficher_details(self):
        print(f"Commande N°{self.num_commande}:")
        for elm in self.listeProduits:
            print(f"{elm[0].nom} : {elm[1]}")
        print(f"Prix Total: {self.calculer_total()}")
        print("================")

class CommandeExpress(Commande):
    def calculer_total(self):
        frais_livraison = 15
        return super().calculer_total() + frais_livraison
    
    def afficher_details(self):
        print("Commande express ", end="")
        super().afficher_details()


if __name__ == "__main__":
    p1 = Produit("Genova", 3)
    p2 = Produit("Merandina", 20)
    p3 = Produit("Tonic", 1)
    p4 = Produit("Chocop", 2)

    c1 = Commande()
    c1.ajouter_produit(p1, 50)
    c1.ajouter_produit(p2, 5)
    c1.ajouter_produit(p3)
    c1.ajouter_produit(p3, 20)
    c1.ajouter_produit(p2, 10)
    c1.ajouter_produit(p4, 4)
    c1.ajouter_produit(p4, 2)
    c1.afficher_details()

    c2 = CommandeExpress()
    c2.ajouter_produit(p1, 50)
    c2.ajouter_produit(p2, 5)
    c2.ajouter_produit(p3)
    c2.afficher_details()
