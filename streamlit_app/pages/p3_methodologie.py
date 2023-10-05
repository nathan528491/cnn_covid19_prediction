# Importation des bibliothèques
import streamlit as st
from PIL import Image

sidebar_name = "🧪 Méthodologie et Préprocessing"

# Creation des variables pour les images qu'on va charger plus tard
masque = Image.open(r"images\radio_masquee.png")
masque2 = Image.open(r"images\masque.png")
flip = Image.open(r"images\pic_turn.png")


def run():
    # L'en-tête de la page

    st.markdown("<h2 style='text-align: center; color: black;'>Méthodologie et Préprocessing </h2>",
                unsafe_allow_html=True, )
    st.write("---")

    tab1, tab2 = st.tabs(["Méthodologie", "Préprocessing"])

    with tab1:

        st.markdown("<h4 style='text-align: center; color: black;'>Méthodologie </h4>", unsafe_allow_html=True, )
        st.write(" ")

        # Fonction pour créer sous-titres
        def subheading_with_bullet_points(subheading, points):
            st.markdown(f"<strong>{subheading}<strong>", unsafe_allow_html=True)
            st.markdown(points, unsafe_allow_html=True)

        # Étape 1
        etape1_points = """-   Établir des résultats de référence à l'aide d'un simple réseau neuronal convolutif (
        LeNet5) sur deux classes de sortie (« sain » et « malade »). -   Catégories « COVID », « Lung Opacity » et « 
        Viral Pneumonia » groupées comme « malade ». -   5000 images par classe. -   Essais sur des images masquées 
        et non masquées."""
        subheading_with_bullet_points("Étape 1", etape1_points)

        # Étape 2
        etape2_points = """-   Appliquer les techniques d'apprentissage par transfert (transfer learning) pour 
        essayer plusieurs autres modèles CNN dont la viabilité a été prouvée en matière de classification d'images, 
        avec des niveaux de complexité et des besoins de calcul variables. -   Modèles choisis : ResNet152, Xception, 
        VGG16, EfficientNetB1. -   Études sur 2 classes et les 4 classes originales. -   Essais sur des images 
        masquées et non masquées. -   Essais sur des jeux de données avec data augmentation."""
        subheading_with_bullet_points("Étape 2", etape2_points)

        # Étape 3
        etape3_points = """-   Choisir le meilleur modèle en termes de performance sur le jeu de données (accuracy) 
        et le régler afin d'en améliorer les performances. -   Essais de congélation et de décongélation (freezing 
        and unfreezing) des couches du modèle. -   Appliquer une GradCam afin d'interpréter notre modèle et de 
        comprendre comment il définit ses classifications."""
        subheading_with_bullet_points("Étape 3", etape3_points)

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

        st.markdown("<h4 style='text-align: center; color: black;'>Préprocessing </h4>", unsafe_allow_html=True, )
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
            st.image(image, caption=f"Exemple de {selected_option}")

            # Afficher le text
            st.write(text)

            # Afficher seulement si "Étape 3" est choisi
            if selected_option == "Data augmentation":
                code = selected_data["code"]
                st.code(code, language="python")
