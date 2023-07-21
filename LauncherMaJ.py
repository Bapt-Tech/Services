###LauncherMaJ
###21/07/2023
###12:41
###Bapt-Tech

from ModSer import ModCallSer
from time import sleep
#import 

print("Bienvenue sur le launcher des services")
sleep(2)
print("Le launcher n'est pas disponible pendant les mises à jour")
print("Le LoginService est également indisponible donc aucune phase d'identification ne sera effectuée durant la mise à jour.")
sleep(2)
ModCallSer.Services()