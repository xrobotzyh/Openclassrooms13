# Introduction

Orange County Lettings est une start-up dans le secteur de la location immobilière. La start-up est actuellement en phase d'expansion aux États-Unis. L'objectif de ce projet est d'améliorer le site web existant (dépôt GitHub : OC Lettings) dans les domaines suivants :

- Réduction de diverses dettes techniques sur le projet
- Refonte de l'architecture modulaire
- Ajout d'un pipeline CI/CD utilisant CircleCI et Render
- Surveillance de l'application et suivi des erreurs via Sentry

# Installation

## Récupération du projet sur votre machine locale

### Clonez le dépôt sur votre machine.

```
git clone https://github.com/xrobotzyh/Openclassrooms13.git
```

### Accédez au répertoire cloné.

```bash
cd Openclassrooms13
```

## Création d'un environnement virtuel

### Créez l'environnement virtuel nommé env.

```bash
python3 -m venv venv
```

## Activation et installation de votre environnement virtuel

### Activez votre environnement virtuel nouvellement créé, env.

```bash
source venv/bin/activate
```

### Installez les paquets répertoriés dans le fichier requirements.txt.

```bash
pip install -r requirements.txt
```

# Utilisation
## Démarrage du serveur local

```bash
python manage.py runserver
```
## Linting

```bash
flake8
```

## Pytest

```bash
pytest
```

## Panneau d'administration

Accédez à http://127.0.0.1:8000/admin Connectez-vous avec l'utilisateur yuhao, mot de passe 1234567890

# Déploiement

Ce dont vous avez besoin

    Un compte GitHub
    Un compte CircleCI
    Un compte DockerHub
    Un compte Render
    Un compte Sentry

## Description du fonctionnement du pipeline CircleCi

Lors d'un commit sur une branche autre que master, exécution du job suivant :

    build-and-test qui est composé des actions (run) suivantes :
    Python/install-packages : installation des paquets nécessaires pour exécuter le projet
    Run Tests : exécution des tests unitaires avec la commande pytest

Lors d'un commit sur la branche master, exécution des jobs suivants :

    build-and-test comme décrit ci-dessus
    build_and_push_docker_image qui est composé des actions (run) suivantes :
    Build Docker image : création d'une image Docker à partir du code source via Git
    Push Docker Image : téléversement de l'image créée vers Docker Hub en deux étapes : d'abord avec le tag correspondant au "hash" du commit CircleCI, puis avec le tag "latest"
    deploy composé de l'action (run) suivante :
    Start container and push to Render : lancement de la construction de l'application sur Render via Git

### Workflow

    Le job build-and-test est exécuté lorsqu'une modification est apportée à n'importe quelle branche du projet.
    Les jobs build_and_push_docker_image et deploy ne sont exécutés que lorsqu'une modification est apportée à la branche master.
    Le job build_and_push_docker_image n'est exécuté que lorsque le job build-and-test est exécuté avec succès.
    Le job deploy n'est exécuté que lorsque le job build_and_push_docker_image est exécuté avec succès.

### Variables d'environnement

Création des variables d'environnement au niveau du projet :
Nom de la variable	Service	Description
RENDER_DEPLOY_TEST	CircleCI	URL de déclenchement    Render Webhook
XROBOTZYH_DOCKERHUB	CircleCI	Nom d'utilisateur du compte Docker
XROBOTZYH_PWD_DOCKERHUB	CircleCI	Mot de passe du compte Docker
SECRET_KEY	CircleCI	Clé secrète Django
SENTRY_DSN	CircleCI	Token interne d'intégration Sentry
SECRET_KEY	Render	Clé secrète Django
SENTRY_DSN	Render	Token interne d'intégration Sentry
ENV	Render	Environnement ('production' ou 'dev')

| Nom des Variables   | Service  | Description                           |
|---------------------|----------|---------------------------------------|
| `RENDER_DEPLOY_TEST` | CircleCI | URL de déclenchement    Render Webhook        |
| `XROBOTZYH_DOCKERHUB`   | CircleCI | Nom d'utilisateur votre compte Docker |
| `XROBOTZYH_PWD_DOCKERHUB`      | CircleCI | Mot de passe du compte Docker          |
| `SECRET_KEY`    | CircleCI | Clé secrète Django        |
| `SENTRY_DSN`   | CircleCI | oken interne d'intégration Sentry           |
| `SENTRY_DSN`        | Render | Token interne d'intégration Sentry    |
| `SECRET_KEY`        | Render  | Clé secrète Django                    |
| `ENV`               | Render   | Environnement ('production' ou 'dev') |


# Accès à l'application

## Local

Pour un déploiement local via le code source ou l'image Docker, veuillez fournir les variables d'environnement suivantes :

```bash
SECRET_KEY=your_django_secret_key
SENTRY_DSN=your_sentry_dsn_key
ENV=production
```
## Docker

Vous pouvez par exemple placer les deux lignes ci-dessus dans un fichier env_file à la racine de votre projet pour exécuter l'image Docker de la manière suivante :

```bash
docker pull <docker_image:tag>
docker run --env-file=env_file -i -p 8000:8000 <docker_image>
```
docker_image : accédez à la dernière image créée en utilisant le tag "latest", ou bien choisis