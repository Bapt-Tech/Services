#Ce service est la propriété de la société HB--QCI
#(Voir dans la Documentation)
#Tous droits réservés

#def LoginService():

#Préproduction

import os

import time

import datetime

import ModLog
#import ModLog
import OsID
#import OsID
if OsID.determiner_os() == "Linux":
    Term_clear = ("clear")
if OsID.determiner_os() == "Windows":
    Term_clear = ("cls")

date_actuelle = datetime.date.today()

#Logs info
ModLog.Log("--ModLogSer--\n")
ModLog.Log("\n")
ModLog.Log("Info ModLogSer\n")
ModLog.Log("\n")
ModLog.Log("Log -> Ready\n")
ModLog.Log("App -> No\n")
ModLog.Log("File -> No\n")
ModLog.Log("Connect -> No\n")
ModLog.Log("Official session -> Yes\n")
ModLog.Log("\n")

#Version

Version_No = ("1.19.1")
Version = ("Version " + Version_No + ".")

#Partie 1 : Ouverture du fichier

print("Pressez \"entrée\" pour continuer")

Clear = input()

os.system(Term_clear)

if Clear != "a":

    #Partie 1.1 : Lancement

    print("Bienvenue sur le service Login Service")

    time.sleep(1)

    print("Uniquement pour usage personnel ou usage collectif sous conditions (voir dans l'aide).")

    time.sleep(1)

    print("La société \"HB--QCI\" est propriétaire de ce service.")

    time.sleep(1)

    print("Tous droits réservés.")

    time.sleep(1)

    print("Version du " + date_actuelle.strftime("%d/%m/%Y") + ".")

    time.sleep(1)

    print("L\'utilisation de ce service pour une infrastucture complète est interdite sans accord de la société \"HB--QCI\".")

    print("Chargement ... ")

    print("Veuillez patienter ... ")

    time.sleep(3)

    print("20%")

    time.sleep(3)

    print("40%")

    time.sleep(3)

    print("60%")

    time.sleep(3)

    print("80%")

    time.sleep(3)

    print("100%")

    print()

    print("Bienvenue sur le service \"Login Service\".")

    print("")

    print(Version)

    print("")

#Partie 1.2 : Ouverture du fichier

ModLog.Log("App -> Ready\n")
ModLog.Log("Ready\n")

print("Menu des versions.")
print("")
print("1. Version " + Version_No + " (Stable).")
#print("2. Version Test (Instable).")
#print("3. Aide")
print("4. Quitter")

Choix_Version = int(input("Entrez votre choix : "))

#Partie 1.2.1 : Version Alpha

if (Choix_Version == 1):
    ModLog.Log("Version Alpha\n")

    Chemin_Absolu = ()

    print()
    print("Assurez-vous d'avoir bien téléchargé le fichier \"PWD_DATA.bps\".")

    print("")

    if OsID.determiner_os() == "Linux":
        os_def = "Linux"
    if OsID.determiner_os() == "Windows":
        os_def = "windows"
    
    print("Menu")
    print("")
    print("1. Conserver l'OS détecté ( " + os_def + " )")
    print("2. Chercher dans le fichier contenant le script.")
    os_choix = int(input("Entrez votre choix : "))
     
    if os_choix == 1:
        ModLog.Log("Os prédéfini\n")
        if os_def == "Linux":
            ModLog.Log("Linux\n")
            Chemin_Absolu = "/home/baptiste/.BPS/PWD_DATA.bps"
        if os_def == "windows":
            ModLog.Log("Windows\n")
            Chemin_Absolu = "D:/Utilisateurs/Telechargements/PWD_DATA.bps"
    if os_choix == 2:
        ModLog.Log("Dans le même fichier\n")
        Chemin_Absolu = "PWD_DATA.bps"

    f = open(Chemin_Absolu, "r")

    data = f.read()
    
    f.close()

#Partie 1.2.2 : Version Test

