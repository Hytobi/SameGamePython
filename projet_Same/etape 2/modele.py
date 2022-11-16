#projet algo
#Plouvin Patrice, Guevorte Flavien
#26/03/2018


#Import
from random import randint


#Début de la classe Case
class Case:
    ''' Classe qui modélise une bille du jeu Same'''
    
    def __init__(self,couleur,compo):
        '''Constructeur de la classe Case
           Arguments : self --- class --- Case
                       couleur --- int --- représente une couleur
                       compo --- int --- une composante
           Return : None'''
        #Initialisation
        self.__couleur = couleur
        self.__compo = compo

    def couleur(self):
        '''Méthode qui retourne la couleur de la bille
           Argument : self --- class --- Case
           Return : int --- la couleur'''
        return self.__couleur

    def change_couleur(self, entier):
        '''Méthode qui permet de changer la couleur de la bille
           grâce à un entier
           Arguments: self --- class --- Case
                      entier --- int --- choix de la couleur
           Return : None'''
        self.__couleur = entier
        self.__compo = -1

    def supprime(self):
        '''Méthode qui enlève la bille de la case
           Argument : self --- class --- Case
           Return : None'''
        self.__couleur = -1
        self.__compo = 0

    def est_vide(self):
        '''Méthode qui vérifie si une case est vide
           Argument: self --- class --- Case
           Return : bool'''
        return self.__couleur == -1

    def composante(self):
        '''Méthode qui retourne le numéro de la composante
           Argument : self --- class --- Case
           Return : int'''
        return self.__compo

    def pose_composante(self, entier):
        '''Méthode qui affecte entier comme numéro de composante pour la case.
           Arguments: self --- class --- Case
                      entier --- int --- choix de la composante
           Return : None'''
        self.__compo = entier

    def supprime_compo(self):
        '''Méthode qui enlève la composante pour la case (passe sa coueleur à -1)
           Argument : self --- class --- Case
           Return : None'''
        if self.est_vide():
            self.__compo = 0
        else :
            self.__compo = -1

    def parcourue(self):
        '''Méthode qui teste si la case a été affectée à un numéro de composante
           Argument : self --- class --- Case
           Retour : bool'''
        return self.__compo != -1

    #Ajout supplémentaire
    def __str__(self):
        '''Méthode qui permet d'afficher une bille (Pas dans l'énoncé)
           Argument : self --- class --- Case
           Retour : affiche une couleur'''
        return str(self.__couleur)

    ###Fin de la classe Case



