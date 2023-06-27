import platform

def determiner_os():
    systeme_exploitation = platform.system()
    if systeme_exploitation == "Windows":
        return "Windows"
    elif systeme_exploitation == "Darwin":
        return "Mac OS"
    elif systeme_exploitation == "Linux":
        return "Linux"
    else:
        return "Système d'exploitation inconnu"

print("Le script s'exécute sur :", determiner_os())
