import requests
import json
import time
import matplotlib.pyplot as plt
import numpy as np
import sys

crypto = "" # Nom de la crypto dont on fait
borne1 = 0
borne2 = 0







data_base = []
adresses = []
nbTx = []
delay = 0 # Respecter les 1 seconde pour le délai sauf si on est un THUG !!!!

class Account:
    adress = ""
    solde = 0
    nbTx = 0




def afficherMenu():
    quitter = 0
    while (not(quitter)):
        print("Etudier une cryptomonnaie --> 1\n")
        print("Cryptomonnaies a etudier disponibles --> 2\n")
        print("Aide --> 3\n")
        print("Quitter --> 4\n")

        choix = input()
        if (choix == "1"):
            getStats()
        if (choix == "2"):
            print("A venir ... Aller voir sur le site https://www.coinexplorer.net")
        if (choix == "3"):
            print("Ce programme permet de faire des statistiques sur une cryptomonnaie et de faire un graphique qui représente le nombre d'occurence d'une adresses sur les x transactions étudiées")
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
    print("SALUT : " + hash)
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
    global crypto, borne1, borne2
    crypto = input("Entrer la cryptomonnaie a etudier\n") # Nom de la crypto dont on fait
    borne1 = int(input("Entrer la première borne de la plage a etudier\n"))
    borne2 = int(input("Entrer la seconde borne de la plage a etudier\n"))

    for i in range (borne1, borne2 + 1):
        getHashTx(i)

    print(len(data_base))
    afficherGraphique()

def readFile():
    f = open("D:\Documents\Etudes\Projet_Pascal\logs.txt", "r")
    lignes = f.readlines()


    for ligne in lignes:
        ligne = ligne.split(",")
        print(ligne)
        addEntry(ligne[0],float(ligne[1]))



def afficherGraphique():
    fig = plt.figure()

    for i in range (0, len(data_base)):
        adresses.append(i)
        nbTx.append(data_base[i].nbTx)




    width = 0.25
    plt.xticks(np.arange(min(adresses), max(adresses) + 1, 1.0))


    plt.bar(range(len(data_base)), nbTx, width, color ='b')
    plt.show()


f = open("D:\Documents\Etudes\Projet_Pascal\logs.txt", "w")
afficherMenu()
f.close()
# readFile()







