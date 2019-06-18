# Projet-ZZ1
Projet de première année ISIMA, Bouchut Florian et Nifosi Antony

## Structure du GitHub : ##

**logs.txt :** Fichier donner par l'éxécution du programme C
**main.c :** Programme C qui génère un fichier texte importable sous un tableur.
**script.js :** Programme JavaScript pouvant être lancer dans un navigateur pour récupérer les informations sont les 1000 premières transactions (dans la console du navigateur)
**script_python.py :** Programme Python pouvant générer un graphique sur les cryptomonnais du site coinexplorer sur la plage souhaitée

## Utilisation du script Python (optimisé :) !!!)
Si l'on souhaite utilier le scrypt Python il suffit de suivre ce petit tutoriel pour installer Python3 ainsi que les modules complémentaires nécessaires au lancement du script :

**Installer Python 3.6 Mac** 

**brew install python3** //Permet d'installer python 3  

**pip3 install request** // Permet d'installer le module request  

**pip3 install matploblib** // Permet d'installer le module matploblib  

**python3 script_python.py** // Permet de lancer le script  

A la fin de l'exécution du script un fichier log est créé qui contient chaque adresse ainsi que le montant de la transaction. 

Le graphique représente le nombre d'occurrence d'une adresse sur les x premières adresses de la monnaie sélectionnée.

**IMPORTANT :** Ne pas commencer à la première adresse car elle ne correspond pas vraiement à une transaction. Si l'on souhaite faire les 1000 premières transactions mettre la plage (1, 1001) dans le programme.

**IMPORTANT 2 :** Bien penser à mettre le chemin où l'on souhaite avoir les résultats du programme dans le code python (ligne 103) de base il ira dans le home directory.

PS : Comme expliqué l'API utilisée est limitée à une requête par seconde mais on peut mettre la variable delay dans le programme Python à 0 cela semble aller à la vitesse maximum autorisée par l'API et qui est supérieure à une requète toutes les secondes.

## Utilisation du script JS + du programme C (pas optimisé :( !!!)
Si l'on souhaite utiliser le script JS il suffit de le lancer dans un navigateur dans Chrome par exemple. Il est important de noter que lors de l'execution du script l'onglet sera "bloqué" tant que le script n'a pas fini d'éxécuter toutes les requètes. Si l'on souhaite voir l'avancement il faut : Ouvrir un nouvel onglet -> ouvrir la console -> et enfin lancer le script.
Une fois le script exécuté sauvegarder la console (clique droit "Save as" dans Google Chrome et appelait le fichier "logs_tx.log".

Ensuite il suffit de lancer le programme C qui va lire le fichier logs_tx.log et écrire les résultats dans un fichier result.txt sous la forme "occurence,gains_totaux,"

On peut ensuite importer ces données sous un tableur pour avoir un graphique.

PS : De base le script JS et le programme C sont programmés pour annalyser 1000 transactions de Peercoin si l'on souhaite modifier la cryptomonnaie aller directement le modifier dans le script JS et si l'on souhaite modifier le nombre de transactions le modifier dans le script JS et le programme C
