# Calculatrice Python

Ce projet est une simple calculatrice implémentée en Python, accompagnée de tests unitaires pour garantir la fiabilité des fonctionnalités.

## Fonctionnalités

La calculatrice prend en charge les opérations de base telles que l'addition, la soustraction, la multiplication et la division. De plus, elle gère également les opérations avancées telles que la racine carrée.

## Installation

1. Clônez le dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/calculatrice-python.git
   cd calculatrice-python
   ```
2. Installer les dépendences
   ```
   pip install
   ```

## Lancement application

1. Lancer la calculate :
   `python main.py`

2. Lancer les tests :
   `pytest tests/test.py`

### Membres du groupe

    -Arnaud Beaulieu
    -Loris PLanté
    -Paul Decalf
    -Paul Serrano

#### Description du projet

Nous avons développé une calculatrice en Python dans le cadre d'un de TP "Tests Unitaires et la Qualité du Code en Python".
L'utilisateur rentre une expression mathématique avec chaque élément (nombres et opérateurs) séparés d'un ou plusieurs espaces.
Le programme renvoie le résultat, et s'arrête.

Deux fichiers :

    - main.py, avec une classe MathOperation. Cette classe possède des méthodes de calcul (addition, soustraction, multiplication, division, puissance et modulo), et une fonction pour déclencher l'intéraction utilisateur et les méthodes de calcul.

    - test.py, qui s'occuppe de tester les méthodes de calcul, et la méthode d'intéraction utilisateur. Nous utilisons la librairie pytest, et testons chaque méthode avec divers set de données, justes et fausses.

pytest nous permet aussi de générer un rapport de test au format HTML, directement accessible depuis une adresse localhost.

Nous utilisons sonarscanner et sonarqube pour tester plus en profondeur notre programme, et avoir une meilleure visualisation des points à améliorer.
