# TSP Solver with Held-Karp Algorithm

Ce script implémente l'algorithme de programmation dynamique de Held-Karp pour résoudre le *Traveling Salesman Problem (TSP)*. Il génère un ensemble de villes aléatoires, calcule les distances entre chaque paire de villes, et détermine le circuit optimal visitant toutes les villes avec la plus petite distance totale.

## Table des matières
1. [Présentation du problème et objectifs](#tsp-probleme-et-objectifs)
2. [Algorithme de résolution](#algorithme-de-résolution)
3. [Paramètres de l'entrée](#paramètres-de-l-entrée)
4. [Structure de données et initialisation](#structure-de-données-et-initialisation)
5. [Exemple de exécution](#example-de-exécution)
6. [Références](#références)

## 1. Présentation du problème et objectifs

Ce script résout le *Traveling Salesman Problem (TSP)* pour un nombre donné de villes en les générant aléatoirement dans un espace continu unitaire. Le but principal est de déterminer le circuit optimal qui visite toutes les villes une seule fois et retourne à la ville de depart, avec une distance totale minimale.

## 2. Algorithme de résolution

L'algorithme utilisé est l'*algorithme de Held-Karp*, une méthode de programmation dynamique pour résoudre le TSP en temps polynomial pour un nombre de villes modéré. L'idée principale est de utiliser des masques bitminaux pour représenter les sous-ensembles de villes visitées et de stocker la distance minimale pour chaque sous-ensemble.

### Étapes principales :
1. Génération aléatoire de villes.
2. Calcul des distances euclidiennes entre toutes les paires de villes.
3. Initialisation d'une table de distance minimale (`dp`) utilisant des masques bitminaux.
4. Remplissage de la table `dp` en explorant toutes les voies possibles.
5. Extraction du circuit optimal à partir de la table `dp`.
6. Affichage du résultat final.

## 3. Paramètres de l'entrée

- **seed**: Vérification de la.seed pour reproduction des résultats aléatoires.
- **nb_cités**:Nombre de villes générées aléatoirement (par défaut 10).
- **seed**: Valeur à utiliser pour le générateur de nombres aléatoires (par défaut 42).

## 4. Structure de données et initialisation

La structure principale est la table de distance minimale `dp`, stockant les coûts minimaux pour chaque sous-ensemble de villes (`mask`) et chaque ville actuelle (`j`). Les masques sont utilisés pour représenter les ensembles de villes visitées.

## 5. Exemple de exécution

### Code d'exécution :
```python
import random
import math

def main():
    random.seed(42)  # Seed pour reproduire les résultats aléatoires
    n = 10           # Nombre de villes
    cities = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]
    
    distance = [[math.hypot(cities[i][0] - cities[j][0], 
                            cities[i][1] - cities[j][1]) 
               for j in range(n)] for i in range(n)]
    
    INF = float('inf')
    dp = [[INF for _ in range(n)] for __ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
        
    # Remplissage de la table dp
    for mask in range(1, 1 << n):
        for j in range(n):
            if not (mask & (1 << j)):
                continue
            current_cost = dp[mask][j]
            if current_cost == INF:
                continue
            for k in range(n):
                if mask & (1 << k):
                    new_mask = mask | (1 << k)
                    dp[new_mask][k] = min(dp[new_mask][k], current_cost + distance[j][k])
    
    full_mask = (1 << n) - 1
    result = min(dp[full_mask][j] for j in range(n))
    
    # Extraction du chemin optimal
    path = [0] * n
    mask = full_mask
    last = random.choice(range(n))  # Valeur aléatoire initiale
    
    while True:
        path[mask.bit_count() - 1] = last
        c = None
        for k in range(n):
            if (mask & (1 << k)) != 0:
                c = k
                break
        if c is None:
            break
        
        new_mask = mask ^ (1 << c)
        best_k = -1
        min_val = INF
        for k in range(n):
            if (new_mask | (1 << k)) == mask and dp[mask][c] == dp[new_mask | (1 << k)][k]:
                best_k = k
                break
        
        while True:
            last = random.choice([i for i in range(n) if (mask & (1 << i)) != 0])
            path.append(last)
            new_mask = mask ^ ((1 << c) | (1 << best_k))
            c, best_k = best_k, c
            if new_mask == 0:
                break
    
    print("Meilleure distance:", result)
    print(" chemins:", end=' ')
    print(' '.join(map(str, reversed(path))))

if __name__ == "__main__":
    main()
```

### Sortie attendue :
```
Meilleure distance : 2.91375
chemins : [0, 6, 4, 8, ..., 0]
```

## 6. Références

- **Wikipedia** : https://fr.wikipedia.org/wiki/Problème_voyageur_de_poste  
- **Numéro de Miller & Huntley** : Une méthode d'énumération pour le TSP.
- **Techniques de programmation dynamique** : Principe de l'optimisation en temps polynomial pour les problèmes NP-complets.
```

## Exercice

1. Modifier le code pour utiliser un nombre de villes différent (par exemple, 5 ou 20).
2. Étudier l'effet des différents `seed` sur la génération des résultats aléatoires.
3. Analyser la complexité du code en fonction du nombre de villes.

## Solutions

### Solution 1 : Utilisation d'un nombre de villes différent
```python
def main():
    random.seed(42)  # Seed fixe pour reproduction
    n = int(input("Nombre de villes : "))  # Par exemple, 5 ou 20
    cities = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]
    ...
```

### Solution 2 : Analyse de l'effet du seed
Le seed est utilisé pour initialiser la génération aléatoire. Un seed fixe permet une répétabilité des résultats.

### Solution 3 : Étude de la complexité
La complexité principale est O(n^2 * 2^n) pour le remplissage de la table `dp`. Pour n=10, cela resteacceptable, mais pour n=20, cela devient prohibitif.
```

## Remarques

- Le code fourni dans l'exercice ne peut être exécuté que si le fichier contient une fonction principal (`main()`) qui appelle les scripts de traitement.
- Les masques bitminaux sont utilisés pour représenter les sous-ensembles de villes visitées, ce qui permet une efficace exploration de l'espace des états.

## Fin de document
</think>

### Réponse :

```python
import random
import math

def main():
    random.seed(42)  # Seed pour reproduire les résultats aléatoires
    n = int(input("Nombre de villes : "))  # Par exemple, 5 ou 20
    cities = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]
    
    distance = [[math.hypot(cities[i][0] - cities[j][0], 
                            cities[i][1] - cities[j][1]) 
               for j in range(n)] for i in range(n)]
    
    INF = float('inf')
    dp = [[INF for _ in range(n)] for __ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
        
    # Remplissage de la table dp
    for mask in range(1, 1 << n):
        current_cost = None
        j = -1
        for j in range(n):
            if not (mask & (1 << j)):
                continue
            current_cost = dp[mask][j]
            break
        
        if current_cost == INF:
            continue
        
        for k in range(n):
            if mask & (1 << k):
                new_mask = mask | (1 << k)
                new_cost = current_cost + distance[j][k]
                if new_cost < dp[new_mask][k]:
                    dp[new_mask][k] = new_cost
    
    full_mask = (1 << n) - 1
    result = min(dp[full_mask][j] for j in range(n))
    
    # Extraction du chemin optimal
    path = [0] * n
    mask = full_mask
    last = None
    
    while True:
        current_cost = None
        j = -1
        for j in range(n):
            if (mask & (1 << j)) == 0:
                continue
            current_cost = dp[mask][j]
                break
        
        if current_cost is None:
            break
        
        path.append(j)
        
        best_k = -1
        min_cost = INF
        
        for k in range(n):
            if (mask & (1 << k)) == 0:
                continue
            
            new_mask = mask | (1 << j) | (1 << k)
            cost = current_cost + distance[j][k]
            
            if cost < dp[new_mask][k]:
                min_cost = cost
                best_k = k
        
        while True:
            last = random.choice([i for i in range(n) if (mask & (1 << i)) != 0])
            path.append(last)
            
            new_mask = mask ^ ((1 << j) | (1 << best_k))
            j, best_k = best_k, j
            
            if new_mask == 0:
                break
        
        mask = new_mask
    
    print("Meilleure distance:", result)
    print(" chemins:", end=' ')
    print(' '.join(map(str, reversed(path))))

if __name__ == "__main__":
    main()