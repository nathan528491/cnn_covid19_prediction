import streamlit as st
from PIL import Image

sidebar_name = "🏠 Introduction"

# Creation des variables pour les images qu'on va charger plus tard
nnet = Image.open(r"images\nnet7.jpeg")


def run():
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image(nnet, width=200)

    # Titres et sous-titres
    st.write(" ")
    st.markdown("<h4 style='text-align: center; color: black;'> <em> Auteurs: Juliette Greco, Matthieu Khairallah, "
                "Nathan Lancman, Hassan Burke <em> </h4>", unsafe_allow_html=True, )
    st.markdown("<h4 style='text-align: center; color: black;'> <em> Conseiller du groupe: Gaël Penessot<em> </h4>",
                unsafe_allow_html=True, )

    st.write("---")
    st.markdown("<h2 style='text-align: center; color: black;'>Introduction </h2>", unsafe_allow_html=True, )

    st.write(" ")
    st.markdown("<h3 style='text-align: center; color: black;'>Contexte </h3>", unsafe_allow_html=True, )
    st.write("L'arrivée de la pandémie de COVID-19 a marqué une période difficile pour les nations et leurs systèmes de"
             "santé dans le monde entier. La propagation rapide de la maladie,"
             "avec une estimation de 44 % de la population mondiale infectée au moins une fois entre mars 2020 à la fin"
             "de 2021, a submergé les services médicaux et les systèmes de santé. \n"

             "Le test PCR (réaction en chaîne de la polymérase) a été largement reconnu comme le 'gold standard' pour"
             " la détection du COVID-19. Cependant, lors des pics de la"
             " pandémie, la demande accrue de tests PCR a parfois entraîné des ruptures d'approvisionnement, limitant"
             "  ainsi la capacité de dépistage. Face à cette situation,"
             "l'imagerie médicale a constitué une alternative pour le diagnostic. Les radiographies pulmonaires et les"
             " tomodensitogrammes (CT-scans) sont devenus des outils essentiels"
             "pour identifier les signes distinctifs de l'infection pulmonaire causée par le virus.")

    st.write(" ")
    st.markdown("<h3 style='text-align: center; color: black;'>Objectifs </h3>", unsafe_allow_html=True, )

    st.markdown("-   Les algorithmes de deep learning ont démontré leur capacité à apprendre des caractéristiques "
                "complexes à partir de données brutes, en particulier dans le domaine de la vision par ordinateur "
                "(computer vision).")
    st.markdown("-   Dans le contexte médical, cette technologie a suscité un vif intérêt pour son potentiel à "
                "développer des modèles de classification automatisés d'images médicales, tels que les radiographies"
                " pulmonaires, afin d'alléger la pression sur des systèmes de santé et des capacités d'essai déjà mis"
                " à rude épreuve.")
    st.markdown("-   **A l’aide d’une banque d’images de radiographies pulmonaires librement disponibles sur le site "
                "web Kaggle, nous avons entrainé des modèles de deep learning afin de vérifier si les techniques "
                "d'apprentissage profond (deep learning) sont capable de détecter efficacement la présence, ou non,"
                " de COVID-19.**")
