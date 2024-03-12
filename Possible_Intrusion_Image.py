#!/bin/python3

from PIL import Image
import math
import subprocess

def entropie_image(image_path):
    #initialisation
    H = 0
    mon_dict = {}
    ls = list()
    P_couleur = list()
	
    #ouvrir l'image
    img = Image.open(image_path)
	
    largeur, hauteur = img.size
	
    #mettre les valeurs RVB dans une liste 
    tot_coul = hauteur*largeur
	
    for i in range(hauteur):
        for j in range(largeur):
            pixel = img.getpixel((j, i)) 
            ls.append(pixel)
			
    for i in ls:
        mon_dict[i] = mon_dict.get(i, 0)+1
	
    tot_coul = 0
    for v in mon_dict.values():
        tot_coul += v
		
    for k,v in mon_dict.items():
        P_couleur.append(v/tot_coul)
    
    for i in P_couleur:
        H -= i*math.log2(i)
    return H

def hibernate_image(image_path):
    subprocess.run(["icacls", image_path, "/inheritance:r", "/remove", "*"], check=True)

Oimage_path = input("entrez l'image originalle: ")
Timage_path = input("entrez l'image que vous voulez testez si originale: ")

#entropie de l'image originalle
HO = entropie_image(Oimage_path)
#entropie de l'image à tester
HT = entropie_image(Timage_path)

#comparaison
if HO == HT:
    print("L'image est original")
else:
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!INTRUSION POSSIBLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    while True:
        hib = input('do you want to hibernate it: ')
        if hib.upper() in ["HIBERNATE","YES","OK"]:
            hibernate_image(Timage_path)
            break
        elif hib.upper() == "NO":
            break
        else:
            print("please enter a valid command!!!")