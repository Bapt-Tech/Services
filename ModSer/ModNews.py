###Nouveautés
###24/06/23
###16:17
###BaptisteH
###STJEANB

def News():
    
    import time
    import colorama
    from colorama import Fore, Style, Back
    from ModSer import OsID
    from ModSer import ModLog

    colorama.init(autoreset=True)
    
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
    
    print(Back.RED + Fore.BLUE + "Nouveauté : mettez à jour votre version des Services depuis GitHub à partir du 29/06/2011")
    
    print("")
    
    print(Back.RED + Fore.BLUE + """1.20 (31/05/2023) : Ajout du système de Login au lancement
Ajout du service Autres Apps
Ajout d'interfaces graphiques

1.21 (29/06/2023) : Ajout du services News
Ajout des Clients MC (accès via ModApps)

Correction des bugs apportés par la version précédente
Ajout du système de notifications au lancement

1.22 / 1.23 / 1.24 (15/07/2023 - 30/08/23) : Ajout de la fonction utilisateur lambda (Un autre Launcher sera mis à disposition pendant la Mise à jour)
""")
    time.sleep(20)
    input("Appuyez sur entrée pour quitter")
