# Importation des bibliothèques
import streamlit as st
from PIL import Image
from streamlit_app.texts import dataviz
from streamlit_app.config import st_markdown
import path
import sys

dir = path.Path(__file__).parent.parent.parent
sys.path.append(dir)

sidebar_name = "📊 DataViz"

# Creation des variables pour les images qu'on va charger plus tard
class_bar = Image.open(dir + "/streamlit_app/assets/images/classes2.png")
provenance = Image.open(r"streamlit_app\assets\images\provenance.png")
radios_classe = Image.open(r"streamlit_app\assets\images\images_classes.png")
moyennes = Image.open(r"streamlit_app\assets\images\moyenne_type.png")
diff = Image.open(r"streamlit_app\assets\images\diff.png")
eigen = Image.open(r"streamlit_app\assets\images\eigen.png")
img_pix = Image.open(r"streamlit_app\assets\images\pix_dist_norm.png")
pix_dist = Image.open(r"streamlit_app\assets\images\source_pix_dist.png")


def run():
    # Titre de la page
    st_markdown('Visualisation des Données', 'h2')

    # Création des tabs pour chaque élément de la data viz
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Métadonnées", "Échantillon par Classe", "Moyennes par Classe",
                                            "Différences Entres Classes", "Distribution des Pixels"])

    # Chargement des images et descriptions pour tab 1
    with tab1:
        st_markdown('Métadonnées', 'h4')
        st.write(" ")

        st_markdown("Nombres d'images par classe", 'h4', 'left')
        st.image(class_bar)
        st.write(dataviz.images_par_classes)

        st.write("---")

        st_markdown("Provenance des images", 'h4', 'left')
        st.image(provenance)
        st.write(dataviz.provenance_images)

    # Chargement des images et descriptions pour tab 2
    with tab2:
        st_markdown("Échantillon par Classe", 'h4')
        st.write(" ")

        st.image(radios_classe)
        st.write(dataviz.echantillon_par_classe)

    # Chargement des images et descriptions pour tab 3
    with tab3:
        st_markdown('Moyennes par Classe', 'h4')
        st.write(" ")

        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.image(moyennes)

        st.write(dataviz.moyenne_par_classe)

    # Chargement des images et descriptions pour tab 4
    with tab4:
        st_markdown('Différences Entres Classes', 'h4')
        st.write(" ")

        st.image(diff)
        st.write(dataviz.differences_images)

    # Chargement des images et descriptions pour tab 5
    with tab5:
        st_markdown('Distribution des Pixels', 'h4')
        st.write(" ")

        st_markdown('Exemple', 'h4', 'left')
        st.image(img_pix)
        st.write(dataviz.exemple_distribution_pixel)

        st.write("---")

        st_markdown('Distribution par Classe', 'h4', 'left')
        st.image(pix_dist)
        st.write(dataviz.distribution_par_classe)

    # # Chargement des images et descriptions pour tab 6
    # with tab6:
    #     st_markdown('Eigenimages', 'h4')
    #     st.write(" ")

    #     st.image(eigen)
    #     st.write("""Nous avons généré des eigenimages pour chaque image de chaque classe.""")
