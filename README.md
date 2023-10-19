# CoviNet : Détection de la COVID-19 grâce au deep learning

## Présentation

Ce projet fait partie de la formation Data Scientist Bootcamp dispensée par DataScientest et co-certifiée avec MinesParisTech PSL.

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

Les [notebooks](./notebooks) contenant nos codes python et le [jeu de données](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database/) composé de 20000 images de radiographies pulmonaires sont à votre disposition.

Une présentation et une démonstration de nos modèles sont aussi disponibles dans une application [Streamlit](./streamlit_app).

Les exigences pour l'installation peuvent être trouvées :

```
pip install -r requirements.txt
```

## Streamlit App

L'application est [**disponible en ligne ici**](https://nathan528491-cnn-covid19-prediction-app-n714sj.streamlit.app/).

Pour lancer l'application en local :

- Si vous voulez utiliser la partie démonstration du modèle avec un modèle, il faut d'abord télécharger le dataset et sauvegarder les modèles VGG16 :

Télécharger le dataset sur [Kaggle](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database/) et le placer dans le dossier [data](./data) en renommant le dossier en `Viral Pneumonia` en `Viral_Pneumonia`.

```
├── data
│   ├── COVID
│   ├── Lung_Opacity
│   ├── Normal
│   ├── Viral_Pneumonia
│   ├── [...]
├── notebooks
└── [...]
```
Les modèles VGG16 étant trop lourds, ils ne sont pas disponibles sur GitHub. Il faudra les sauvegarder à partir des notebooks se trouvant dans le dossier [notebooks](./notebooks).
Exécuter les cellules dans les notebooks 4 classes jusqu'à la sauvegarde des modèles.

```shell
[...]
model.save('./models/[nom_du_modèle].h5')
```

- Si vous n'avez pas besoin des modèles VGG16 de la partie démonstration du modèle, passez les étapes précédentes :

```shell
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run app.py
```

L'appli sera disponible à [localhost:8501](http://localhost:8501).
