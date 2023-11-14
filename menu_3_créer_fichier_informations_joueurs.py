# -*- coding: utf-8 -*-
"""

Récupère les informations de tout les joueurs de l'équipe.

"""

# Import des différents modules :
import os
import urllib.request
import pandas as pd
from datetime import date, datetime
from bs4 import BeautifulSoup as bs


def get_info_player(url):
    """
    Fonction qui récupère les informations d'un joueur depuis une url.
    """

    # Récupération de la page du joueur :
    html = urllib.request.urlopen(url, timeout=5)

    # Création de l'objet soup :
    soup = bs(html, "html.parser")
    info_player = soup.find_all('div', {'class': 'single-info'})

    # Création d'un dictionnaire avec les informations du joueur :
    player_info_dict = {}
    for i in info_player:
        label = i.find("div", {"class": "st-label normal_font"}).text
        value = i.find("div", {"class": "st-value"}).text.strip()
        player_info_dict[label] = value

    return player_info_dict


def get_age(birthday_date):
    """
    Fonction qui renvoi un âge à partir d'une date de naissance.
    """

    today = date.today()
    birthday = datetime.strptime(birthday_date, "%d/%m/%Y")
    new_age = int(today.year - birthday.year)
    return new_age


def main():
    """
    Fonction principale.
    """

    # Récupération de la page :
    url = "https://www.bruleursdeloups.fr/la-meute/"
    html = urllib.request.urlopen(url, timeout=5)

    # Création de l'objet soup :
    soup = bs(html, "html.parser")
    players = soup.find_all('div', {'class': 'stm-list-single-player'})

    # Récupération des liens url des joueurs :
    link_players = []
    for p in players:
        link = p.find("a")['href']
        link_players.append(link)

    # Récupération des informations de tous les joueurs :
    master = []
    for url in link_players:
        info = get_info_player(url)
        master.append(info)

    # Création du DataFrame :
    df = pd.DataFrame(master)

    # Modifications du DataFrame :
    # Renomage de certaines colonnes :
    df = df.rename(columns={"#": "Numéro", "Name": "Nom",
                            "Nationality": "Nationalité",
                            "Taille": "Taille (cm)",
                            "Poids": "Poids (kg)"})

    # Retrait de la colonne "Age":
    df = df.drop(["Age", "Statut"], axis=1)

    # Formatage en titre des colonnes "Shoot" et "Nom":
    df["Shoot"] = df["Shoot"].str.title()
    df["Nom"] = df["Nom"].str.title()

    # Calcule de l'age des joueurs:
    df["Age"] = df["Naissance"][1:].apply(get_age)

    # Ajout de la position de l'entraineur
    df.loc[0, "Position"] = "Entraineur"

    # Formatage des colonnes "Poids" et "Taille" pour n'avoir que des nombres:
    df["Poids (kg)"] = df["Poids (kg)"].str.replace(
        r"(\d*)\s?kg", r"\1", regex=True)
    df["Taille (cm)"] = df["Taille (cm)"].str.replace(
        r"(\d*)\s?cm", r"\1", regex=True)

    # Réarangement de l'ordre des colonnes:
    df = df[["Numéro", "Nom", "Au club depuis", "Position",
             "Naissance", "Age", "Taille (cm)", "Poids (kg)", "Shoot"]]

    # Nettoie la colonne "Shoot" :
    df["Shoot"] = df["Shoot"].replace("Droit", "Droite")

    # Conversion des "NaN"
    df = df.convert_dtypes()

    # Tri du DataFrame par la colonne "Numéro"
    df = pd.concat([df[0:1], df[1:].sort_values(
        by=["Numéro"], key=lambda x: x.astype(int))])

    # Input pour le choix du nom de fichier :
    menu = ("Entrer un nom de ficher :\n"
            + "(Appuyer sur entrer pour garder la valeur par défaut "
            + "'informations_joueurs_BDL.csv')")
    print(menu)
    file_name = input() or "informations_joueurs_BDL.csv"
    end_verification_menu = False

    # Vérification de l'existance du nom du fichier :
    while not end_verification_menu and file_name in os.listdir("data"):
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

    # Export du DataFrame en csv :
    df.to_csv(f"data\\{file_name}", index=False, encoding="utf-8", sep=";")
    print(f"Fichier {file_name} enregistré.")


if __name__ == "__main__":
    main()
