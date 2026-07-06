# Agent IA DevOps Full-stack

Plateforme pédagogique DevOps et Full-Stack avec un assistant IA, des modules de formation, des cas pratiques, et des démonstrations vidéo.

## Objectif pédagogique

Ce projet vise à créer un environnement d'apprentissage actif autour de la méthodologie **PractiKa** :

- `Pratique` : des cas concrets comme Ubuntu 24.10, Shinobi et caméras Axis IP.
- `Compréhension` : explication des concepts DevOps, CI/CD, conteneurs et infrastructure.
- `Documentation` : ressources structurées, vidéos et synthèse pédagogique.
- `Pédagogie active` : tutoriel en ligne et assistant IA pour guider l'utilisateur.

## Contenu du projet

- `index.html` : page d'accueil avec navigation vers la formation, les vidéos, les ressources et la page À propos.
- `training.html` : parcours de formation avec modules, cas pratiques et assistant IA flottant.
- `demonstrations.html` : galerie de démonstrations vidéo pédagogique.
- `widget.html` : page À propos de l'agent IA DevOps.
- `devfullstack.py` : serveur Flask principal.
- `main.js` : script d'interaction possible pour l'interface utilisateur.

## Architecture technique

- Serveur Flask pour livrer les pages HTML et exposer l'endpoint `/assistant`.
- Intégration de l'API OpenAI / DeepSeek via la bibliothèque `openai`.
- Intégration du SDK `anthropic` pour guider la sécurité des prompts et renforcer les bonnes pratiques.

## Dépendances

Ce projet nécessite :

- Python 3.13+
- Flask
- OpenAI
- anthropic

Les dépendances sont listées dans `requirements.txt`.

## Installation locale

1. Créez un environnement virtuel :

```bash
python3 -m venv venv
```

2. Activez l'environnement :

```bash

```

3. Installez les dépendances :
Avant : toujours faire
python3 -m pip install --upgrade pip
FLASK_ENV=development
FLASK_DEBUG=1


```bash
pip install -r requirements.txt
```

4. Configurez les variables d'environnement :

```bash
export OPENAI_API_KEY="votre_cle_api"
```

Le serveur accepte aussi `OPENAI_ADMIN_KEY`, `DEEPSEEK_API_KEY` ou `API_KEY`.

## Lancement

```bash
python3 devfullstack.py
```

Accédez ensuite à `http://127.0.0.1:5000`.

## Sécurité et bonnes pratiques

- Ne stockez jamais de clés API directement dans le code.
- Utilisez des variables d'environnement et des secrets GitHub.
- Le SDK `anthropic` est intégré pour renforcer les aspects de sécurité, de prompt design et de gouvernance.
- Validez toujours les dépendances avant déploiement.

## Déploiement GitHub

Ce projet est prêt pour un dépôt GitHub sous le compte `Kamilou52`.

1. Créez un repository GitHub et poussez les fichiers :

```bash
git init
git add .
git commit -m "Initial commit - Agent IA DevOps Full-stack"
git remote add origin https://github.com/Kamilou52/<nom-du-repo>.git
git push -u origin main
```

2. Le workflow GitHub Actions `/.github/workflows/ci.yml` effectue :
   - l'installation des dépendances,
   - la validation des fichiers Python,
   - la compilation du projet.

3. Le workflow `/.github/workflows/deploy.yml` déploie automatiquement sur Render lorsque :
   - `main` reçoit un push,
   - ou en manuel via `workflow_dispatch`.

4. Ajoutez les secrets GitHub :
   - `OPENAI_API_KEY`
   - `OPENAI_ADMIN_KEY` ou `DEEPSEEK_API_KEY` si nécessaire
   - `RENDER_API_KEY`
   - `RENDER_SERVICE_ID`

## Déploiement Render via GitHub Actions

Pour utiliser le déploiement Render :

1. Créez un service Web sur Render pour votre application Flask.
2. Copiez l'ID du service Render (format `srv-...`).
3. Dans les Secrets du repository GitHub, ajoutez :
   - `RENDER_API_KEY`
   - `RENDER_SERVICE_ID`

Le workflow `deploy.yml` appelle l'API Render pour lancer un nouveau déploiement.

## Déploiement recommandé

Pour un déploiement en production, vous pouvez utiliser :

- Render
- Railway
- Fly.io
- Azure App Service
- AWS Elastic Beanstalk

Le projet est conçu pour un serveur WSGI Python simple et peut être déployé en tant qu'application Flask.

## Aspects pédagogiques inclus

- Méthodologie `PractiKa` dans `training.html`.
- Cas pratiques concrets et environnement Ubuntu.
- Galerie de démonstrations vidéo guidée.
- Assistant IA pour interaction et rétroaction.
- Force du learning-by-doing avec des ressources actionnables.

## Contribution

- Ajoutez des modules supplémentaires.
- Renforcez les cas pratiques.
- Documentez les retours d'expérience et les améliorations didactiques.

---

> Projet préparé pour un déploiement GitHub et une utilisation pédagogique complète, avec mise en place de la sécurité et de la gouvernance des prompts.
