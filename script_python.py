import requests
import json
import time
import matplotlib.pyplot as plt
import numpy as np


crypto = "PPC"
data_base = []
adresses = []
nbTx = []
delay = 0 # Respecter les 1 seconde pour le délai sauf si on est un THUG !!!!

class Account:
    adress = ""
    solde = 0
    nbTx = 0


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

    for i in range (0, len(txList["result"]["tx"])):
        getTxInfo(txList["result"]["tx"][i])
        time.sleep(delay)





def getStats(taille):
    for i in range (1, taille + 1):
        getHashTx(i)


def readFile():
    f = open("D:\Documents\Etudes\Projet_Pascal\logs.txt", "r")
    lignes = f.readlines()


    for ligne in lignes:
        ligne = ligne.split(",")
        print(ligne)
        addEntry(ligne[0],float(ligne[1]))


f = open("D:\Documents\Etudes\Projet_Pascal\logs.txt", "w")
getStats(1000)
print(len(data_base))
f.close()

# readFile()



f.close()






fig = plt.figure()

for i in range (0, len(data_base)):
    adresses.append(i)
    nbTx.append(data_base[i].nbTx)




width = 0.25
plt.xticks(np.arange(min(adresses), max(adresses) + 1, 1.0))


plt.bar(range(len(data_base)), nbTx, width, color ='b')
plt.show()


