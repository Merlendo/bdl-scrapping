# -*- coding: utf-8 -*-
"""

Créer des dossiers pour tout les joueurs de l'équipe avec leurs informations
et photos.

"""

# Import des différents modules :
import os
import urllib.request
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

    # Création du dossier "Joueurs"
    if not os.path.exists("data\\Joueurs"):
        os.mkdir("data\\Joueurs")

    # Parcours des joueurs de l'équipe :
    for p in players:
        player_name = p.find('div', {'class': 'player-title'}).text.title()
        img_player = p.find("img")["src"]
        url_player = p.find("a")["href"]

        # Création d'un dossier avec le nom du joueur :
        if not os.path.exists(f"data\\Joueurs\\{player_name}"):
            print(f"Création du dossier du joueur {player_name}")
            os.mkdir(f"data\\Joueurs\\{player_name}")

            # Téléchargement de l'image du joueur :
            urllib.request.urlretrieve(
                img_player,
                (f"data\\Joueurs\\{player_name}\\{player_name}.jpg"))

            # Téléchargement des informations du joueur :
            with open(f"data\\Joueurs\\{player_name}\\{player_name}.txt", "w",
                      encoding="utf8") as f:
                for k, v in get_info_player(url_player).items():
                    f.write(f"{k} : {v}\n")
        else:
            print(f"Dossier joueur {player_name} existe déjà.")


if __name__ == "__main__":
    main()
