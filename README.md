# Projet-ZZ1
Projet de première année ISIMA, Bouchut Florian et Nifosi Antony

## Utilisation du script Python (optimisé :) !!!)
Si l'on souhaite utilier le scrypt Python il suffit de suivre ce petit tutoriel pour installer Python3 ainsi que les modules complémentaires necessaires au lancement du script :

**Installer Python 3.6 Mac** 

**brew install python3** //Permet d'installer python 3  

**pip3 install request** // Permet d'installer le module request  

**pip3 install matploblib** // Permet d'installer le module matploblib  

**python3 script_python.py** // Permet de lancer le script  

A la fin de l'exécution du script un fichier log est créé qui contient chaque adresse ainsi que le montant de la transaction. 

Le graphique représente le nombre d'occurrence d'une adresse sur les x premières adresses de la monnaie sélectionnée 

PS : Comme expliqué l'APi utilisée est limitée à une requête par seconde mais on peut mettre la variable delay dans le programme Python à 0 cela semble aller à la vitesse maximum autorisée par l'API et qui est supérieure à une requète toutes les secondes.

## Utilisation du script JS + du programme C (pas optimisé :( !!!)
Si l'on souhaite utiliser le script JS il suffit de le lancer dans un navigateur dans Chrome par exemple et une fois le script exécuté sauvegarder la console (clique droit "Save as" dans Google Chrome et appelait le fichier "logs_tx.log".

Ensuite il suffit de lancer le programme C qui va lire le fichier logs_tx.log et écrire les résultats dans un fichier result.txt sous la forme "occurence,gains_totaux,"

On peut ensuite importer ces données sous un tableur pour avoir un graphique.

PS : De base le script JS et le programme C sont programmés pour annalyser 1000 transactions de Peercoin si l'on souhaite modifier la cryptomonnaie aller directement le modifier dans le script JS et si l'on souhaite modifier le nombre de transactions le modifier dans le script JS et le programme C
