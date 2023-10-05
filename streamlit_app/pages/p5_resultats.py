import streamlit as st
from PIL import Image

sidebar_name = "Résultats"

# Creation des variables pour les images qu'on va charger plus tard
resume_sans = Image.open(r"images\4_classes.png")
resume_masques = Image.open(r"images\4_classes_masques.png")
conf_enet = Image.open(r"images\4_enet_conf.png")
courbe_enet = Image.open(r"images\4_enet_courbe.png")
conf_vgg = Image.open(r"images\4_vgg_conf.png")
courbe_vgg = Image.open(r"images\4_vgg_courbe.png")
correct = Image.open(r"images\gradcam_correct.png")
incorrect = Image.open(r"images\gradcam_incorrect.png")


def run():
    st.markdown("<h2 style='text-align: center; color: black;'>Résultats </h2>", unsafe_allow_html=True)
    st.write("---")

    st.markdown("<h4 style='text-align: center; color: black;'>Résumé des résultats </h4>", unsafe_allow_html=True, )

    # Tableau pour resumer les résultats
    selected_option = st.selectbox("Sélectionner une option", ["Résultats sans masques", "Résultats avec masques"])

    if selected_option == "Résultats sans masques":
        st.subheader("Résumé des résultats sur 4 classes sans masques")
        st.image(resume_sans)
        st.write("Les modèles basés sur EfficientNetB1 et VGG16 se sont révélés remarquablement efficaces tant en "
                 "termes de précision globale que de sensibilité aux faux négatifs.")
    elif selected_option == "Résultats avec masques":
        st.subheader("Résumé des résultats sur 4 classes avec masques")
        st.image(resume_masques)
        st.write("Comme pour l’étude à deux classes, l’application de masques entraîne une réduction des mesures de "
                 "performances, mais l’architecture basée sur EfficientNetB1 conserve néanmoins des scores assez "
                 "élevés.")

    st.write("---")

    # Contexte
    st.markdown("<h5 style='text-align: center; color: black;'>Optimisation des hyperparamètres </h5>",
                unsafe_allow_html=True, )
    st.write(" ")
    st.markdown("-   Pour affiner davantage la performance de nos modèle choisi, EfficientNetB1 et VGG16, nous avons "
                "employé Keras Tuner pour l'optimisation des hyperparamètres. Cette démarche a été guidée par un code "
                "de recherche aléatoire (`RandomSearch`), ciblant spécifiquement la minimisation de la perte de "
                "validation (`val_loss`) sur un total de 50 essais (`max_trials`).")
    st.markdown("- Outre la sélection des meilleurs hyperparamètres, cette étape nous a permis de tester l'efficacité "
                "de la congélation et de la décongélation des couches dans les modèles de base.")
    st.markdown("- Les modèles les plus performants utilisés pour l'étude finale étaient celui basé sur "
                "l'architecture EfficientNet avec 31 couches du modèle de base dégelées, et celui basé sur "
                "l'architecture VGG16 avec 4 couches dégelées.")
    st.write(" ")

    st.markdown("<h5 style='text-align: center; color: black;'>Etude avec masques vs. sans masques </h5>",
                unsafe_allow_html=True, )
    st.write(" ")
    st.markdown(
        "-   Nos résultats indiquent une performance généralement inférieure des modèles lorsque des masques "
        "numériques sont appliqués pour cibler la région pulmonaire.")
    st.markdown(
        "- Une raison possible pourrait être la perte d'information contextuelle qui pourrait aider le modèle à "
        "différencier entre les diverses classes.")

    st.markdown("<h5 style='text-align: center; color: black;'>Faux positifs et faux négatifs </h5>",
                unsafe_allow_html=True, )
    st.write(" ")
    st.markdown("-   Dans le contexte clinique, la précision du diagnostic est cruciale. Un faux positif, "
                "c'est-à-dire la classification erronée d'un patient sain comme étant malade, peut conduire à des "
                "traitements inutiles et induire un stress psychologique considérable pour le patient.")
    st.markdown("-   Dans notre étude, tous les modèles ont montré une faible proportion de faux positifs et de faux "
                "négatifs, mais il est crucial de prendre ces erreurs en compte.")
    st.markdown("- Dans l’étude binaire « Sain vs Malade », le modèle VGG16 a affiché le plus faible taux de faux "
                "négatifs, avec seulement 59 cas mal classés parmi les 996 réellement malades. Ce résultat pourrait "
                "faire de VGG16 un choix préférable dans un contexte clinique où minimiser les faux négatifs est une "
                "priorité. Cependant, il est important de considérer également d'autres métriques de performance et "
                "les spécificités de l'application clinique en question.")
    st.write(" ")

    st.markdown("<h5 style='text-align: center; color: black;'>Tnterprétabilité du modèle </h5>",
                unsafe_allow_html=True, )
    st.write(" ")
    st.markdown("-   Afin d'offrir une meilleure compréhension des décisions prises par notre modèle EfficientNetB1, "
                "nous avons fait appel à la technique Grad-CAM (Gradient-weighted Class Activation Mapping).")
    st.markdown("-   Dans le cadre de notre étude, l'implémentation de Grad-CAM a révélé une focalisation cohérente "
                "et médicalement pertinente des zones d'intérêt, renforçant ainsi la crédibilité de nos résultats.")
    st.write(" ")

    st.write("---")
    st.markdown("<h4 style='text-align: center; color: black;'>Résultats de l'étude de 4 classes sans masques</h4>",
                unsafe_allow_html=True, )

    # Matrices de confusion et courbes d'entrainement
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("VGG16")
        st.image(conf_enet, use_column_width=True)
        st.write(" ")
        st.image(courbe_enet, use_column_width=True)

    with col2:
        st.subheader("EfficientNetB1")
        st.image(conf_vgg, use_column_width=True)
        st.write("---")
        st.image(courbe_vgg, caption="Courbe d'entrainement", use_column_width=True)

    # GradCAM
    st.write("---")
    st.markdown("<h4 style='text-align: center; color: black;'>Résultats du GradCAM sur EfficientNetB1, 4 classes "
                "sans masques </h4>", unsafe_allow_html=True, )
    st.write("  ")
    st.write("GradCAM de prédictions correctes")
    st.image(correct)
    st.write("  ")
    st.write("  ")
    st.write("GradCAM de prédictions incorrectes")
    st.image(incorrect)
