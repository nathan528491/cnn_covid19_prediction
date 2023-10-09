etape1_points = """
-   Établir des résultats de référence à l'aide d'un simple réseau neuronal convolutif (LeNet5) 
sur deux classes de sortie (« sain » et « malade »).
-   Catégories « COVID », « Lung Opacity » et « Viral Pneumonia » groupées comme « malade ».
-   5000 images par classe.
-   Essais sur des images masquées et non masquées.
"""

etape2_points = """
-   Appliquer les techniques d'apprentissage par transfert (transfer learning) pour essayer plusieurs autres 
modèles CNN dont la viabilité a été prouvée en matière de classification d'images, 
avec des niveaux de complexité et des besoins de calcul variables.
-   Modèles choisis : ResNet152, Xception, VGG16, EfficientNetB1.
-   Études sur 2 classes et les 4 classes originales.
-   Essais sur des images masquées et non masquées.
-   Essais sur des jeux de données avec data augmentation.
"""

etape3_points = """
-   Choisir le meilleur modèle en termes de performance sur le jeu de données (accuracy) et 
le régler afin d'en améliorer les performances.
-   Essais de congélation et de décongélation (freezing and unfreezing) des couches du modèle.
-   Appliquer une GradCam afin d'interpréter notre modèle et de comprendre comment il définit ses 
classifications.
"""

etapes = [etape1_points, etape2_points, etape3_points]
