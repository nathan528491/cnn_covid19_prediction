# Importation des bibliothèques
import streamlit as st
from PIL import Image

sidebar_name = "Modélisation"


def run():
    # Titre de la page
    st.markdown("<h2 style='text-align: center; color: black;'>Modélisation </h2>", unsafe_allow_html=True, )
    st.write("---")

    st.write("""
            Les réseaux neuronaux convolutifs (CNN) excellent dans la classification des images en raison de leur 
            capacité à apprendre et à extraire automatiquement des caractéristiques hiérarchiques des images.
            Contrairement aux modèles traditionnels qui nécessitent une ingénierie des caractéristiques réalisée à la
            main, les CNN peuvent découvrir et utiliser de manière adaptative des motifs et des textures, ce qui les
            rend très efficaces pour des tâches telles que la reconnaissance d'objets, où des indices visuels complexes
            jouent un rôle crucial.
             """)

    # Creation des variables pour les images qu'on va charger plus tard
    lenet = Image.open(r"streamlit_app/assets/logo-datascientest.png")
    xception = Image.open(r"streamlit_app/assets/logo-datascientest.png")
    vgg = Image.open(r"streamlit_app/assets/logo-datascientest.png")
    resnet = Image.open(r"streamlit_app/assets/logo-datascientest.png")
    enet = Image.open(r"streamlit_app/assets/logo-datascientest.png")

    # Création des tabs pour chaque modèle
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["LeNet5", "ResNet152", "Xception", "VGG16", "EfficientNetB1"])

    # Chargement des images et descriptions pour tab 1
    with tab1:
        st.markdown("<h4 style='text-align: center; color: black;'>LeNet5 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(lenet)
        st.write("""Parmi les 21.165 images de radiographies pulmonaires dans notre base de données, **48%** des 
        images représentent des cas normaux, **28%** représentent des cas d'opacité pulmonaire, **17%** des cas 
        positifs de COVID-19, et **6%** de pneumonie virale.""")

    # Chargement des images et descriptions pour tab 2
    with tab2:
        st.markdown("<h4 style='text-align: center; color: black;'>ResNet152 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(resnet)
        st.write("""
            Afin de se donner un aperçu des images qui constituent notre jeu de données nous
            avons rédigé un script en Python qui génère une figure avec 12 images sélectionnées au
            hasard à partir de leurs classes respectives
            """)
    # Chargement des images et descriptions pour tab 3
    with tab3:
        st.markdown("<h4 style='text-align: center; color: black;'>Xception </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(xception)
        st.write("""
            L’image moyenne générée pour chaque classe nous a permis d’observer certaines
            caractéristiques propres à chaque classe. Nous avons pu ainsi remarquer que
            les radiographies des sous-classes « COVID » et « Lung_Opacity » semblaient être les
            plus obstruées dans la région pulmonaire. Inversement, nous avons constaté une opacité
            nettement différente dans la région pulmonaire dans la sous-classe « Normal ».
            """)

    # Chargement des images et descriptions pour tab 4
    with tab4:
        st.markdown("<h4 style='text-align: center; color: black;'>VGG16 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(vgg)
        st.write("""
            L’image moyenne générée pour chaque classe nous a permis d’observer certaines
            caractéristiques propres à chaque classe. Nous avons pu ainsi remarquer que
            les radiographies des sous-classes « COVID » et « Lung_Opacity » semblaient être les
            plus obstruées dans la région pulmonaire. Inversement, nous avons constaté une opacité
            nettement différente dans la région pulmonaire dans la sous-classe « Normal ».
            """)

    # Chargement des images et descriptions pour tab 5
    with tab5:
        st.markdown("<h4 style='text-align: center; color: black;'>EfficientNetB1 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(enet)
        st.write("""
            A l’aide des images moyennes nous avons pu calculer les différences entre la sous-classe
            « COVID » et le reste. D’une part nous remarquons que face aux images
            « Normal », l’intensité des pixels dans la région pulmonaire des radiographies
            « COVID » a tendance être plus élevée. En imagerie, ceci pourrait se traduire, comme
            nous l’avons vu pour la moyenne des images, d’une obstruction au niveau des poumons.
            D’autre part, lorsque nous comparons « COVID » et « Viral pneumonia », le constat
            semble plus mitigé : les zones pulmonaires renvoient des pixels aux valeurs plus élevées
            dans certaines zones, ce qui pourrait impacter la compréhension des images par notre
            modèle.
            """)
