# Tab 1: Conclusion
conclusion = [
    "-   Les modèles que nous avons testé ont été évalués en tenant compte de plusieurs critères "
    "essentiels en milieu clinique : la précision du diagnostic, le taux de faux positifs et de faux "
    "négatifs, ainsi que l'efficacité en termes de temps et de puissance de calcul.",

    "-   Notre choix de retenir EfficientNetB1 comme modèle optimal s'est basé sur son équilibre entre une "
    "haute précision de classification et une grande efficacité en termes de ressources.",

    "-   **Notre modèle obtient de meilleures performances sur un support moins efficace dans la détection de "
    "la COVID-19, la radiographie, que celui de Yang et al. (2020) entraîné sur des CT-scans.**",

    "-   **les résultats obtenus sont prometteurs et suggèrent que l'application de techniques d'apprentissage "
    "en profondeur dans le domaine médical est non seulement viable mais aussi extrêmement bénéfique.**"
]

# Tab 2: Limites
limites = [
    "-   Nous avons observé que l'application de masques numériques pour cibler la région pulmonaire pourrait "
    "avoir des effets négatifs sur la performance du modèle, soulevant des questions sur l'efficacité de "
    "cette technique.",

    "-   Bien que l'ensemble de vingt mille images soit considérable, une base de données de taille plus "
    "importante pourrait fournir de meilleurs résultats.",

    "-   Bien que nous n'ayons pas pu constater de différences significatives entre les sources d'images, "
    "nous ne pouvons pas exclure qu'un ensemble d'images plus standardisé (provenant d'un seul hôpital, "
    "par exemple) puisse améliorer les performances du modèle."
]

# Tab 3 : Axes d'amélioration
axes_amelioration = [
    "-   La robustesse des modèles face à des images de mauvaise qualité n'a pas été testée.",

    "-   nous avons identifié tardivement que les couches «Dense» utilisées dans la comparaison initiale des "
    "modèles n'étaient pas uniformes. Ceci pourrait avoir introduit un biais dans nos résultats et mérite "
    "d'être corrigé dans des recherches futures."
]