"""if (Choix_Version == 2):
    ModLog.Log("Version Test\n")

    Chemin_Absolu = ()

    print()

    print("Assurez-vous d'avoir bien téléchargé le fichier \"PWD_DATAtest.bps\".")

    print("")

    print("Menu")

    print("")
    
    if OsID.determiner_os() == "Linux":
        os_def = "Linux"
    if OsID.determiner_os() == "Windows":
        os_def = "windows"
    
    print("Menu")
    print("")
    print("1. Conserver l'OS détecté ( " + os_def + " )")
    print("2. Chercher dans le fichier contenant le script.")
    os_choix = int(input("Entrez votre choix : "))
     
    if os_choix == 1:
        if os_def == "linux":
            Chemin_Absolu = "/home/baptiste/.BPS/PWD_DATAtest.bps"
        if os_def == "windows":
            Chemin_Absolu = "D:/Utilisateurs/Telechargements/PWD_DATAtest.bps"
    if os_choix == 2:
        Chemin_Absolu = "PWD_DATAtest.bps"

    f = open(Chemin_Absolu, "r")

    data = f.read()

    f.close()

#Partie 1.2.3 : Aide sur les versions

#if Choix_Version == 3:
    ModLog.Log("Help\n")

    print()

    print("Menu de l\'aide.")
    print("1. Aide sur les versions.")
    print("2. Aide sur les licences.")
    print("3. Aide sur l\'utilisation.")
    print("4. Quitter.")

    Choix_Aide = int(input("Entrez votre choix : "))

    if (Choix_Aide == 1):
        print("")
        print("Aide sur les Versions")
        print("")
        ModLog.Log("Aide Versions\n")
        print("Menu de l\'aide sur les versions.")
        print("")
        print("1. Version Alpha.")
        print("2. Version Test.")

        Choix_Version_Aide = int(input("Entrez votre choix : "))

        if Choix_Version_Aide == 1:
            ModLog.Log("Aide Version Alpha\n")
            print("")
            print("Aide sur la version Alpha.")
            print("")
            print("La version " + Version + " est la version la plus stable à ce jour.")
            print("Elle doit être utilisée pour les usages collectifs pour bénéficier des avantages utilisateurs")
            print("Cette version lit uniquement le fichier officiel mis en place par votre collectivité et non le fichier test pour les MàJ (1 puis 2).")

        if Choix_Version_Aide == 2:
            print("")
            print("Aide sur la version Test.")
            print("")
            ModLog.Log("Aide version Test\n")
            print("La version Test est la version qui doit être utilisée pendant les modifications du fichier utilisateur originel.")
            print("Elle n\'utilise pas le fichier officiel mais un doublon identique.")
            print("Ce doublon peut-être utilisé sans risque de perte de données.")

    if Choix_Aide == 2:
        print("")
        print("Aide sur les Licences.")
        print("")
        ModLog.Log("Aide Licenses\n")
        print("Les licenses utilisées pour ce Logiciel sont les mêmes que si vous utilisez des autres services de cette sociéte.")
        print("L\' Administrateur de la collectivité doit obtenir une license de la société \"HB--QCI\" pour pouvoir utiliser les services légalement")
        print("Si aucune licence de la société nommée ci-dessus n\'est pas obtenue par l\' Administrateur, des peines pénales peuvent s\' appliquer à l\'administrateur et à sa collectivité.")
        print("Pour obtenir une license, s\adresser à la société \"HB--QCI\".")
        print("Les personnes utilisant le service pour des besoins personnels n\'ont pas besoin de licence.")

    if Choix_Aide == 3:
        print("")
        ModLog.Log("Aide Utilisateurs\n")
        print("Aide sur les Utilisateurs.")
        print("")
        print("Les utilisateurs ont différents statuts selon leur pronom comme \"Admin\" pour avoir les pouvoirs administrateurs.")
        print("Tous les autres utilisateurs n'ayant pas le pronom d\'administrateur seront considérés comme utilisateurs lambda.")
        print("La phase de tri sur les statuts s\'effectue lorsque le message \"Bienvenue, NOM D\'UTILISATEUR.\" est affiché.")

    print("Le Logiciel à bien été quitté. La fenêtre va se fermer automatiquement. Â© Version du " + date_actuelle.strftime("%d/%m/%Y") + ". HB--QCI.")

    time.sleep(5)

    ModLog.Log("En attente de la réponse User\n")

    input("Appuyez pour fermer...")

    ModLog.Log("End\n")

    os.system("pkill -f 'terminal'")
"""
#Partie 1.2.4 : Quitter

