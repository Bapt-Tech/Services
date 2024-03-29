#Ce service est la propriété de la société HB--QCI
#(Voir dans la Documentation)
#Tous droits réservés


#Pour activer les services mettre True
#Pour désactiver les services mettre False
try:

    Services_Activated = ("True")

    if Services_Activated == ("True"):

        ###Import Modules

        import time
        import colorama
        import datetime
        import os
        from colorama import Fore, Style, Back

        ###Import Modules Internes

        from ModSer import Services
        from ModSer import ModLog
        from ModSer import OsID

        colorama.init(autoreset=True)
            
        if OsID.determiner_os() == "Linux":
            Term_clear = ("clear")
        if OsID.determiner_os() == "Windows":
            Term_clear = ("cls")

        date_actuelle = datetime.date.today()
        heure_actuelle = datetime.datetime.now()

        ModLog.Log("--Boot--\n")
        ModLog.Log(date_actuelle.strftime("%A %d %B %Y\n"))
        ModLog.Log("{}h{}m{}s.\n".format(heure_actuelle.hour, heure_actuelle.minute, heure_actuelle.second))

        Version = "1.20.2"
        ModLog.Log("Version " + Version + "\n")

        print("Client de connexion au services")
        print("Ce service assure la sucession de l'ancien service \'ModCallModCallSer\'")
        time.sleep(2)
        print("Ce service est la propriété de \"HB--QCI\"")
        time.sleep(1)
        print("Version du client : " + Version)
        print(Back.RED + Fore.BLUE + """Nouveau : mettez à jour votre version des Services depuis GitHub à partir du 29/06/2023
    La Version 1.21 est là ! Toute belle toute propre ! Retrouvez les ajouts dans la page Nouveautés.
    Les Clients Minecraft sont enfin arrivés ! Accès via Autres Apps.
    De nombreuses possibilités s'ouvrent à vous : téléchargez la version 1.21 dès le jeudi 29 et profitez un max des nouveautés !
    Suite à une erreur de GUI, la Mise à jour des interfaces sera reportée.
    """)
        time.sleep(1)
        print("Transfert de la demande au service ModCallSer...")
        print("Patientez SVP")
        time.sleep(3)
        ModLog.Log("Transfert au service ModCallSer\n")
        print("Connexion établie")
        Services()

    if Services_Activated == ("False"):
        exit("Une mise à jour est en cours. Veuillez réessayer ultérieurement")

except KeyboardInterrupt:
    print("Erreur !")
    print("Récupération des données en cours")
    print("Récupération terminée")
    print("Erreur fatale !")
    print("Données récupérées : OK")
    print("Fermeture d'urgence.")
    print("Merci d'avoir utilisé les Services")
