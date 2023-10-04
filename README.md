# CoviNet : Détection de la COVID-19 grâce au deep learning

## Présentation

Ce projet fait partie de la formation [Data Scientist Bootcamp](https://datascientest.com/en/data-scientist-course) dispensée par [DataScientest](https://datascientest.com/) et co-certifiée avec MinesParisTech PSL.

Contributeurs au projet :
- Juliette Greco
- Matthieu Khairallah
- Nathan Lancman
- Hassan Burke

Chef de projet :
- Gaël Penessot

Nous avons utilisé une banque d'images de radiographies pulmonaires, disponibles en libre accès sur le site web Kaggle, pour entraîner des modèles de deep learning. Notre objectif était de vérifier la capacité des techniques d'apprentissage profond à détecter efficacement la présence ou l'absence de COVID-19.

Les modèles les plus performants ont montré une précision supérieure à 90 % dans la détection de la COVID-19 et d'autres pathologies pulmonaires. Ce projet illustre donc la pertinence des techniques de deep learning dans un contexte médical. Dans des situations où les tests de diagnostic (comme le test PCR) et les ressources humaines médicales sont limitées, notamment durant la pandémie de COVID-19, des modèles comme ceux que nous avons développés peuvent s'avérer utiles pour identifier les patients nécessitant des soins.

Pour plus d'informations sur le contexte, la méthodologie et les résultats, nous vous invitons à consulter le rapport disponible dans ce dépôt.

Les [notebooks](./notebooks) contenant nos codes python et le [jeu de données](./data) composé de 20000 images de radiographies pulmonaires sont à votre disposition.

Une présentation et une démonstration de nos modèles sont aussi disponibles dans une application [Streamlit](./streamlit_app).

les exigences pour l'installation peuvent être trouvées :

```
pip install -r requirements.txt
```

## Streamlit App

Pour lancer l'appli:

```shell
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run 1_🏠_Intro.py.py
```

L'appli sera disponible à [localhost:8501](http://localhost:8501).
