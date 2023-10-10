intro_bullet_points = [
    "-   Les réseaux neuronaux convolutifs (CNN) sont excellent dans la classification des images en "
    "raison de leur capacité à apprendre et à extraire automatiquement des caractéristiques hiérarchiques "
    "des images.",

    "-   Nous avons testé 5 modèles avant d'en choisir un, sur la base de la précision et des exigences "
    "de calcul. L'architecture Lenet5, un modèle relativement simple, a servi comme référence contre des "
    "modèles «state of the art»",

    "-   Nous avons d'abord testé les modèles sur deux classes (« sain » et « malade ») afin de "
    "sélectionner les modèles les plus performants pour la classification des quatre classes."
]

text_lenet = """
L'architecture de LeNet-5 est structurée avec une alternance de couches convolutives et de couches 
de mise en commun, suivies de couches entièrement connectées. 
Il se compose généralement de deux couches convolutives avec activation ReLU, de deux couches de mise 
en commun maximale et de couches entièrement connectées. 
Même si des modèles plus récents l'ont dépassés, la simplicité de LeNet-5 par rapport 
à d'autres modèles de classification, le rend efficace en termes de calcul.
"""

text_resnet = """
ResNet152 est structuré comme un réseau résiduel profond, avec des blocs résiduels qui permettent 
un apprentissage très profond du réseau sans le problème du gradient de fuite. 
Sa profondeur exceptionnelle, qui lui permet de capturer des caractéristiques hiérarchiques 
complexes dans les images, et son efficacité à atteindre une précision de pointe dans diverses tâches 
de classification d'images.
"""

text_xception = """
Xception utilise des convolutions séparables dans le sens de la profondeur. Il est structuré avec 
plusieurs blocs de convolutions, suivis par des connexions 
de saut et une mise en commun de la moyenne globale. Xception est connu 
pour ses performances élevées en termes de précision et d'efficacité de calcul, grâce à ses 
convolutions séparables dans le sens de la profondeur.
"""

text_vgg = """
VGG16 est une architecture de réseau neuronal convolutif qui se compose de 16 couches de poids, 
dont 13 couches convolutives et 3 couches entièrement connectées. Il est connu pour sa simplicité et 
son architecture uniforme avec de petits filtres convolutifs 3x3.
"""

text_efficientnet = """
EfficientNetB1 fait partie de la famille EfficientNet d'architectures de réseaux neuronaux, 
connues pour leur efficacité en termes de taille de modèle et d'exigences de calcul. EfficientNetB1 utilise 
une mise à l'échelle composée pour équilibrer la profondeur, la largeur et la résolution afin d'obtenir un 
compromis solide entre la précision et l'efficacité de calcul.
"""

resultats_sans_masques = """
Comme attendu, les modèles plus complexes ont généralement obtenu de meilleurs résultats que LeNet5, 
VGG16 et EfficientNet étant particulièrement performants.
"""

resultats_avec_masques = """
Nous constatons une nette diminution des performances lorsque des masques sont ajoutés, 
les architectures EfficientNet et ResNet152 conservant leurs performances mieux que les autres.
"""