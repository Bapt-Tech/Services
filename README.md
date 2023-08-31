# Actus

La 1.21 est sortie !

Testez-la et reportez les erreurs pour améliorer les services.

Les nouveautés sont disponibles dans le service News.

# Notes

Un peu d'aide ? La documentation est incluse dans le dossier principal.

# Mises à Jour et opérations

Opérations en cours : 

Aucune Mise à Jour est en cours...

Prochaines fonctionnalités : 

Mise en place d'interfaces différentes selon statut (Admin ou Basique)

1.23 bientôt disponible en preview !

# Installation

## Pour installer les Services simplement : 

1. Cliquez sur le bouton "CODE"
2. Téléchargez l'archive ZIP en cliquant sur "Download ZIP".
3. Extrayez les fichiers de l'archive ZIP
4. Installez les modules en utilisant la commande dans un terminal : "pip install {Nom du module}" (Modules requis : os, Flask, Platform, Colorama, time, datetime, random et mcpi.minecraft (pour les joueurs de Minecraft Pi)) 
5. Executez le fichier "LoginService.cmd"
6. Les services sont lancés !
7A. Identifiant : Guest1
7B. Mot de passe : PUwKN5e9mt5s9x2aCQAD
8. Pour les utilisateurs avancés, vous pouvez lire la référence suivante.

## Pour installer les Services à la façon Bidouilleur : 

/!\ Ce tuto ne fonctionne que avec le shell du terminal "Bash".
Pour le changer temporairement, entrez la commande suivante : 
```pwsh
bash
```

1. Ouvrez un terminal.
1a. Pour Windows : Accedez au menu Démarrer puis entrez "cmd" ou "terminal"
1b. Pour Mac : Accedez au menu LaunchPad et recherchez "Terminal" ou dans Finder, ouvrez le dossier "Applications" puis "Utilitaires" et cliquez sur "Terminal"

2. Assurez vous que Git est installé via cette commande :
 ```bash
git version
```
3. Si Git est installé, la version de Git s'affichera. Sinon, la commande ne sera pas reconnue.

4.Executez cette commande pour recevoir une copie des services. Veillez à executer cette commande souvent pour posseder la dernière version. 

```bash
git clone https://github.com/Bapt-Tech/Services.git
```
Cherchez où s'est enregistré le dossier ModSer.

Vous pouvez utiliser la commande "cd" pour ouvrir les dossiers et la commande "ls" pour afficher le contenu des dossiers.
```bash
cd /Changez/ce/texte/pour/arriver/dans/le/dossier/Modser
```
```bash
ls
```
8A. Identifiant : Guest1
8B. Mot de passe : PUwKN5e9mt5s9x2aCQAD
9. Pour les utilisateurs avancés, vous pouvez lire la référence suivante.

# Avancé

Dans le dossier "ModSer", tous les scripts sont présents et modifiables.

Le dossier "Logs" comporte comme son nom l'indique le fichier de logs.

Le fichier "PWD_DATA.bps" contient les identifiants et les mots de passe utilisés dans le LoginService

Vous pouvez modifier le code du serveur en ouvrant les fichiers présents dans le dossier "Templates" et les couleurs dans le dossier "Static".

