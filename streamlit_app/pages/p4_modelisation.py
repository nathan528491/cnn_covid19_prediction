# Importation des bibliothèques
import streamlit as st
from PIL import Image
from streamlit_app.texts import modelisation
from streamlit_app.config import st_markdown
import path
import sys

dir = path.Path(__file__).parent.parent.parent
sys.path.append(dir)

sidebar_name = "📐 Modélisation"

# Creation des variables pour les images qu'on va charger plus tard
lenet = Image.open(r"streamlit_app\assets\images\lenet.jpg")
xception = Image.open(r"streamlit_app\assets\images\xception.png")
vgg = Image.open(r"streamlit_app\assets\images\vgg.jpg")
resnet = Image.open(r"streamlit_app\assets\images\resnet.png")
enet = Image.open(r"streamlit_app\assets\images\enet.png")
conf_lenet = Image.open(r"streamlit_app\assets\images\2_lenet_conf.png")
courbe_lenet = Image.open(r"streamlit_app\assets\images\2_lenet_courbe.png")
conf_resnet = Image.open(r"streamlit_app\assets\images\2_resnet_conf.png")
courbe_resnet = Image.open(r"streamlit_app\assets\images\2_resnet_courbe.png")
conf_xception = Image.open(r"streamlit_app\assets\images\2_xcep_conf.png")
courbe_xception = Image.open(r"streamlit_app\assets\images\2_xcep_courbe.png")
conf_vgg = Image.open(r"streamlit_app\assets\images\2_vgg_conf.png")
courbe_vgg = Image.open(r"streamlit_app\assets\images\2_vgg_courbe.png")
conf_enet = Image.open(r"streamlit_app\assets\images\2_enet_conf.png")
courbe_enet = Image.open(r"streamlit_app\assets\images\2_enet_courbe.png")
resume_sans = Image.open(r"streamlit_app\assets\images\2_classes.png")
resume_masques = Image.open(r"streamlit_app\assets\images\2_classes_masques.png")


def display_tab(title, image, text, conf, courbe):
    st_markdown(title, 'h4')
    st.write(" ")

    st.image(image)
    st.write(text)

    st.write("---")

    st_markdown('Matrice de confusion : Sain vs Malade', 'h5')
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image(conf)
    st.write(" ")

    st_markdown('Courbe d\'entrainement : Sain vs Malade', 'h5')
    st.image(courbe)


def run():
    # Titre de la page
    st_markdown('Modélisation', 'h2')
    st.write("---")

    for text in modelisation.intro_bullet_points:
        st.markdown(text)

    # Création des tabs pour chaque modèle
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["LeNet5", "ResNet152", "Xception", "VGG16", "EfficientNetB1"])

    # Chargement des images et descriptions pour tab 1
    with tab1:
        display_tab('LeNet5', lenet, modelisation.text_lenet, conf_lenet, courbe_lenet)

    # Chargement des images et descriptions pour tab 2
    with tab2:
        display_tab('ResNet152', resnet, modelisation.text_resnet, conf_resnet, courbe_resnet)

    # Chargement des images et descriptions pour tab 3
    with tab3:
        display_tab('Xception', xception, modelisation.text_xception, conf_xception, courbe_xception)

    # Chargement des images et descriptions pour tab 4
    with tab4:
        display_tab('VGG16', vgg, modelisation.text_vgg, conf_vgg, courbe_vgg)

    # Chargement des images et descriptions pour tab 5
    with tab5:
        display_tab('EfficientNetB1', enet, modelisation.text_efficientnet, conf_enet, courbe_enet)

    # Tableau pour resumer les résultats
    selected_option = st.selectbox("Sélectionner une option", ["Résultats sans masques", "Résultats avec masques"])

    if selected_option == "Résultats sans masques":
        st.subheader("Résumé des résultats sur 2 classes sans masques")
        st.image(resume_sans)
        st.write(modelisation.resultats_sans_masques)
    elif selected_option == "Résultats avec masques":
        st.subheader("Résumé des résultats sur 2 classes avec masques")
        st.image(resume_masques)
        st.write(modelisation.resultats_avec_masques)
