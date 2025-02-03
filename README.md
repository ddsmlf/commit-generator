# AUTO push

## Table des matières
1. [Introduction](#introduction)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Automatisation avec alias](#automatisation-avec-alias)
6. [Dépannage](#dépannage)

## Introduction
Ce projet automatise la génération et le push de scripts Python sur un dépôt GitHub en utilisant le modèle `deepseek-coder` d'Ollama. Le script génère un fichier Python basé sur un prompt prédéfini, l'ajoute au dépôt, le commit et le push automatiquement.

## Prérequis
- Python 3.10
- Ollama installé et configuré
- Git installé et configuré
- Accès à un dépôt GitHub

## Installation
1. Clonez le dépôt sur votre machine locale :
    ```bash
    git clone <URL_DU_DEPOT>
    ```
2. Accédez au dossier du projet :
    ```bash
    cd /home/melissa/Documents/automat-gh/AUTO
    ```

## Utilisation
1. Exécutez le script pour générer et pousser un nouveau fichier Python :
    ```bash
    python3 generate_code.py
    ```
2. Le script va :
    - Vérifier et télécharger le modèle `deepseek-coder` si nécessaire.
    - Générer un script Python basé sur un prompt prédéfini.
    - Créer un fichier avec un nom unique incluant un timestamp.
    - Ajouter, commit et push le fichier sur le dépôt GitHub.

## Automatisation avec alias
Pour simplifier l'exécution du script, vous pouvez créer un alias dans votre terminal :
1. Ouvrez votre fichier de configuration de shell (par exemple, `~/.bashrc` ou `~/.zshrc`).
2. Ajoutez la ligne suivante :
    ```bash
    alias mkstat="python3 /home/melissa/Documents/automat-gh/AUTO/generate_code.py"
    ```
3. Rechargez votre fichier de configuration de shell :
    ```bash
    source ~/.bashrc
    ```
4. Maintenant, vous pouvez exécuter le script avec la commande `mkstat`.

## Dépannage
- Si le modèle `deepseek-coder` n'est pas téléchargé correctement, assurez-vous que Ollama est installé et configuré correctement.
- Si le push Git échoue, vérifiez vos configurations Git et assurez-vous que vous avez les permissions nécessaires pour pousser sur le dépôt.