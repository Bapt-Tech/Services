#ModUserBasic
#11/10/2023
#13:55
#Bapt-Tech

def UserBasic():
    try:
        import os
        import time
        from ModSer import OsID
        from ModSer import ModLog

        NIPCode = 1934

        def WiFiServer():
            while True :
                print("Un code PIN est necessaire pour démarrer le serveur.")
                NIPCodeInput = int(input("Entrez le code PIN : ")
                if NIPCodeInput == NIPCode:
                    print("Chargement...")
                    from ModSer import HubServer
                    HubServer.HubServer()
                    break
                else:
                    print("Code PIN incorrect.")
                    print("Réessayez SVP")
        
        def Games():
            while True :
                print("Un code PIN est necessaire pour Jouer. Entrez 0000 pour quitter.")
                NIPCodeInput = int(input("Entrez le code PIN : ")
                if NIPCodeInput == NIPCode:
                    print("Chargement...")
                    from ModSer import HubGames
                    HubGames.HubGames()
                    break
                elif NIPCodeInput == (0000):
                    break
                else:
                    print("Code PIN incorrect.")
                    print("Réessayez SVP")


        print("Bienvenue sur ce nouveau service.")
        print("Chargement en cours...")

        while True:
            print("Menu")
            print("")
            print("1. Serveur WiFi")
            print("2. Jeux")
            print("3. Autres Apps")

            Choix = int(input("Entrez votre choix : "))

            if Choix == 1:
                WiFiServer()
            if Choix == 2:
                Games()

    except:
        print("err")