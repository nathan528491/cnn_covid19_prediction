import streamlit as st
from PIL import Image
from streamlit_app.texts import resultats
from streamlit_app.config import st_markdown
import path

directory = path.Path(__file__).parent.parent.parent

sidebar_name = "🎯 Résultats"

# Creation des variables pour les images qu'on va charger plus tard
resume_sans = Image.open(directory + "streamlit_app/assets/images/4_classes.png")
resume_masques = Image.open(directory + "streamlit_app/assets/images/4_classes_masques.png")
conf_enet = Image.open(directory + "streamlit_app/assets/images/4_enet_conf.png")
courbe_enet = Image.open(directory + "streamlit_app/assets/images/4_enet_courbe.png")
conf_vgg = Image.open(directory + "streamlit_app/assets/images/4_vgg_conf.png")
courbe_vgg = Image.open(directory + "streamlit_app/assets/images/4_vgg_courbe.png")
correct = Image.open(directory + "streamlit_app/assets/images/gradcam_correct.png")
incorrect = Image.open(directory + "streamlit_app/assets/images/gradcam_incorrect.png")

gradcam_enet_correct = Image.open(directory + "streamlit_app/assets/images/gc_4_eff_co.png")
gradcam_enet_correct_mask = Image.open(directory + "streamlit_app/assets/images/gc_4_eff_co_mask.png")
gradcam_enet_incorrect = Image.open(directory + "streamlit_app/assets/images/gc_4_eff_inco.png")
gradcam_enet_incorrect_mask = Image.open(directory + "streamlit_app/assets/images/gc_4_eff_inco_mask.png")
gradcam_vgg_correct = Image.open(directory + "streamlit_app/assets/images/gc_4_vgg_co.png")
gradcam_vgg_correct_mask = Image.open(directory + "streamlit_app/assets/images/gc_4_vgg_co_mask.png")
gradcam_vgg_incorrect = Image.open(directory + "streamlit_app/assets/images/gc_4_vgg_inco.png")
gradcam_vgg_incorrect_mask = Image.open(directory + "streamlit_app/assets/images/gc_4_vgg_inco_mask.png")


def run():
    st_markdown('Résultats', 'h2')
    st.write("---")

    st_markdown('Résumé des résultats', 'h4')

    # Tableau pour resumer les résultats
    selected_option = st.selectbox("Sélectionner une option", ["Résultats sans masques", "Résultats avec masques"])

    if selected_option == "Résultats sans masques":
        st.subheader("Résumé des résultats sur 4 classes sans masques")
        st.image(resume_sans)
        st.write(resultats.resultats_sans_masques)
    elif selected_option == "Résultats avec masques":
        st.subheader("Résumé des résultats sur 4 classes avec masques")
        st.image(resume_masques)
        st.write(resultats.resultats_avec_masques)

    st.write("---")

    # Contexte
    st_markdown('Optimisation des hyperparamètres', 'h5')
    st.write(" ")
    for text in resultats.optimisation_hyperparametres:
        st.markdown(text)
    st.write(" ")

    st_markdown('Étude avec masques vs. sans masques', 'h5')
    st.write(" ")
    for text in resultats.etudes_avec_sans_masques:
        st.markdown(text)
    st.write(" ")

    st_markdown('Faux positifs et faux négatifs', 'h5')
    st.write(" ")
    for text in resultats.faux_positifs_negatifs:
        st.markdown(text)
    st.write(" ")

    st_markdown('Interprétabilité du modèle', 'h5')
    st.write(" ")
    for text in resultats.interpretabilite:
        st.markdown(text)
    st.write(" ")

    st.write("---")

    st_markdown("Résultats de l'étude de 4 classes sans masques", 'h4')

    # Matrices de confusion et courbes d'entrainement
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("VGG16")
        st.image(conf_vgg, use_column_width=True)
        st.write("---")
        st.image(courbe_vgg, caption="Courbes d'entrainement VGG16", use_column_width=True)

    with col2:
        st.subheader("EfficientNetB1")
        st.image(conf_enet, use_column_width=True)
        st.write("---")
        st.image(courbe_enet, caption="Courbes d'entrainement EfficientNetB1", use_column_width=True)

    # GradCAM
    st.write("---")
    st_markdown("GradCAM", 'h4')
    st.write("  ")

    tab1, tab2 = st.tabs(["EfficientNetB1", "VGG16"])

    with tab1:
        tab3, tab4 = st.tabs(["Sans masques", "Masques"])
        with tab3:
            st.image(gradcam_enet_correct)
            st.image(gradcam_enet_incorrect)

        with tab4:
            st.image(gradcam_enet_correct_mask)
            st.image(gradcam_enet_incorrect_mask)

    with tab2:
        tab5, tab6 = st.tabs(["Sans masques", "Masques"])
        with tab5:
            st.image(gradcam_vgg_correct)
            st.image(gradcam_vgg_incorrect)

        with tab6:
            st.image(gradcam_vgg_correct_mask)
            st.image(gradcam_vgg_incorrect_mask)

    # st.write("GradCAM de prédictions correctes")
    # st.image(correct)
    # st.write("  ")
    # st.write("  ")
    # st.write("GradCAM de prédictions incorrectes")
    # st.image(incorrect)
