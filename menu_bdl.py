# -*- coding: utf-8 -*-
"""

Menu principal de l'appplication.

"""

import os
import menu_1_afficher_liste_joueurs_par_nom
import menu_2_afficher_liste_joueurs_par_numero
import menu_3_créer_fichier_informations_joueurs
import menu_4_créer_dossiers_joueurs


menu = ("Faites votre choix dans le menu suivant :\n"
        + "(1) Afficher la liste des joueurs de l’équipe par ordre"
        + " alphabétique de leur nom de famille.\n"
        + "(2) Afficher la liste des joueurs de l’équipe par ordre"
        + " de leur numéro.\n"
        + "(3) Récupérer les données de l’équipe dans un fichier CSV.\n"
        + "(4) Récupérer les données individuelles des joueurs"
        + " dans des dossiers séparés.\n"
        + "(q) Quitter.")

menu_return = "\nAppuyer sur Entrée pour retourner au menu."

# Création du dossier "data" :
if not os.path.exists("data"):
    os.mkdir("data")

# Initialisation du menu :
fin_programme = False
while not fin_programme:
    print("\033[H\033[J")  # Nettoie la console Spyder ou l'invité de commande.
    print(menu)
    reponse = input().strip().lower()
    if reponse == "1":
        menu_1_afficher_liste_joueurs_par_nom.main()
        input(menu_return)
    elif reponse == "2":
        menu_2_afficher_liste_joueurs_par_numero.main()
        input(menu_return)
    elif reponse == "3":
        menu_3_créer_fichier_informations_joueurs.main()
        input(menu_return)
    elif reponse == "4":
        menu_4_créer_dossiers_joueurs.main()
        input(menu_return)
    elif reponse == "q":
        fin_programme = True
    else:
        print("Choix invalide.")
        input(menu_return)
