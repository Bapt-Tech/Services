###HubClientsMc
###28/06/2023
###15:28
###BaptisteH

def Mc_Clients():
    import time
    from ModSer import ModMcTp
    from ModSer import ModMcEau
    from ModSer import ModLog
    from ModSer import OsID
    
    ModLog;Log("--HubMcCli--")
    
    ModLog.Log("Ready")

    print("Menu des clients Minecraft")
    print("")
    print("1. Client de TP")
    print("2. Client d'eau")

    Choix = int(input("Entrez votre choix : "))

    if Choix == 1:
        ModLog.Log("TpMc")
        ModMcTp.TpMc()
    
    if Choix == 2:
        ModLog.Log("McEau")
        ModMcEau.McEau()