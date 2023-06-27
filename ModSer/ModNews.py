###Nouveautés
###24/06/23
###16:17
###BaptisteH
###STJEANB

def News():
    
    import time
    from colorama import Fore, Style
    from ModSer import OsID
    from ModSer import ModLog
    
    ModLog.Log("--ModNews--\n")
    print("Chargement en cours depuis la Base de données")
    ModLog.Log("Chargement de cours des News\n")
    time.sleep(1)
    print("14 %")
    time.sleep(2)
    print("47 %")
    time.sleep(2)
    print("100 %")
    print("Chargement terminé !")
    
    print("")
    
    texte = "Nouveauté : mettez à jour votre version des Services depuis GitHub à partir du 29/06/2011"
    texte_colore = f"{Fore.BLUE}{texte}{Style.RESET_ALL}"
    
    print(texte_colore)
    
    print("")
    
    print("""1.20 (31/05/2023) : Ajout du système de Login au lancement
Ajout du service Autres Apps
Ajout d'interfaces graphiques

1.21 (29/06/2023) : Ajout du services News
Correction des bugs apportés par la version précédente
Ajout du système de notifications au lancement

1.22 / 1.23 / 1.24 (15/07/2023 - 30/08/23) : Ajout de la fonction utilisateur lambda (Un autre Launcher sera mis à disposition pendant la Mise à jour)
Ajout des Clients MC (accès via ModApps)
""")
    time.sleep(20)
    input("Appuyez sur entrée pour quitter")