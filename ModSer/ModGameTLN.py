def GameTLN():
    import random
    from ModSer import ModLog
    ModLog.Log("--ModGameTLN--\n")
    ModLog.Log("Ready\n")
    NombAléa = random.randrange(40)
    for i in range(5):
        NbChoisi = int(input("Entrez un nombre entre 1 et 40 : "))
        if NbChoisi == NombAléa:
            ModLog.Log("Trouvé\n")
            #ModLog.Log(NombAléa)
            print("Bravo ! Le nombre était bien le nombre entré ! ")
            break
        if NbChoisi < NombAléa:
            ModLog.Log("+ Grd\n")
            print("Le nombre est plus grand que le nombre entré ! ")
        if NbChoisi > NombAléa:
            ModLog.Log("+ Pt\n")
            print("Le nombre est plus petit que le nombre entré ! ")
    print(NombAléa)
    ModLog.Log("Fin du jeu\n")
    #ModLog.Log(NombAléa)