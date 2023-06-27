def GameMorpion():
    from ModSer import ModLog
    ModLog.Log("--ModGameMor--\n")
    ModLog.Log("Ready\n")

    # Définition du plateau de jeu
    plateau = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Fonction pour afficher le plateau de jeu
    def afficher_plateau():
        print("   1  2  3 ")
        print("  ---------")
        for i in range(3):
            print(str(i+1) + "|", end="")
            for j in range(3):
                print(" " + plateau[i][j] + " ", end="")
                if j != 2:
                    print("|", end="")
            print("|")
            print("  ---------")
    
    # Fonction pour vérifier si le plateau est plein
    def plateau_plein():
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == " ":
                    return False
        return True

    # Fonction pour vérifier si un joueur a gagné
    def verifier_victoire(symbole):
        # Vérifier les lignes
        for i in range(3):
            if plateau[i][0] == symbole and plateau[i][1] == symbole and plateau[i][2] == symbole:
                return True

        # Vérifier les colonnes
        for j in range(3):
            if plateau[0][j] == symbole and plateau[1][j] == symbole and plateau[2][j] == symbole:
                return True

        # Vérifier les diagonales
        if plateau[0][0] == symbole and plateau[1][1] == symbole and plateau[2][2] == symbole:
            return True
        if plateau[0][2] == symbole and plateau[1][1] == symbole and plateau[2][0] == symbole:
            return True

        # Si aucun gagnant, retourner False
        return False

    # Boucle principale du jeu
    joueur_actuel = "X"
    while True:
        afficher_plateau()

        while True:
        
            # Demander au joueur de saisir un coup
            ligne = int(input("Joueur " + joueur_actuel + ", entrez le numéro de ligne : "))
            colonne = int(input("Joueur " + joueur_actuel + ", entrez le numéro de colonne : "))

            # Vérifier si le coup est valide
            if (ligne<0) and (ligne>4):
                print("Coup invalide, veuillez choisir une case vide.")
            if (colonne<0) and (colonne>4):
                print("Coup invalide, veuillez choisir une case vide.")
            if plateau[ligne-1][colonne-1] != " ":
                print("Coup invalide, veuillez choisir une case vide.")
            else:
                break

        # Placer le symbole du joueur sur le plateau
        plateau[ligne-1][colonne-1] = joueur_actuel

        # Vérifier si le joueur a gagné
        if verifier_victoire(joueur_actuel):
            afficher_plateau()
            ModLog.Log("Player "+ joueur_actuel +" Win\n")
            print("Félicitations, joueur " + joueur_actuel + ", vous avez gagné !")
            break

        # Vérifier si le plateau est plein
        if plateau_plein():
            afficher_plateau()
            print("Match nul.")
            ModLog.Log("Match Nul\n")
            break

        # Changer de joueur
        if joueur_actuel == "X":
            joueur_actuel = "O"
        else:
            joueur_actuel = "X"
