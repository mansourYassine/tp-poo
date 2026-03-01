from abc import ABC, abstractmethod
class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite
    
    @property
    def produit(self):
        return self.__produit
    @produit.setter
    def produit(self, nvproduit):
        self.__produit = nvproduit
    
    @property
    def quantite(self):
        return self.__quantite
    @quantite.setter
    def quantite(self, nvquantite):
        if nvquantite >= 0:
            self.__quantite = nvquantite
    
class Produit(ABC):
    def __init__(self, code, nom):
        self.__code = code
        self.__nom = nom
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def code(self):
        return self.__code
    
    @abstractmethod
    def getPrixHT(self):
        pass

class Produit_Elementaire(Produit):
    def __init__(self, code, nom, prixAchat):
        super().__init__(code, nom)
        self.__prixAchat = prixAchat
    
    @property
    def prixAchat(self):
        return self.__prixAchat
    
    def __str__(self):
        return f"Code: {self.code} | Nom: {self.nom} | Prix d'achat: {self.prixAchat}"
    
    def getPrixHT(self):
        return self.prixAchat

class Produit_Compose(Produit):
    tauxTVA = 0.18
    def __init__(self, code, nom, fraisFabrication):
        super().__init__(code, nom)
        self.__fraisFabrication = fraisFabrication
        self.__listeCompositions = []
    
    @property
    def fraisFabrication(self):
        return self.__fraisFabrication
    
    @property
    def listeCompositions(self):
        return self.__listeCompositions
    
    def __str__(self):
        str = f"Code: {self.code} | Nom: {self.nom} | Frais de fabrication: {self.fraisFabrication}\n"
        str += "Sa composition: \n"
        for composante in self.listeCompositions:
            str += f"{composante.produit} | Quantite utilisé : {composante.quantite}\n"
        
        return str
    
    def ajouteCompositions(self, *composantes : Composition):
        for comp in composantes:
            self.listeCompositions.append(comp)
    
    def getPrixHT(self):
        prixHT = self.fraisFabrication
        for composante in self.listeCompositions:
            prixHT += composante.produit.getPrixHT() * composante.quantite
        
        return prixHT

if __name__ == "__main__":
    pe1 = Produit_Elementaire("PE001", "Brique", 2.50)
    pe2 = Produit_Elementaire("PE002", "Ciment", 6.80)
    pe3 = Produit_Elementaire("PE003", "Planche en bois", 12)
    pe4 = Produit_Elementaire("PE004", "Lot de vis", 3.20)
    pe5 = Produit_Elementaire("PE005", "Pot de peinture", 25)

    # pc1 = Produit_Compose("PC001", "Mur Standard", 150)
    # pc1.ajouteCompositions(Composition(pe1, 100), Composition(pe2, 10))
    # print(pc1)
    # print(pc1.getPrixHT())

    pc2 = Produit_Compose("PC002", "Table en Bois", 40)
    pc2.ajouteCompositions(Composition(pe3, 5), Composition(pe4, 2))
    print(pc2)
    print(f"Le prix de produit est: {pc2.getPrixHT()}")

    # pc3 = Produit_Compose("PC003", "Chambre Peinte", 100)
    # pc4 = Produit_Compose("PC004", "Petit Abri", 250)

    
