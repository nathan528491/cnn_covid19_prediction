# Tab 1
images_par_classes = """
Parmi les 21.165 images de radiographies pulmonaires dans notre base de données, **48%** des 
images représentent des cas normaux, **28%** représentent des cas d'opacité pulmonaire, **17%** des cas positifs de 
COVID-19, et **6%** de pneumonie virale.
"""

provenance_images = """
La base de données, nommé « COVID-19 Radiography Database » s'agissent d'une collection 
d'images .png  des radiographies de pulmonaires et leurs masques associés en libre accès sur 
[**Kaggle**](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database/). 
Si les images sont toutes réunies sur ce page web, ils proviennent de 8 sources différentes, 
dont l'une représente la majorité des données. \n
        
Aussi pertinent est le fait que les classes ne sont pas réparties de manière égale entre les huit 
sources. Par exemple, les 3616 radiographies des poumons positifs de COVID-19 sont reparties entre 6 
sources différents, alors que 2 sources contiennent des images des poumons sains et aucune image de 
poumons en présence de covid-19. \n
        
Cela pose des problèmes potentiels car les différentes sources peuvent présenter des différences de qualité 
d'image ou d'autres facteurs qui pourraient être corrélés avec les classes 
et donc confondre les résultats de notre modèle d'apprentissage automatique.
"""

# Tab 2
echantillon_par_classe = """
Afin de se donner un aperçu des images qui constituent notre jeu de données, nous  
avons rédigé un script en Python qui génère une figure avec 12 images sélectionnées au 
hasard à partir de leurs classes respectives.
"""

# Tab 3
moyenne_par_classe = """
L’image moyenne générée pour chaque classe nous a permis d’observer certaines 
caractéristiques propres à chaque classe. Nous avons pu ainsi remarquer que 
les radiographies des sous-classes « COVID » et « Lung_Opacity » semblaient être les 
plus obstruées dans la région pulmonaire. Inversement, nous avons constaté une opacité 
nettement différente dans la région pulmonaire dans la sous-classe « Normal ».
"""

# Tab 4
differences_images = """
A l’aide des images moyennes nous avons pu calculer les différences entre la sous-classe 
« COVID » et le reste. D’une part nous remarquons que face aux images 
« Normal », l’intensité des pixels dans la région pulmonaire des radiographies 
« COVID » a tendance être plus élevée. En imagerie, ceci pourrait se traduire, comme 
nous l’avons vu pour la moyenne des images, d’une obstruction au niveau des poumons.
"""

# Tab 5
exemple_distribution_pixel = """
Nous avons examiné sur un échantillon aléatoire des radiographies la distribution 
des pixels afin d'assurer la cohérence de l'image dans l'ensemble de notre jeu de données.
"""

distribution_par_classe = """
Les distributions des pixels entre les classes semble confirmer qu'il est peu 
probable qu'il y ait un écart important entre les classes qui pourrait avoir un impact sérieux sur 
l'efficacité de notre modèle.
"""