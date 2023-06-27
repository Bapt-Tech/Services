#Hub Games

def HubGames():
    
    from ModSer import ModGameMor
    from ModSer import ModGamePendu
    from ModSer import ModGameTLN
    from ModSer import ModLog
    import os
    from ModSer import OsID
    
    if OsID.determiner_os() == "Linux":
        Term_clear = ("clear")
    if OsID.determiner_os() == "Windows":
        Term_clear = ("cls")
    
    ModLog.Log("--HubGames--\n")
    
    ModLog.Log("Ready\n")
    
    print("Menu des jeux")
    print("")
    print("1. Morpion")
    print("2. Trouve le nombre")
    print("3. Pendu")
    
    Choix = int(input("Entrez votre choix : "))
    
    if Choix == 1:
        ModGameMor.GameMorpion()
        ModLog.Log("Morpion\n")
    
    if Choix == 2:
        ModGameTLN.GameTLN()
        ModLog.Log("TLN\n")
    
    if Choix == 3:
        ModGamePendu.GamePendu()
        ModLog.Log("Pendu\n")
    
    if Choix == 5:
        
        ModLog.Log("Exit\n")
        
        input("Appuyez pour fermer...")
        
        os.system("pkill -f 'terminal'")
        
        ModLog.Log("\n")
        
        ModLog.Log("\n")
        
        ModLog.Log("\n")
    
    """input("Appuyez pour fermer...")
        
    ModLog.Log("Fermeture en cours...\n")
        
    os.system("pkill -f 'terminal'")
        
    ModLog.Log("Le terminal s\'est fermé avec succès...\n")
        
    ModLog.Log("\n")
        
    ModLog.Log("\n")
        
    ModLog.Log("\n")"""