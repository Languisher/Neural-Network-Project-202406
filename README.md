# Projet Neural-Network-202406

Projet pour le cours Réseaux de Neurones.

## Structure du code

Le code est divisé en deux parties principales :
- `dataset/` : contient les classes pour charger les données
    - `dataset/CWRU-dataset/` : contient les données du dataset CWRU
    - `dataset/train-dataset/` : contient les données du dataset d'entraînement que nous avons sélectionné
- `src/` : contient les classes pour les modèles et les fonctions d'entraînement
    - `src/prepDataset.ipynb` : notebook pour préparer les données
    - `src/cnn-classification.ipynb` : notebook pour entraîner le modèle CNN 1D
    - `src/cnn-class-amelioration.ipynb` : notebook pour entraîner le modèle CNN 2D

Nous pouvons vérifier les résultats des modèles, les courbes de perte (loss) et de précision (accuracy) dans les notebooks. Évidemment, le modèle CNN 2D que nous avons proposé présente une meilleure performance que le modèle CNN 1D, qui est une approche plus directe.

Les modèles convergent bien, et le taux de précision est satisfaisant. Toutes les implémentations sont faites en utilisant Numpy.

Github link : https://github.com/Languisher/Neural-Network-Project-202406