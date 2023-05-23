# Mercadona store offers
# A Python Django Student project 


Une application de commerce électronique simple basée sur Django, Heroku, Postgres et AWS S3 pour le stockage de médias.

## Installation et configuration

1. Clonez le dépôt : `git clone https://github.com/Filipouzo/mercadona-studi.git`
2. Allez dans le répertoire du projet : `cd src`
3. Installez les dépendances nécessaires : `pip install -r requirements.txt`
4. Exécutez les migrations : `python manage.py migrate`
5. Lancez le serveur de développement : `python manage.py runserver`

## Structure de l'application

- L'interface utilisateur est simple et intuitive, permettant aux utilisateurs de naviguer facilement à travers les produits.
- L'application est constituée de plusieurs modules Django :

- `catalogue`: Gère les produits et les catégories.
- 'login' : Atteint la page d'adminitration (après authentification) pour gérer les promotions de produit.


## Structure du code
Le code back-end est basé sur le framework Django.
Le code front-end utilise Bootstrap pour le style et JavaScript pour la dynamique.
Les fichiers statiques et les médias sont hébergés sur AWS S3.
L'application est déployée sur Heroku avec une base de données Postgres.

## Structure de la base de données
Modèle Product pour représenter les produits.
Modèle Category pour représenter les catégories de produits.
Modèle Promotion pour représenter les promotions sur les produits.

Pour toute question ou préoccupation, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.