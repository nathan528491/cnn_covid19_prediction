#Importation des bibliothèques
import pandas as pd
import streamlit as st
import os
from PIL import Image

# Page large
st.set_page_config(layout='wide')
                   
#L'en-tête de la page
st.write("""
         # CoviNet
         ## Détection de la COVID-19 grâce au deep learning
         """)

st.markdown("<h2 style='text-align: center; color: black;'>Méthodologie </h2>", unsafe_allow_html=True,)
st.write("---")

#Creation des variables pour les images qu'on va charger plus tard
logo = Image.open(r"C:\Users\Hassam\Documents\app\images\new_logo.png")
masque = Image.open(r"C:\Users\Hassam\Documents\app\images\radio_masquee.png")
flip = Image.open(r"C:\Users\Hassam\Documents\app\images\pic_turn.png")


#Paramètres du sidebar
sidebar_name = "CoviNet"
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown(sidebar_name)
st.sidebar.info(
    """Auteurs : Juliette Greco, Matthieu Khairallah, \n
 Nathan Lancman, Hassan Burke) \n
Cohort Data Scientist Juillet 2022 \n
DataScientest""")


#Contenu
st.markdown("<strong>Étape 1.<strong> Établir des résultats de référence à l'aide d'un simple réseau neuronal convolutif (LeNet5) sur deux classes de sortie (« sain » et « malade »).", unsafe_allow_html=True)
st.markdown("-   catégories « COVID », « Lung Opacity » et « Viral Pneumonia » groupées comme « malade »")
st.markdown("-   5000 images par classes")
st.markdown("-   Essais sur des images masquées et non masquées")

st.markdown("<strong>Étape 2.<strong> Appliquer les techniques d'apprentissage par transfert (transfer learning) pour essayez plusieurs autres modèles CNN dont la viabilité a été prouvée en matière de classification d'images, avec des niveaux de complexité et des besoins de calcul variables.", unsafe_allow_html=True)
st.markdown("-   Modèles choisi: ResNet152, Xception, VGG16, EfficientNetB1")
st.markdown("-   Etudes sur 2 classes et les 4 classes originales")
st.markdown("-   Essais sur des images masquées et non masquées")
st.markdown("-   Essais sur des jeus de données avec data augmentation")

st.markdown("<strong>Étape 3.<strong> Choisir le meilluer modèle en terme de performance sur le jeu de données (accuracy) et le régler afin d'en améliorer les performances", unsafe_allow_html=True)
st.markdown("-   Essais de congélation et de décongélation (freezing and unfreezing) des couches du modèle")
st.markdown("-   Appliquer une GradCam afin d'interpréter notre modèle et de comprendre comment il définit ses classifications")

#Cette partie crée des indentations dans le texte ci-dessus
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)


# Afficher des images cote-a-cote
col1, col2 = st.columns(2)

with col1:
    st.image(masque, caption="Image Masquée", use_column_width=True, width=300)

with col2:
    st.image(flip, caption="Data Augmentation", use_column_width=True, width=300)





