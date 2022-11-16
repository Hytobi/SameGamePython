#Projet Algo
#Plouvin Patrice, Guevorte Flavien
#26/03/2018


#Import
import tkinter
import modele

#Debut class VueSame
class VueSame :
    '''Class qui modèlise le Same game sur tkinter'''

    def __init__(self, same):
        '''Méthode qui initialise la class VueSame.
           Arguments : self --- class --- VueSame
                       same --- instance --- instance du ModeleSame
           Retour : None'''
        #Attribut same
        self.__same = same
        self.__same = modele.ModeleSame()
        
        #Créer la fenêtre principale et le titre
        fenetre = tkinter.Tk()
        fenetre.title("Same Game")
        
        #Initialisation des images
        self.__images = []
        for i in range(1, 9):
            img = tkinter.PhotoImage(file = "./img/medium_sphere"+str(i)+".gif")
            self.__images.append(img)
        self.__images.append(tkinter.PhotoImage(file = "./img/medium_spherevide.gif"))
        
        #Matrice de Button, un Button représente une bille
        self.__les_btns =[]
        for i in range(self.__same.nblig()):
            inter = []
            for j in range(self.__same.nbcol()) :
                inter.append(tkinter.Button(fenetre, image=self.__images[self.__same.couleur(i,j)]))
                inter[j]["command"] = self.creer_controleur_btn(i,j)
                inter[j].grid(row=i,column=j)
            self.__les_btns.append(inter)

        #Le boutton Nouveau
        btn_new = tkinter.Button(fenetre, text="Nouveau", command = self.nouvelle_partie) 
        btn_new.grid(row=round(same.nblig()/2)-1, column=same.nbcol()+1)
        
        #Le boutton Quitter
        btn_quitter = tkinter.Button(fenetre, text="Quitter", command = fenetre.destroy) 
        btn_quitter.grid(row=round(self.__same.nblig()/2), column=self.__same.nbcol()+1)

        #Boucle d'écoute des événements
        fenetre.mainloop()

    def redessine(self):
        '''Méthode qui parcourt les boutons pour mettre à jour.
           Argument : self --- class --- VueSame
           Retour : None'''
        for i in range(self.__same.nblig()):
            for j in range(self.__same.nbcol()) :
                self.__les_btns[i][j]['image'] = self.__images[self.__same.couleur(i,j)]
        
    def nouvelle_partie(self):
        '''Méthode qui change les lettres aléatoirement.
           Argument : self --- class --- VueSame
           Retour : None'''
        self.__same.nouvelle_partie()
        self.redessine()

    def creer_controleur_btn(self,i,j):
        '''Méthode qui supprime une bille grace à une fonction.
           Arguments : self --- class --- VueSame
                       i --- int --- coordonnée de la ligne
                       j --- int --- coordonnée de la colonne
           Retour : une fonction'''
        def controleur_btn():
            '''Fonction qui supprime une bille.
               Argument : None
               Retour : None '''
            self.__same.calcule_composantes()
            self.__same.supprime_composante(self.__same.composante(i,j))
            self.redessine()
        return controleur_btn    
            


if __name__ == '__main__' :
    # création du modèle
    same = modele.ModeleSame()
    # création de la vue qui créé les contrôleurs
    # et lance la boucle d’écoute des évts
    vue = VueSame(same)


    