if Choix_Version == 4:
    ModLog.Log("Quitter\n")

    print("Le logiciel à été quitté avec succès. Version du " + date_actuelle.strftime("%d/%m/%Y") + ". HB--QCI.")

    ModLog.Log("Logiciel quitté avec succès\n")

    time.sleep(5)

    ModLog.Log("En attente de la réponse utilisateur...\n")

    input("Appuyez pour fermer...")

    ModLog.Log("Fermeture en cours...\n")

    os.system("pkill -f 'terminal'")

    ModLog.Log("Le terminal à été fermé avec succès.\n")

print("Le fichier utilisateur a bien été chargé.")

ModLog.Log("Le fichier utilisateur a bien été chargé\n")

#Partie 2 : Mise en forme des données
ModLog.Log("File : Ready\n")

ModLog.Log("P 2 : Mise en forme des données\n")

#Initialisation des listes
usernames = []
passwords = []
UsersStatus = []

splittedData = data.split("\n")

#Parcourir chaque ligne du texte"
for line in splittedData:
    #Séparer le nom d'utilisateur et le mot de passe
    username, password, UserStatus = line.split(";")

    #Ajouter le nom d'utilisateur et le mot de passe aux listes respectives
    
    usernames.append(username)

    passwords.append(password)

    UsersStatus.append(UserStatus)
    
STRusernames = ' '.join(usernames)
ModLog.Log(STRusernames)

STRpwd = ' '.join(passwords)
ModLog.Log(STRpwd)

STRusr = ' '.join(UsersStatus)
ModLog.Log(STRusr)

#Partie 3 : Login

ModLog.Log("Login...\n")

Username_Request = input("Entrez le nom d'utilisateur : ")

ModLog.Log(Username_Request + "\n")

foundIndex = -1

for index, item in enumerate(usernames):
    if Username_Request == item:
        foundIndex = index
        break

if foundIndex > -1:
    Pwd_Request = input("Entrez le mot de passe : ")

    ModLog.Log(Pwd_Request + "\n")

    expectedPassword = passwords[foundIndex]

    if Pwd_Request == expectedPassword:

        if UsersStatus[index] == "Admin":
            StatusUsername = "Admin"
        if UsersStatus[index] == "User":
            StatusUsername = "Basique"

        print("Bienvenue, " + Username_Request + ".")
        print("Votre statut est défini sur " + StatusUsername)
        ModLog.Log("Connect -> Yes\n")


        ModLog.Log("Connexion effectuée avec succès...\n")
        ModLog.Log("\n")
        ModLog.Log("\n")
        ModLog.Log("\n")

    else:
        print("Mauvais mot de passe (E0002). Version du " + date_actuelle.strftime("%d/%m/%Y") + ". HB--QCI.")

        ModLog.Log("Mauvais mot de passe...\n")

        time.sleep(5)

        ModLog.Log("En attente de la réponse utilisateur...\n")

        input("Appuyez pour fermer...")

        ModLog.Log("Fermeture en cours...\n")

        os.system("pkill -f 'terminal'")

        ModLog.Log("Terminal fermé avec succès.\n")

        ModLog.Log("\n")

        ModLog.Log("\n")

        ModLog.Log("\n")

        exit("Reporter les logs SVP")

else:
    print("Compte inconnu (E0001). Version du " + date_actuelle.strftime("%d/%m/%Y") + ". HB--QCI.")

    ModLog.Log("Compte inconnu...\n")

    time.sleep(5)

    ModLog.Log("En attente de la réponse utilisateur...\n")

    input("Appuyez pour fermer...")

    ModLog.Log("Fermeture en cours...\n")

    os.system("pkill -f 'terminal'")

    ModLog.Log("Terminal fermé avec succès.\n")
    
    exit("Reporter les logs SVP")
