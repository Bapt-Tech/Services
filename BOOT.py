#Ce service est la propriété de la société HB--QCI
#(Voir dans la Documentation)
#Tous droits réservés


#Pour activer les services mettre True
#Pour désactiver les services mettre False
Services_Activated = ("True")

if Services_Activated == ("True"):

    import time
    import datetime
    import os
    from colorama import Fore, Style
    from ModSer import Services
    from ModSer import ModLog
    from ModSer import OsID
        
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
    texte = """Nouveau : mettez à jour votre version des Services depuis GitHub à partir du 29/06/2023
La Version 1.21 est là ! Toute belle toute propre ! Retrouvez les ajouts dans la page Nouveautés.
Les Clients Minecraft sont enfin arrivés ! Accès via Autres Apps.
De nombreuses possibilités s'ouvrent à vous : téléchargez la version 1.21 dès le jeudi 29 et profitez un max des nouveautés !
Suite à une erreur de GUI, la Mise à jour des interfaces sera reportée.
"""
    texte_colore = f"{Fore.BLUE}{texte}{Style.RESET_ALL}"
    print(texte_colore)
    time.sleep(1)
    print("Transfert de la demande au service ModCallSer...")
    print("Patientez SVP")
    time.sleep(3)
    ModLog.Log("Transfert au service ModCallSer\n")
    print("Connexion établie")
    Services()

if Services_Activated == ("False"):
    exit("Une mise à jour est en cours. Veuillez réessayer ultérieurement")
