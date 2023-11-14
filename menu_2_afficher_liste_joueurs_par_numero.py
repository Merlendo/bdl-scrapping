# -*- coding: utf-8 -*-
"""

Affiche la liste des joueurs sans l'entraineur par ordre de leur numéro.
Avec la possibilité de sauvegarder la liste en .txt.

"""

# Import des différents modules :
import os
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs


def main():
    """
    Fonction principale.
    """

    # Accès à une page web à partir de son URL :
    url = "https://www.bruleursdeloups.fr/la-meute"
    page = urllib.request.urlopen(url)

    # Récupération du code html entier de la page web :
    soup = bs(page, "html.parser")

    # Récupération des noms de joueurs et de leur numéro :
    players_list = []
    data_player = soup.find_all("div", {"class": "stm-list-single-player"})
    for player in data_player:
        player_name = player.find(
            "div", {"class": "player-title"}).text.title().strip().split()
        player_number = player.find(
            "div", {"class": "player-number"}).text.strip()
        players_list.append([player_number] + player_name)

    # Création DataFrame grâce à pandas :
    players_df = pd.DataFrame(players_list, columns=[
                              "Numéro", "Prénom", "Nom"])[1:]

    # Tri des joueurs par leur numéro :
    players_df = players_df.sort_values(
        by=["Numéro"], key=lambda x: x.astype(int))

    # Affiche la liste des joueurs triés :
    print(players_df.to_string(index=False))

    # Demande d'enregistrement du fichier :
    save_menu = ("Voulez vous enregistrer le fichier (O/N) ?")
    print(save_menu)
    end_save_menu = False

    while not end_save_menu:
        reponse = input().strip().upper()
        if reponse == "O":
            # Input pour le choix du nom de fichier :
            menu = ("Entrer un nom de ficher :\n"
                    + "(Appuyer sur entrer pour garder la valeur par défaut "
                    + "'liste_joueurs_BDL_num.txt')")
            print(menu)
            file_name = input() or "liste_joueurs_BDL_num.txt"
            end_verification_menu = False

            # Vérification de l'existance du nom du fichier :
            while (not end_verification_menu and
                   file_name in os.listdir("data")):
                verification_menu = (f"Le fichier '{file_name}' existe déjà. "
                                     + "Souhaitez-vous l'écraser (O/N) ? ")
                print(verification_menu)
                reponse = input().strip().upper()
                if reponse == "O":
                    end_verification_menu = True
                elif reponse == "N":
                    file_name = input("Entrer un nouveau nom de ficher :\n")
                else:
                    print("Choix invalide.")

            # Ecriture du dataframe dans un fichier .txt :
            players_df.to_csv(
                f"data/{file_name}",
                index=False, header=False, encoding="utf-8", sep=" ")
            print(f"Fichier {file_name} enregistré.")

            # Sortie de la boucle d'enregistrement :
            end_save_menu = True

        elif reponse == "N":
            end_save_menu = True
            print("\nFichier non enregistré.")
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