#Debut class ModeleSame
class ModeleSame:
    '''Modèle pour le jeux'''

    def __init__(self, ligne=10, colonne=15, nb_couleur=3):
        '''Constructeur de la class ModeleSame.
           Arguments : self --- class --- ModeleSame
                       ligne --- int --- le nombre de ligne
                       colonne --- int --- le nombre de colonne
                       nb_couleur --- int --- le nombre de couleur
           Retour : None'''
        #Initialisation des arguments
        self.__lig = ligne
        self.__nbcol = colonne
        self.__nbcouleurs = nb_couleur

        #Attribut principale, matrice qui modèlise le plateau du jeu
        self.__mat = []
        for i in range(ligne):
            inter = []
            for j in range(colonne):
                inter.append(Case(randint(0,nb_couleur - 1),-1))
            self.__mat.append(inter)

        #Initialisation du score à 0
        self.__score = 0

        #Initialisation de la liste du nombre d’éléments de chaque composante
        #Le numéro de la composante est l'indice
        #Le nombre d'élément de la composante est associé à l'indice
        self.__nb_elts_compo = []

    def score(self):
        '''Méthode qui retourn le score du joueur.
           Argument : self -- class --- ModeleSame
           Retour : self.__score --- le score du joueur'''
        return self.__score

    def nblig(self):
        '''Méthode qui retourn le nombre de ligne de la matrice.
           Argument : self -- class --- ModeleSame
           Retour : self.__lig --- le nombre de ligne de la matrice'''
        return self.__lig

    def nbcol(self):
        '''Méthode qui retourn le nombre de colonne de la matrice.
           Argument : self -- class --- ModeleSame
           Retour : self.__nbcol --- le nombre de colonne de la matrice'''
        return self.__nbcol


    def nbcouleurs(self):
        '''Méthode qui retourn le nombre de couleurs.
           Argument : self -- class --- ModeleSame
           Retour : self.__nbcouleurs --- le nombre de couleurs'''
        return self.__nbcouleurs

    def coords_valides(self, i, j):
        '''Méthode qui retourne True si les coordonnées sont valides. False sinon.
           Arguments : self --- class --- ModeleSame
                       i --- int --- position ligne
                       j --- int --- position colonne
           Retour : Bool'''
        # 10 lignes implique que l'on va de 0 à 9 donc de 0 à self.__lig-1 par rapprot à l'initialisation par défaut
        # 15 colonnes implique que l'on va de 0 à 14 donc de 0 à self.__nbcol-1 par rapprot à l'initialisation par défaut
        return 0 <= i and i < self.__lig and 0 <= j and j < self.__nbcol

    def couleur(self, i, j):
        '''Méthode qui retourn la couleur en position (i,j)
           Arguments : self --- class --- ModeleSame
                       i --- int --- position ligne
                       j --- int --- position colonne
           Retour : int --- La couleur en pos (i,j)'''
        #Si i,j sont valides
        if self.coords_valides(i,j):
            return self.__mat[i][j].couleur()

    def supprime_bille(self, i, j):
        '''Méthode qui supprime la bille en position (i,j)
           Arguments : self --- class --- ModeleSame
                       i --- int --- position ligne
                       j --- int --- position colonne
           Retour : int --- La couleur en pos (i,j) prend la valeur -1'''
        #Si i,j sont valides
        if self.coords_valides(i,j):
            self.__mat[i][j].supprime()

    def nouvelle_partie(self):
        '''Méthode qui relance une partie.
           Argument : self -- class --- ModeleSame
           Retour : None'''
        #On parcourt la matrice self.__mat
        for i in range(self.__lig):
            for j in range(self.__nbcol):
                #Ecrase la valeur en position i,j
                self.__mat[i][j].change_couleur(randint(0,self.__nbcouleurs - 1))

    def composante(self, i, j):
        '''Méthode qui donne la valeur de la composante en position i,j.
           Argument : self -- class --- ModeleSame
           Retour : int --- la valeur de la composante'''
        return self.__mat[i][j].composante()

    def calcule_composantes(self):
        '''Méthode qui calcule chaque composante.
           Argument : self --- class --- ModeleSame
           Retour : None'''
        self.__nb_elts_compo.append(0)
        for i in range(self.__lig):
            for j in range(self.__nbcol):
                if not self.__mat[i][j].parcourue():
                    couleur = self.couleur(i, j)
                    num_compo = len(self.__nb_elts_compo)
                    nb_elts = self.calcule_composante_numero(i, j, num_compo, couleur)
                    self.__nb_elts_compo.append(nb_elts)
        
    def calcule_composante_numero(self, i, j, num_compo, couleur):
        '''Méthode récursive qui calcule une composante.
           Argument : self --- class --- ModeleSame
                      i --- int --- coordonnée de la ligne
                      j --- int --- coordonnée de la colonne
                      num_compo --- int --- numéro de la composante
                      couleur --- int --- couleur de la bille
           Retour : int --- nb de bille de la meme composante'''
        if not self.coords_valides(i,j) or self.__mat[i][j].parcourue() or self.couleur(i,j) != couleur:
            return 0
        self.__mat[i][j].pose_composante(num_compo)
        nb=0
        if (i > 0):
            nb += self.calcule_composante_numero(i-1,j,num_compo,couleur)
        if (i < self.nblig()-1):
            nb += self.calcule_composante_numero(i+1,j,num_compo,couleur)
        if (j > 0):
            nb += self.calcule_composante_numero(i,j-1,num_compo,couleur)
        if (j < self.nbcol()-1):
            nb += self.calcule_composante_numero(i,j+1,num_compo,couleur)
        return nb+1

    def recalc_composantes(self):
        '''Méthode qui recalcule les composantes.
           Argument : self --- class --- ModeleSame
           Retour : None'''
        for i in range(self.__lig):
            for j in range(self.__nbcol):
                self.__mat[i][j].supprime_compo()
        self.__nb_elts_compo = []
        self.calcule_composantes()

    def supprime_composante(self, num_compo):
        '''Méthode qui supprime une composante.
           Argument : self --- class --- ModeleSame
                      num_compo --- int --- numéro de la composante
           Retour : Bool'''
        n=0
        supprim = False
        for i in range(self.__lig):
            for j in range(self.__nbcol):
                if self.__mat[i][j].composante() == num_compo and self.__nb_elts_compo[num_compo]>=2 :
                    self.supprime_bille(i, j)
                    n+=1
                    supprim = True
        self.recalc_composantes()
        if supprim :
            self.__score += ((n-2)**2)
        return supprim

    #Ajout supplémentaire
    def __str__(self):
        '''Méthode qui affiche la matrice.
           Arguments : self --- class --- ModeleSame
           Retour : str'''
        return str(self.__mat)
            


#appel a la fonction principale
if __name__ == '__main__':
    print("Vous ne pouvez pas me lancer")
                             
