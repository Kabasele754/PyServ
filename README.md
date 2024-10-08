# PyServ - Serveur Python Personnalisé

PyServ est un serveur web Python léger et personnalisable, conçu pour fournir une solution simple et efficace pour les petits projets web.

## Fonctionnalités

- Serveur HTTP personnalisé basé sur le module `http.server` de Python
- Gestion de base de données avec SQLite
- Système de templates pour les pages HTML
- Gestion des ressources statiques (CSS, JavaScript)
- Formulaire de contact avec stockage des données

## Structure du Projet

```
pyServ/
├── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── contact.db
└── server.py
```

## Prérequis

- Python 3.6 ou supérieur

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-username/pyserv.git
   cd pyserv
   ```

2. (Optionnel) Créez et activez un environnement virtuel :
   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances (si nécessaire) :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le serveur :
   ```
   python server.py
   ```

2. Ouvrez votre navigateur et accédez à `http://localhost:8080`

## Personnalisation

- Modifiez les fichiers HTML dans le dossier `templates/` pour changer le contenu des pages
- Ajustez le style dans `static/css/style.css`
- Personnalisez le comportement JavaScript dans `static/js/script.js`
- Modifiez `server.py` pour ajouter de nouvelles fonctionnalités ou routes

## Les captures

![Screenshot 2024-10-08 at 12.57.52 in the afternoon.png](static%2Fimg%2FScreenshot%202024-10-08%20at%2012.57.52%20in%20the%20afternoon.png)

![Screenshot 2024-10-08 at 12.58.07 in the afternoon.png](static%2Fimg%2FScreenshot%202024-10-08%20at%2012.58.07%20in%20the%20afternoon.png)

![Screenshot 2024-10-08 at 12.57.31 in the afternoon.png](static%2Fimg%2FScreenshot%202024-10-08%20at%2012.57.31%20in%20the%20afternoon.png)


## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.# PyServ
