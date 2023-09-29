# CoviNet : Détection de la COVID-19 grâce au deep learning

## Présentation

Ce projet fait partie de la formation [Data Scientist Bootcamp](https://datascientest.com/en/data-scientist-course) dispensée par [DataScientest](https://datascientest.com/) et co-certifiée avec MinesParisTech PSL.

Contributeurs au projet :
- Juliette Greco
- Matthieu Khairallah
- Nathan Lancman
- Hassan Burke

A l’aide d’une banque d’images de radiographies pulmonaires librement disponibles sur le site web Kaggle, nous avons entrainé des modèles de deep learning afin de vérifier si les techniques d'apprentissage profond (deep
learning) sont capable de détecter efficacement la présence, ou non, de COVID-19.

Les meilleures parmi ces modèles se sont révélés très efficaces, avec une précision de plus de 90 % dans la détection de la présence de Covid-19 et d'autres maladies dans les poumons. Nous pensons que ce projet démontre
la pertinence de ces techniques de deep learning dans le contexte médical. Dans les environnements où les tests (tels que la PCR) et les capacités du personnel des établissements médicaux sont limités, comme lors de la
pandémie de Covid-19, des modèles tels que ceux que nous avons testés dans le cadre de ce projet peuvent être utiles pour identifier les patients qui ont besoin de soins.

Pour en savoir plus sur le contexte, la méthodologie et les résultats, veuillez consulter le rapport dans ce dépôt.

Les [notebooks](./notebooks) contenant nos codes python et le [jeu de données](./data) composé de 20000 images de radiographies pulmonaires sont à votre disposition.

Une présentation et démonstration de nos modèles sont aussi disponibles dans une application [Streamlit](./streamlit_app).

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
