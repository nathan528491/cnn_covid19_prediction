#Importation des bibliothèques
import pandas as pd
import streamlit as st
import os
from PIL import Image

#Page centrée
st.set_page_config(layout="centered")

#L'en-tête de la page
st.write("""
         # CoviNet
         ## Détection de la COVID-19 grâce au deep learning
         """)

st.markdown("<h2 style='text-align: center; color: black;'>Visualisation des Données </h2>", unsafe_allow_html=True,)

#Creation des variables pour les images qu'on va charger plus tard
logo = Image.open(r"C:\Users\Hassam\Documents\app\images\new_logo.png")
class_bar = Image.open(r"C:\Users\Hassam\Documents\app\images\classes2.png")
provenance = Image.open(r"C:\Users\Hassam\Documents\app\images\provenance.png")
radios_classe = Image.open(r"C:\Users\Hassam\Documents\app\images\images_classes.png")
moyennes = Image.open(r"C:\Users\Hassam\Documents\app\images\moyenne_type.png")
diff = Image.open(r"C:\Users\Hassam\Documents\app\images\diff.png")
eigen = Image.open(r"C:\Users\Hassam\Documents\app\images\eigen.png")
img_pix = Image.open(r"C:\Users\Hassam\Documents\app\images\pix_dist_norm.png")
pix_dist = Image.open(r"C:\Users\Hassam\Documents\app\images\source_pix_dist.png")


#Paramètres du sidebar
sidebar_name = "CoviNet"
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown(sidebar_name)
st.sidebar.info(
    """Auteurs : Juliette Greco, Matthieu Khairallah, \n 
Nathan Lancman, Hassan Burke) \n
Cohort Data Scientist Juillet 2022 \n
DataScientest""")

# Création des tabs pour chaque élément de la data viz
tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Metadonnées", "Échantillon par Classe", "Moyennes par Classe", "Differences Entres Classes", "Eigenimages", "Pixel Distribution"])

#Chargement des images et descriptions pour tab 1
with tab1: 
    st.markdown( "<h4 style='text-align: center; color: black;'>Metadonnées </h4>",unsafe_allow_html=True,)
    st.write(" ")
    st.write("#### Nombres d'images par classe ")
    st.image(class_bar)
    st.write("""Parmi les 21.165 images de radiographies pulmonaires dans notre base de données, **48%** des images représentent des cas normaux, **28%** répresentent 
             des cas d'opacite pulmonaire, **17%** des cas positifs de COVID-19, et **6%** de pneumonie virale.""")

    st.write("---")
    st.write("#### Provenance des images ")
    st.image(provenance)    
    st.write("""
        Le base de données, nommé « COVID-19 Radiography Database » s'agissent d'une collection d'images .png des radiographies de pulmonaires et leurs masques associés
        en libre acces sur [**Kaggle**](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database/). Si les images sont toutes réunies sur ce page web, ils proviennent de 8 sources différentes, dont l'une 
        représente la majorité des données. \n

        Aussi pertinent est le fait que les classes ne sont pas réparties de manière égale entre les huit sources. Par exemple, les 3616 radiographies des poumons posistifs de COVID-19 sont 
        reparties entre 6 sources differents, alors que 2 sources contiennent des images des poumons sains et aucune image de poumons en présence de covid-19. \n
        
        Cela pose des problèmes potentiels car les différentes sources peuvent présenter des différences de qualité d'image ou d'autres facteurs qui pourraient être corrélés avec les classes 
        et donc confondre les résultats de notre modèle d'apprentissage automatique.
        """)

#Chargement des images et descriptions pour tab 2
with tab2: 
    st.markdown( "<h4 style='text-align: center; color: black;'>Échantillon par Classe </h4>",unsafe_allow_html=True,)
    st.write(" ")
    st.image(radios_classe)
    st.write("""
        Afin de se donner un aperçu des images qui constituent notre jeu de données nous
        avons rédigé un script en Python qui génère une figure avec 12 images sélectionnées au
        hasard à partir de leurs classes respectives
        """)
#Chargement des images et descriptions pour tab 3
with tab3: 
    st.markdown( "<h4 style='text-align: center; color: black;'>Moyennes par Classe </h4>",unsafe_allow_html=True,)
    st.write(" ")
    st.image(moyennes)
    st.write("""
        L’image moyenne générée pour chaque classe nous a permis d’observer certaines
        caractéristiques propres à chaque classe. Nous avons pu ainsi remarquer que
        les radiographies des sous-classes « COVID » et « Lung_Opacity » semblaient être les
        plus obstruées dans la région pulmonaire. Inversement, nous avons constaté une opacité
        nettement différente dans la région pulmonaire dans la sous-classe « Normal ».
        """)

#Chargement des images et descriptions pour tab 4
with tab4: 
    st.markdown( "<h4 style='text-align: center; color: black;'>Differences Entres Classes </h4>",unsafe_allow_html=True,)
    st.write(" ")
    st.image(diff)
    st.write("""
        A l’aide des images moyennes nous avons pu calculer les différences entre la sousclasse
        « COVID » et le reste. D’une part nous remarquons que face aux images
        « Normal », l’intensité des pixels dans la région pullmonaire des radiographies
        « COVID » a tendance être plus élevée. En imagerie, ceci pourrait se traduire, comme
        nous l’avons vu pour la moyenne des images, d’une obstruction au niveau des poumons.
        D’autre part, lorsque nous comparons « COVID » et « Viral pneumonia », le constat
        semble plus mitigé : les zones pulmonaires renvoient des pixels aux valeurs plus élevées
        dans certaines zones, ce qui pourrait impacter la compréhension des images par notre
        modèle.
        """)

#Chargement des images et descriptions pour tab 5
with tab5: 
    st.markdown( "<h4 style='text-align: center; color: black;'>Eigenimages </h4>",unsafe_allow_html=True,)
    st.write(" ")
    st.image(eigen)
    st.write("""
        [ici le text]
        """)

#Chargement des images et descriptions pour tab 6
with tab6: 
    st.markdown( "<h4 style='text-align: center; color: black;'>Distribution des Pixels </h4>",unsafe_allow_html=True,)
    st.write(" ")
    st.write("#### Exemple ")
    st.image(img_pix)
    st.write("""
             [ici le text]
             """)

    st.write("---")
    st.write("#### Distribution par Source des Données ")
    st.image(pix_dist)    
    st.write("""
             [ici le text]
             """)