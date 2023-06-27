def GamePendu():
    
    
    import random
    from ModSer import ModLog
    ModLog.Log("--ModGamePendu--\n")
    ModLog.Log("Ready\n")

    # Les mots à deviner
    mots = ["python", "programmation", "ordinateur", "jeu", "fleur", "programme", "language", "informatique", "algorithme", "developpeur", "boucle", "fonction", "iteration", "bibliotheque", "variable", "interface", "systeme","console", "internet", "navigateur", "donees", "interpreteur", "editeur", "shell" ]

    # Choisir un mot aléatoire parmi les mots disponibles
    mot_a_deviner = random.choice(mots)
    ModLog.Log("Mot aléatoire choisi\n")

    # Initialiser les variables
    lettres_devinées = []
    nb_chances = 7

    # Boucle principale du jeu
    while nb_chances > 0:
        # Afficher le mot partiellement deviné
        mot_partiel = ""
        for lettre in mot_a_deviner:
            if lettre in lettres_devinées:
                mot_partiel += lettre
            else:
                mot_partiel += "_"
        print(mot_partiel)

        # Demander une lettre à l'utilisateur
        lettre = input("Entrez une lettre : ")
        ModLog.Log("lettre entrée : " + lettre + ".\n")

        # Vérifier si la lettre est dans le mot à deviner
        if lettre in mot_a_deviner:
            print("Bonne réponse !")
            ModLog.Log("Lettre valide\n")
            lettres_devinées.append(lettre)
        else:
            print("Mauvaise réponse.")
            ModLog.Log("Lettre non valide\n")
            nb_chances -= 1

        # Vérifier si le joueur a gagné
        if "_" not in mot_partiel:
            print("Félicitations, vous avez gagné !")
            ModLog.Log("Win\n")
            break

    # Vérifier si le joueur a perdu
    if nb_chances == 0:
        print("Dommage, vous avez perdu. Le mot était : ", mot_a_deviner)
        ModLog.Log("Perdu\n")
        ModLog.Log(mot_a_deviner + "\n")
    