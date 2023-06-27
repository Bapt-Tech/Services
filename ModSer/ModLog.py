import os
def Log(Contenu):
        sous_dossier = "Log"
        nom_fichier = "Logs.txt"
        contenu = Contenu
        enregistrer_fichier(sous_dossier, nom_fichier, contenu)

def enregistrer_fichier(sous_dossier, nom_fichier, contenu):
    chemin_sous_dossier = os.path.join(os.getcwd(), sous_dossier)  # Chemin absolu du sous-dossier
    if not os.path.exists(chemin_sous_dossier):
        os.makedirs(chemin_sous_dossier)  # Créer le sous-dossier s'il n'existe pas déjà
    
    chemin_fichier = os.path.join(chemin_sous_dossier, nom_fichier)  # Chemin absolu du fichier
    with open(chemin_fichier, 'a') as fichier:
        fichier.write(contenu)
        fichier.close
    
    #print("Fichier enregistré avec succès dans le sous-dossier :", sous_dossier)