def TpMc():
 
    #Init

    import time
    from mcpi import minecraft

    mc = minecraft.Minecraft.create()

    #Boot

    print("Bienvenue sur le service Minecraft")

    #Chat

    mc.postToChat("Bienvenue sur le service Minecraft.")
    mc.postToChat("Quand cette icone s\'affichera ( [] ) une action sur le terminal sera requise.")

    if 1==1:

        print("Menu")
        print()
        print("1. Entrer les coordonnees.")
        print("2. Favoris.")

        Choix = int(input("Entrez votre choix : "))
        if Choix == 1:
            Pos = mc.player.getPos ()
        
            mc.postToChat("[]")
        
            print("Voulez vous vous teleporter ? ")
        
            Tp = input("Oui/Non : ")
            if Tp == ("Oui"):
                TpPosX = int(input("Entrez la coordonnee X : "))
                TpPosY = int(input("Entrez la coordonnee Y : "))
                TpPosZ = int(input("Entrez la coordonnee Z : "))
                mc.player.setPos(TpPosX, TpPosY, TpPosZ)
                mc.postToChat("Vous avez ete teleporte avec succes aux coordonnees choisies.") 
            else:
                exit(":/")

        if Choix == 2:
            print("Menu des Favoris")
            print()
            print("1. Choisir un favori")
            print("2. Ajouter un favori")
            Choix = int(input("Entrez votre choix : "))
            if Choix == 1:
                f = open("ModMinTp.txt", "r")
                data = f.read()
                
                f.close()
            
                Names = []
                TpX = []
                TpY = []
                TpZ = []

                splittedData = data.split("\n")

                #Parcourir chaque ligne du texte
                for line in splittedData:
                    #Separer le nom d'utilisateur et le mot de passe
                    name, TpXFil, TpYFil, TpZFil = line.split(  ";")
        
                    #Ajouter le nom d'utilisateur et le mot de passe aux listes respectives
                    Names.append(name)
                    
                    TpX.append(TpXFil)
                    TpY.append(TpYFil)
                    TpZ.append(TpZFil)
                    #numéro de ligne et - 1 pour liste
                if 1==1:
                    print("1. " + Names[0])
                    print("2. " + Names[1])
                    print("3. " + Names[2])
                    print("4. " + Names[3])
                    print("5. " + Names[4])
                    print("6. " + Names[5])
                    TpPos = int(input("Entrez votre choix : "))
                    if TpPos == 1:
                        mc.postToChat("Veuillez patienter durant la teleportation...")
                        time.sleep(5)
                        mc.player.setPos(TpX[0],TpY[0],TpZ[0])
                        mc.postToChat("Vous etes arrives a destination.")
                    if TpPos == 2:
                        mc.postToChat("Veuillez patienter durant la teleportation...")
                        time.sleep(5)
                        mc.player.setPos(TpX[1],TpY[1],TpZ[1])
                        mc.postToChat("Vous etes arrives a destination.")
                    if TpPos == 3:
                        mc.postToChat("Veuillez patienter durant la teleportation...")
                        time.sleep(5)
                        mc.player.setPos(TpX[2],TpY[2],TpZ[2])
                        mc.postToChat("Vous etes arrives a destination.")
                    if TpPos == 4:
                        mc.postToChat("Veuillez patienter durant la teleportation...")
                        time.sleep(5)
                        mc.player.setPos(TpX[3],TpY[3],TpZ[3])
                        mc.postToChat("Vous etes arrives a destination.")
                    if TpPos == 5:
                        mc.postToChat("Veuillez patienter durant la teleportation...")
                        time.sleep(5)
                        mc.player.setPos(TpX[4],TpY[4],TpZ[4])
                        mc.postToChat("Vous etes arrives a destination.")
                    if TpPos == 6:
                        mc.postToChat("Veuillez patienter durant la teleportation...")
                        time.sleep(5)
                        mc.player.setPos(TpX[5],TpY[5],TpZ[5])
                        mc.postToChat("Vous etes arrives a destination.")
                    
            if Choix == 2:
                exit("Accédez au fichier ModMinTp.txt et ajoutez des destinations sous le format NOM;X;Y;Z")
