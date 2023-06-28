###AutresApps
###15/06/2023
###19:59
###BaptisteH

def Others_apps():
    import time
    from ModSer import RR_1
    from ModSer import RR_2
    from ModSer import RR_3
    from ModSer import ModMcTp
    from ModSer import ModLog
    from ModSer import OsID

    ModLog.Log("--Others Apps--")

    print("Bienvenue sur le service Autres Apps")
    print("Ceci est une version expérimentale")
    print("Elle pourra être retirée à tout moment si un problème est détecté")

    time.sleep(1)
    ModLog.Log("Ready")
    print("Menu")
    print("")
    print("1. Ce service est actuellement en MàJ. Clients Mc")
    print("2. Portail GUI")
    print("3. /!\ Danger /!\ Ne pas ouvrir")
    print("4. Aide")
    print("5. Quitter")

    Choix = int(input("Entrez votre choix : "))

    """if Choix == 1:
        ModLog.Log("Clients MC\n")
        if OsID.determiner_os() == "Linux":
            ModLog.Log("Clients Mc par linux (accès)\n")
            ModMcTp.TpMc()"""
            
        if OsID.determiner_os() == "Windows":
            print("Vous devez disposer de Raspbian pour acceder à cette fonction")
            ModLog.Log("Mc Win Err\n")
        

    if Choix == 2:
        ModLog.Log("Portail GUI\n")
        print("/!\ Ce service utilise des librairies comme Tkinter ou Guizero")
        print("Des dysfonctionnements potentiels sont probablement dus au transfert d'interface")
        print("Une fois que vous avez terminé, fermez la fenêtre avec une nouvelle interface et continuez depuis le terminal")
        time.sleep(2)
        print("Chargement des interfaces...")
        time.sleep(3)
        print("Menu")
        print("")
        print("1.Rickroller")
        print("2. INVALID")
        print("3. INVALID")
        print("4. Quitter")
        
        Choix = int(input("Entrez votre choix : "))
        
        if Choix == 1:
            ModLog.Log("RickRoll\n")
            print("Rickroll")
            print("")
            print("1. Memes PC + Chips")
            print("2. Memes NGGYU")
            print("3. Memes Beluga")
            
            Choix = int(input("Entrez votre choix : "))
            
            if Choix == 1:
                ModLog.Log("RR_1\n")
                RR_1.RickRoll_1()
            
            if Choix == 2:
                ModLog.Log("RR_2\n")
            
            if Choix == 3:
                ModLog.Log("RR_3\n")

