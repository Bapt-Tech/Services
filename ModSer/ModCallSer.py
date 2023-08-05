def Services():
    
    #Pour Activer/Désactiver par défaut les Hubs (true/false)
    Disable_HG = ("false")
    Disable_HS = ("false")

    import os
    from ModSer import ModLogSer, StatusUsername
    from ModSer import HubGames
    from ModSer import HubServer
    from ModSer import ModApps
    from ModSer import ModNews
    from ModSer import ModLog
    from ModSer import OsID
    
    if OsID.determiner_os() == "Linux":
        Term_clear = ("clear")
    if OsID.determiner_os() == "Windows":
        Term_clear = ("cls")
        
    
    print("Pour des raisons de sécurité, veuillez vous identifier.")

    ModLog.Log("--ModCallSer--\n")
    
    ModLog.Log("Connexion au LoginService pour Auth.\n")

    ModLogSer.LoginService()

    StatusUsername = StatusUsernames

    print(StatusUsername)
    
    ModLog.Log("Ready\n")
    
    while True:
    
        ModLog.Log("While True pour ModCallSer")
        
        os.system(Term_clear) 

        print("Tableau Administrateur")

        print("Menu des services")
        print()
        print("1. Login Service.")
        print("2. Jeux.")
        print("3. Serveurs.")
        print("4. Désactivation des services.")
        print("5. Autres Apps")
        print("6. Nouveautés")
        print("7. Exit")


        Choix = int(input("Entrez le service à appeler : "))

        if Choix == 1:
            ModLog.Log("ModLogSer-Start\n")
            ModLogSer.LoginService()
            ModLog.Log("ModLogSer-End\n")

        if Choix == 2:
            if Disable_HG == ("true"):
                ModLog.Log("HubGames-Start\n")
                ModLog.Log("Transfert de la demande vers le service Hub Games\n")
                HubGames.HubGames()
                ModLog.Log("HubGames-End\n")
            else:
                print("Ce service à été désactivé par votre administrateur")

        if Choix == 3:
            if Disable_HS == ("true"):
                ModLog.Log("HubServer-Start\n")
                ModLog.Log("Transfert de la demande vers le service Hub Server\n")
                HubServer.HubServer()
                ModLog.Log("HubServer-End\n")
            else:
                print("Ce service à été désactivé par votre Administrateur")
        
        if Choix == 4:
            os.system(Term_clear)
            ModLog.Log("Services desactivation")
            print("Interface de désactivation des services")
            print("")
            print("1. HubGames")
            print("2. HubServer")
            
            Choix = int(input("Entrez le service à désactiver : "))
            
            if Choix == 1:
                ModLog.Log("HubGames-Disable")
                if Disable_HG == ("true"):
                    ModLog.Log("Désactivation")
                    Disable_HG = ("false")
                if Disable_HG == ("false"):
                    ModLog.Log("Activation")
                    Disable_HG = ("true")
            
            if Choix == 2:
                ModLog.Log("HubServer-Disable")
                if Disable_HS == ("true"):
                    ModLog.Log("Désactivation")
                    Disable_HS = ("false")
                if Disable_HS == ("false"):
                    ModLog.Log("Activation")
                    Disable_HS = ("true")
            
        if Choix == 5:
            print("Autres Apps")
            ModLog.Log("Autres Apps")
            ModApps.Others_apps()
        
        if Choix == 6:
            ModLog.Log("ModNews\n")
            ModNews.News()
            
        
        if Choix == 7:
            ModLog.Log("Exit\n")
            input("Appuyez pour fermer...")
            ModLog.Log("End\n")
            ModLog.Log("\n")
            ModLog.Log("\n")
            ModLog.Log("\n")
            os.system("pkill -f 'terminal'")
            exit("reportez les logs")