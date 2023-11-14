# Équipe Data Scraper

## Aperçu

Ce programme Python est conçu pour collecter diverses données du site web [Bruleurs de Loups - La Meute](https://www.bruleursdeloups.fr/la-meute). Les données collectées comprennent des informations sur les joueurs de l'équipe telles que leurs noms, numéros, dates de naissance, positions, et plus encore. Le programme propose une interface basée sur un menu pour effectuer différentes opérations liées aux données collectées.

## Configuration requise

- Version de Python : 3.8.10

## Dépendances

- pandas=1.5.2
- beautifulsoup4=4.11.1

## Auteurs

- Merlendo

## Utilisation

Pour exécuter le programme, lancez le fichier `menu_bdl.py`. Le programme s'exécutera automatiquement dans l'invite de commandes de Windows. Les fichiers de données sont stockés dans le dossier `data\`, qui est créé lors de la première initialisation du programme.

## Options du menu

1. Afficher la liste des joueurs de l'équipe par ordre alphabétique de leur nom de famille.
2. Afficher la liste des joueurs de l'équipe par ordre de leur numéro.
3. Récupérer les données de l'équipe dans un fichier CSV.
4. Récupérer les données individuelles des joueurs dans des dossiers séparés.
q. Quitter.

## Fichiers de code

1. menu_bdl.py
2. menu_1_afficher_liste_joueurs_par_nom
3. menu_2_afficher_liste_joueurs_par_numero
4. menu_3_créer_fichier_informations_joueurs
5. menu_4_créer_dossiers_joueurs
