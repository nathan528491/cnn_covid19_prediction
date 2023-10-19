# Importation des bibliothèques
import streamlit as st
from PIL import Image
from streamlit_app.texts import methodologie
from streamlit_app.config import st_markdown
import path

directory = path.Path(__file__).parent.parent.parent

sidebar_name = "🧪 Méthodologie et Préprocessing"

# Creation des variables pour les images qu'on va charger plus tard
masque = Image.open(directory + "/streamlit_app/assets/images/radio_masquee.png")
masque2 = Image.open(directory + "/streamlit_app/assets/images/masque.png")
flip = Image.open(directory + "/streamlit_app/assets/images/pic_turn.png")


# Fonction pour créer sous-titres
def subheading_with_bullet_points(subheading, points):
    st.markdown(f"<strong>{subheading}<strong>", unsafe_allow_html=True)
    st.markdown(points, unsafe_allow_html=True)


def run():
    # Titre de la page
    st_markdown('Méthodologie et Préprocessing', 'h2')
    st.write("---")

    tab1, tab2 = st.tabs(["Méthodologie", "Préprocessing"])

    with tab1:
        st_markdown('Méthodologie', 'h4')
        st.write(" ")

        # Étapes
        for i, etape in enumerate(methodologie.etapes):
            subheading_with_bullet_points(f"Étape {i + 1}", etape)
            st.write(" ")

        # Réduire l'espace entre points
        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:20px;
                margin-bottom: 5px;
            }
            </style>
            ''', unsafe_allow_html=True)

    with tab2:
        st_markdown('Préprocessing', 'h4')
        st.write(" ")

        # Créer un dictionnaire pour mapper des options correspondant aux images and textes
        options_data = {
            "Adaptation de la taille des images": {
                "image": masque,
                "text": "Les images du jeu de données sont toutes de taille 299x299 pixels. Leurs masques associés"
                        "sont de 256x256 pixels. Nous avons dû procéder à un ajustement de la taille des images et "
                        "des masques pour les adapter aux différents modèles que nous avons testés.",
            },
            "Superposition des masques": {
                "image": masque2,
                "text": "Ces masques délimitent précisément la zone d'intérêt, permettant ainsi une focalisation sur "
                        "la région pulmonaire tout en réduisant le bruit provenant d'éléments non pertinents.",
            },
            "Data augmentation": {
                "image": flip,
                "text": "Nous avons procédé à une data augmentation dans l’étude des quatre classes afin de pouvoir "
                        "entrainer notre modèle sur un plus grand jeu de données.",
                "code": """
                    train_datagen = ImageDataGenerator(
                        rotation_range = 0.15,
                        width_shift_range = 0.2,
                        height_shift_range = 0.2,
                        shear_range = 0.2,
                        zoom_range = 0.2,
                        fill_mode = 'nearest')
                        """
            },
        }

        # Créer ub menu déroulant pour les étapes de preprocessing
        selected_option = st.selectbox("Sélectionner l'étape de préprocessing", list(options_data.keys()))

        # Afficher l'image et le text
        if selected_option:
            selected_data = options_data[selected_option]
            image = selected_data["image"]
            text = selected_data["text"]

            # Afficher l'image
            col1, col2, col3 = st.columns([1, 6, 1])
            with col2:
                st.image(image, caption=f"Exemple de {selected_option}")

            # Afficher le text
            st.write(text)

            # Afficher seulement si "Étape 3" est choisi
            if selected_option == "Data augmentation":
                code = selected_data["code"]
                st.code(code, language="python")
