# Importation des bibliothèques
import streamlit as st
from PIL import Image

sidebar_name = "📐 Modélisation"

# Creation des variables pour les images qu'on va charger plus tard
lenet = Image.open(r"images\lenet.jpg")
xception = Image.open(r"images\xception.png")
vgg = Image.open(r"images\vgg.jpg")
resnet = Image.open(r"images\resnet.png")
enet = Image.open(r"images\enet.png")
conf_lenet = Image.open(r"images\2_lenet_conf.png")
courbe_lenet = Image.open(r"images\2_lenet_courbe.png")
conf_resnet = Image.open(r"images\2_resnet_conf.png")
courbe_resnet = Image.open(r"images\2_resnet_courbe.png")
conf_xception = Image.open(r"images\2_xcep_conf.png")
courbe_xception = Image.open(r"images\2_xcep_courbe.png")
conf_vgg = Image.open(r"images\2_vgg_conf.png")
courbe_vgg = Image.open(r"images\2_vgg_courbe.png")
conf_enet = Image.open(r"images\2_enet_conf.png")
courbe_enet = Image.open(r"images\2_enet_courbe.png")
resume_sans = Image.open(r"images\2_classes.png")
resume_masques = Image.open(r"images\2_classes_masques.png")

def run():
    # Titre de la page
    st.markdown("<h2 style='text-align: center; color: black;'>Modélisation </h2>", unsafe_allow_html=True, )
    st.write("---")

    st.markdown("-   Les réseaux neuronaux convolutifs (CNN) sont excellent dans la classification des images en "
                "raison de leur capacité à apprendre et à extraire automatiquement des caractéristiques hiérarchiques "
                "des images.")
    st.markdown("-   Nous avons testé 5 modèles avant d'en choisir un, sur la base de la précision et des exigences "
                "de calcul. L'architecture Lenet5, un modèle relativement simple, a servi comme référence contre des "
                "modèles «state of the art»")
    st.markdown("-   Nous avons d'abord testé les modèles sur deux classes (« sain » et « malade ») afin de "
                "sélectionner les modèles les plus performants pour la classification des quatre classes.")



    # Création des tabs pour chaque modèle
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["LeNet5", "ResNet152", "Xception", "VGG16", "EfficientNetB1"])

    # Chargement des images et descriptions pour tab 1
    with tab1:
        st.markdown("<h4 style='text-align: center; color: black;'>LeNet5 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(lenet)
        st.write("L'architecture de LeNet-5 est structurée avec une alternance de couches convolutives et de couches"
                 "de mise en commun, suivies de couches entièrement connectées. "
                 "Il se compose généralement de deux couches convolutives avec activation ReLU, de deux couches de mise"
                 "en commun maximale et de couches entièrement connectées."
                 "Même si des modèles plus récents l'ont dépassés, la simplicité de LeNet-5 par rapport"
                 "à d'autres modèles de classification, le rend efficace en termes de calcul.")
        st.write("---")
        st.markdown("<h5 style='text-align: center; color: black;'>Matrice de confusion : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(conf_lenet)
        st.write(" ")
        st.markdown("<h5 style='text-align: center; color: black;'>Courbe d'entrainement : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )

        st.image(courbe_lenet)

    # Chargement des images et descriptions pour tab 2
    with tab2:
        st.markdown("<h4 style='text-align: center; color: black;'>ResNet152 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(resnet)
        st.write("ResNet152 est structuré comme un réseau résiduel profond, avec des blocs résiduels qui permettent"
                 " un apprentissage très profond du réseau sans le problème du gradient de fuite."
                 "Sa profondeur exceptionnelle, qui lui permet de capturer des caractéristiques hiérarchiques "
                 "complexes dans les images, et son efficacité à atteindre une précision de pointe dans diverses tâches"
                 "de classification d'images.")
        st.write("---")
        st.markdown("<h5 style='text-align: center; color: black;'>Matrice de confusion : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(conf_resnet)
        st.write(" ")
        st.markdown("<h5 style='text-align: center; color: black;'>Courbe d'entrainement : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(courbe_resnet)

    # Chargement des images et descriptions pour tab 3
    with tab3:
        st.markdown("<h4 style='text-align: center; color: black;'>Xception </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(xception)
        st.write("Xception utilise des convolutions séparables dans le sens de la profondeur. Il est structuré avec "
                 "plusieurs blocs de convolutions séparables dans le sens de la profondeur, suivis par des connexions "
                 "de saut et une mise en commun de la moyenne globale. Xception est connu"
                 " pour ses performances élevées en termes de précision et d'efficacité de calcul, grâce à ses "
                 "convolutions séparables dans le sens de la profondeur.")
        st.write("---")
        st.markdown("<h5 style='text-align: center; color: black;'>Matrice de confusion : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(conf_xception)
        st.write(" ")
        st.markdown("<h5 style='text-align: center; color: black;'>Courbe d'entrainement : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(courbe_xception)

    # Chargement des images et descriptions pour tab 4
    with tab4:
        st.markdown("<h4 style='text-align: center; color: black;'>VGG16 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(vgg)
        st.write("VGG16 est une architecture de réseau neuronal convolutif qui se compose de 16 couches de poids, "
                 "dont 13 couches convolutives et 3 couches entièrement connectées. Il est connu pour sa simplicité et"
                 " son architecture uniforme avec de petits filtres convolutifs 3x3. ")
        st.write("---")
        st.markdown("<h5 style='text-align: center; color: black;'>Matrice de confusion : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(conf_vgg)
        st.write(" ")
        st.markdown("<h5 style='text-align: center; color: black;'>Courbe d'entrainement : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(courbe_vgg)

    # Chargement des images et descriptions pour tab 5
    with tab5:
        st.markdown("<h4 style='text-align: center; color: black;'>EfficientNetB1 </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.image(enet)
        st.write("""EfficientNetB1 fait partie de la famille EfficientNet d'architectures de réseaux neuronaux, 
        connues pour leur efficacité en termes de taille de modèle et d'exigences de calcul. EfficientNetB1 utilise 
        une mise à l'échelle composée pour équilibrer la profondeur, la largeur et la résolution afin d'obtenir un 
        compromis solide entre la précision et l'efficacité de calcul.. """)
        st.write("---")
        st.markdown("<h5 style='text-align: center; color: black;'>Matrice de confusion : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(conf_enet)
        st.write(" ")
        st.markdown("<h5 style='text-align: center; color: black;'>Courbe d'entrainement : Sain vs Malade </h5>",
                    unsafe_allow_html=True, )
        st.image(courbe_enet)

    # Tableau pour resumer les résultats
    selected_option = st.selectbox("Sélectionner une option", ["Résultats sans masques", "Résultats avec masques"])

    if selected_option == "Résultats sans masques":
        st.subheader("Résumé des résultats sur 2 classes sans masques")
        st.image(resume_sans)
        st.write("Comme attendu, les modèles plus complexes ont généralement obtenu de meilleurs résultats que LeNet5, "
                 "VGG16 et EfficientNet étant particulièrement performants.")
    elif selected_option == "Résultats avec masques":
        st.subheader("Résumé des résultats sur 2 classes avec masques")
        st.image(resume_masques)
        st.write("Nous constatons une nette diminution des performances lorsque des masques sont ajoutés, "
                 "les architectures EfficientNet et ResNet152 conservant leurs performances mieux que les autres.")
