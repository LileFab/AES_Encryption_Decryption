# Compte Rendu - Implémentation AES
![image](https://github.com/LileFab/AES_Encryption_Decryption/assets/98893025/e6d2faf0-ea90-43b1-b3b4-05745c4f293c)

## 1. Entrée et Matrice d'État Initial
- `input_str` représente la chaîne d'entrée initiale au format hexadécimal.
- La matrice d'état `state` est créée à partir de la chaîne d'entrée, organisée en une matrice 4x4.

## 2. Substitution de Bytes (SubBytes)
- La fonction `subBytes` remplace chaque octet dans la matrice d'état par la valeur correspondante dans la S-box (boîte de substitution).
- La S-box est une table de substitution 16x16 pré-définie (`s_box_16x16`).

## 3. Décalage des Lignes (ShiftRows)
- La fonction `shiftRows` effectue un décalage des octets dans chaque ligne de la matrice d'état.
- La première ligne reste inchangée, la deuxième est décalée d'un octet à gauche, la troisième de deux octets à gauche, et la quatrième de trois octets à gauche.

## 4. Mélange des Colonnes (MixColumns)
- La fonction `mixColumns` effectue une opération mathématique sur chaque colonne de la matrice d'état.
- L'opération implique la multiplication des octets par une matrice prédéfinie `mixColKey` dans le champ de Galois fini.
- La multiplication est réalisée via la fonction `multiply`, qui gère la multiplication dans le champ Galois fini.

## 5. Fonctions Auxiliaires
- `printPropre` affiche la matrice d'état d'une manière lisible.
- `fromLetterToDec` convertit une lettre hexadécimale en décimal.
- `toMatrice` organise la chaîne hexadécimale en une matrice 4x4.
- `multiply` réalise la multiplication dans le champ de Galois fini.

## 6. Fonction Principale (Main)
- La fonction `main` est la fonction principale qui appelle successivement les étapes de SubBytes, ShiftRows et MixColumns.
- Le résultat final est affiché à l'aide de la fonction `printPropre`.

L'ensemble du code représente l'implémentation d'une ronde (round) de l'algorithme AES (Advanced Encryption Standard) pour une clé de 128 bits. Chaque étape (SubBytes, ShiftRows, MixColumns) contribue à la confusion et à la diffusion des données pour renforcer la sécurité de l'algorithme.
