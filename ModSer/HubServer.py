def HubServer():
    import os
    #/!\ version RPi
    #Serveurs Win disables
    #Pour activer mettre commande "HubServer.MenuServer()"
    from ModSer import AppRaspiV2
    from ModSer import app
    from ModSer import ModLog
    from ModSer import AppWinV1
    from ModSer import AppWin10V2
    from ModSer import OsID
    
    if OsID.determiner_os() == "Linux":
        Term_clear = ("clear")
    if OsID.determiner_os() == "Windows":
        Term_clear = ("cls")
    #import
    #import
    #import
    #import
    #import
    #import
    ModLog.Log("--HubServer--\n")
    ModLog.Log("Ready\n")
    print("")
    print("Menu des serveurs")
    print()
    print("1. Version pour Raspbian (RPI)")
    print("2. Version pour Windows 10")
    Choix = int(input("Entrez votre choix : "))
    print("")
    if Choix == 1:
        ModLog.Log("Server Rpi\n")
        print("Versions de l'application")
        print()
        #print("2. Version 2 (Obsolète)")
        print("3. Version 3 (Recommandé)")
        Choix = int(input("Entrez votre choix : "))
        os.system('clear')
    
        """if Choix == 2:
            ModLog.Log("Server Rpi V2\n")
            AppRaspiV2.Server()"""
        if Choix == 3:
            ModLog.Log("Server Rpi V3 (Good)\n")
            app.Server()

    if Choix == 2:
        ModLog.Log("Server Win\n")
        print("Versions de l'application")
        print("")
        #print("1. Version 1 (Obsolète)")
        print("2. Version 2 (Recommandé)")
        os.system('clear')
        """if Choix == 1:
            ModLog.Log("Server Win V1\n")
            AppWinV1.Server()"""
        if Choix == 2:
            ModLog.Log("Server Win V2\n")
            AppWin10V2.Server()
