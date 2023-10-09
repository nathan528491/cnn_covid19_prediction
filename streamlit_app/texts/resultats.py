resultats_sans_masques = """
Les modèles basés sur EfficientNetB1 et VGG16 se sont révélés remarquablement efficaces tant en 
termes de précision globale que de sensibilité aux faux négatifs.
"""

resultats_avec_masques = """
Comme pour l’étude à deux classes, l’application de masques entraîne une réduction des mesures de 
performances, mais l’architecture basée sur EfficientNetB1 conserve néanmoins des scores assez élevés.
"""

optimisation_hyperparametres = [
    "-   Pour affiner davantage la performance de nos modèle choisi, EfficientNetB1 et VGG16, nous avons "
    "employé Keras Tuner pour l'optimisation des hyperparamètres. Cette démarche a été guidée par un code "
    "de recherche aléatoire (`RandomSearch`), ciblant spécifiquement la minimisation de la perte de "
    "validation (`val_loss`) sur un total de 50 essais (`max_trials`).",

    "- Outre la sélection des meilleurs hyperparamètres, cette étape nous a permis de tester l'efficacité "
    "de la congélation et de la décongélation des couches dans les modèles de base.",

    "- Les modèles les plus performants utilisés pour l'étude finale étaient celui basé sur "
    "l'architecture EfficientNet avec 31 couches du modèle de base dégelées, et celui basé sur "
    "l'architecture VGG16 avec 4 couches dégelées."
]

etudes_avec_sans_masques = [
    "-   Nos résultats indiquent une performance généralement inférieure des modèles lorsque des masques "
    "numériques sont appliqués pour cibler la région pulmonaire.",

    "- Une raison possible pourrait être la perte d'information contextuelle qui pourrait aider le modèle à "
    "différencier entre les diverses classes."
]

faux_positifs_negatifs = [
    "-   Dans le contexte clinique, la précision du diagnostic est cruciale. Un faux positif, "
    "c'est-à-dire la classification erronée d'un patient sain comme étant malade, peut conduire à des "
    "traitements inutiles et induire un stress psychologique considérable pour le patient.",

    "-   Dans notre étude, tous les modèles ont montré une faible proportion de faux positifs et de faux "
    "négatifs, mais il est crucial de prendre ces erreurs en compte.",

    "- Dans l’étude binaire « Sain vs Malade », le modèle VGG16 a affiché le plus faible taux de faux "
    "négatifs, avec seulement 59 cas mal classés parmi les 996 réellement malades. Ce résultat pourrait "
    "faire de VGG16 un choix préférable dans un contexte clinique où minimiser les faux négatifs est une "
    "priorité. Cependant, il est important de considérer également d'autres métriques de performance et "
    "les spécificités de l'application clinique en question."
]

interpretabilite = [
    "-   Afin d'offrir une meilleure compréhension des décisions prises par notre modèle EfficientNetB1, "
    "nous avons fait appel à la technique Grad-CAM (Gradient-weighted Class Activation Mapping).",

    "-   Dans le cadre de notre étude, l'implémentation de Grad-CAM a révélé une focalisation cohérente "
    "et médicalement pertinente des zones d'intérêt, renforçant ainsi la crédibilité de nos résultats."
]
