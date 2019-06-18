import requests
import json
import time
import matplotlib.pyplot as plt
import numpy as np
import sys

crypto = "" # Nom de la crypto dont on fait les statistiques
borne1 = 0 # Borne inferieure de la plage de recherche
borne2 = 0 # Borne superieure de la plage de recherche
f = 0 # Fichier contenant les logs



data_base = []
adresses = []
nbTx = []
soldeTotal = []
delay = 0 # Respecter les 1 seconde pour le délai

class Account:
    adress = ""
    solde = 0
    nbTx = 0




def afficherMenu():
    quitter = 0
    while (not(quitter)):
        print ("--------------------------------- .: MENU :. ---------------------------------\n")
        print(" Etudier une cryptomonnaie --> 1\n")
        print(" Cryptomonnaies a etudier disponibles --> 2\n")
        print(" Aide --> 3\n")
        print(" Quitter --> 4\n")
        print("-------------------------------------------------------------------------------\n")

        choix = input()
        if (choix == "1"):
            getStats()

        if (choix == "2"):
            print("Exemple des cryptomonnais disponibles (les 10 premières)\n\nLitecoin -> LTC\nDash -> DASH\nZCoin -> XZC\nNPay Network -> NPAY\nPIVX -> PIV\nVertcoin -> VTC\nElercoin -> EMC\nPeercoin -> PPC\nFeathercoin -> FTC\nBitGreen -> BITG\n\nAller voir sur le site https://www.coinexplorer.net\ pour voir toutes les cryptomonnais disponnibles\n")

        if (choix == "3"):
            print("Ce programme permet de faire des statistiques sur une cryptomonnaie et de faire un graphique qui représente le nombre d'occurence d'une adresse sur les x transactions étudiees.\nDe plus un fichier texte logs_+nomdelacrypto.txt contient tous les logs des requetes effectuees avec l'API\n")

        if (choix == "4"):
            quitter = 1




def addEntry (adr_elem, solde_elem):
    exist = False
    id = 0

    for i in data_base:
            if i.adress == adr_elem :
                exist = True
                i.solde += solde_elem
                i.nbTx += 1
    if not(exist) :
        elem = Account()
        elem.adress = adr_elem
        elem.solde += solde_elem
        elem.nbTx = 1
        data_base.append(elem)





def getTxInfo(hash):
    print("HASH : " + hash)
    info = requests.get("https://www.coinexplorer.net/api/v1/"+crypto+"/transaction?txid="+str(hash))
    tx  = json.loads(info.text)
    addEntry(tx["result"]["vout"][0]["scriptPubKey"]["addresses"][0], tx["result"]["vout"][0]["value"])
    f.write(tx["result"]["vout"][0]["scriptPubKey"]["addresses"][0] + "," + str(tx["result"]["vout"][0]["value"]) + ",\n")



def getHashTx(id):
    result = requests.get("https://www.coinexplorer.net/api/v1/"+crypto+"/block?height="+str(id))

    txList = json.loads(result.text)

    time.sleep(delay)
    size =len(txList["result"]["tx"])
    for i in range (0, size):
        getTxInfo(txList["result"]["tx"][i])
        time.sleep(delay)





def getStats():
    global crypto, borne1, borne2, f
    crypto = input("Entrer la cryptomonnaie a etudier\n") # Nom de la crypto dont on fait les statistiques
    borne1 = int(input("Entrer la première borne de la plage a etudier\n"))
    borne2 = int(input("Entrer la seconde borne de la plage a etudier\n"))
    f = open("./logs_"+crypto+".txt", "w")

    for i in range (borne1, borne2 + 1):
        getHashTx(i)

    print(len(data_base))
    afficherGraphique()
    f.close()

def readFile():
    f = open("./logs_"+crypto+".txt", "r")
    lignes = f.readlines()


    for ligne in lignes:
        ligne = ligne.split(",")
        addEntry(ligne[0],float(ligne[1]))



def afficherGraphique():
    fig = plt.figure()

    for i in range (0, len(data_base)):
        adresses.append(i)
        nbTx.append(data_base[i].nbTx)
        soldeTotal.append(data_base[i].solde)


    width = 0.35
    r1 = range(len(data_base))
    r2 = [x + width for x in r1]
    plt.xticks(np.arange(min(adresses), max(adresses) + 1, 1))


    l1 = plt.bar(r1, nbTx, width, color ='dodgerblue')
    ax2 = plt.gca().twinx()
    l2 = plt.bar(r2, soldeTotal, width, color = 'darkorange')

    plt.legend([l1,l2], ['Nombre de transactions', 'Solde total (en '+crypto+')'])
    plt.title('Nombre de transactions et solde total par adresse')

    plt.show()



afficherMenu()







