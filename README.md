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

1. Ouvrez un terminal. Pour savoir comment ouvrir un terminal, regardez la mention en bas du texte. 

2. Assurez vous que Git est installé via cette commande :
 ```bash
git version
```
3. Si Git est installé, la version de Git s'affichera. Sinon, la commande ne sera pas reconnue.

4. Executez cette commande pour recevoir une copie des services. Veillez à executer cette commande souvent pour posseder la dernière version. 

```bash
git clone https://github.com/Bapt-Tech/Services.git
```
5. Cherchez où s'est enregistré le dossier ModSer.

6. Vous pouvez utiliser la commande "cd" pour ouvrir les dossiers et la commande "ls" pour afficher le contenu des dossiers.
```bash
cd /Changez/ce/texte/pour/arriver/dans/le/dossier/Modser
```
```bash
ls
```

7. Pour vérifier que vous avez en votre possesion une copye de Python, vous pouvez executer cette commande :
```bash
python3 --version
```
Si la commande n'est pas reconnue, regardez la mention en bas du texte.


8. Via cette commande, vous pouvez executer le fichier "ServicesLauncher.py"
```bash
python3 ServicesLauncher.py
```

9. Les identifiants demandés sont :
╔═════════╦═════════╦═══════════════════╗
║Statut   ║Pseudo   ║MdP                ║
╠═════════╬═════════╬═══════════════════╣
║Admin    ║Admin    ║Admin              ║
╠═════════╬═════════╬═══════════════════╣
║Basique  ║Guest1   ║
╚═════════╩═════════╩═══════════════════╝

# Avancé

Dans le dossier "ModSer", tous les scripts sont présents et modifiables.

Le dossier "Logs" comporte comme son nom l'indique le fichier de logs.

Le fichier "PWD_DATA.bps" contient les identifiants et les mots de passe utilisés dans le LoginService

Vous pouvez modifier le code du serveur en ouvrant les fichiers présents dans le dossier "Templates" et les couleurs dans le dossier "Static".

# Aide Rapide

## Comment ouvrir un terminal ?

Pour Windows : Accedez au menu Démarrer puis entrez "cmd" ou "terminal"
Pour Mac : Accedez au menu LaunchPad et recherchez "Terminal" ou dans Finder, ouvrez le dossier "Applications" puis "Utilitaires" et cliquez sur "Terminal"

## Comment installer Python ?

Vous pouvez [Télécharger Python](https://www.python.org/) depuis le site officiel.

## Comment installer Git ?

Executez cette commande : 
```bash
winget install --id Git. Git -e --source winget
```
