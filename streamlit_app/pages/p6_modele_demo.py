import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import os
import random
import cv2
from PIL import Image

from keras.models import load_model
from keras.applications.efficientnet import preprocess_input

from streamlit_app.config import st_markdown
import path

directory = path.Path(__file__).parent.parent.parent

sidebar_name = "💻 Démo du modèle"

labels_4_classes = ['Covid', 'Lung Opacity', 'Normal', 'Viral Pneumonia']
labels_2_classes = ['Malade', 'Sain']


def preprocess_input_model1(img):
    img = cv2.resize(img, (240, 240))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (240, 240))
    img = preprocess_input(img_resized)
    return img


def preprocess_input_model2(img):
    img = cv2.resize(img, (224, 224))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img = preprocess_input(img_resized)
    return img


# File uploader
# @st.cache_resource(hash_funcs={"MyUnhashableClass": lambda _: None}, experimental_allow_widgets=True)
def upload_image():
    print('uploading image')
    uploaded_image = st.file_uploader('Insert image for classification', type=['png', 'jpg'])
    return uploaded_image


def get_img_array(img):
    array = keras.utils.img_to_array(img)
    array = np.expand_dims(array, axis=0)
    return array


def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    grad_model = keras.models.Model(
        model.inputs, [model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    grads = tape.gradient(class_channel, last_conv_layer_output)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()


def return_gradcam(img, heatmap, alpha):
    heatmap = np.uint8(255 * heatmap)

    jet = plt.colormaps.get_cmap("jet")

    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]

    jet_heatmap = keras.utils.array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
    jet_heatmap = keras.utils.img_to_array(jet_heatmap)

    superimposed_img = jet_heatmap * alpha + img
    superimposed_img = keras.utils.array_to_img(superimposed_img)

    return superimposed_img


def grad_cam(img, model, alpha, last_conv_layer_name):
    img_array = get_img_array(img)
    heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name)

    return return_gradcam(img, heatmap, alpha)


model_paths = {
    "EfficientNetB1": directory + "/models/model_enet_4_classes.h5",
    "EfficientNetB1 Masques":  directory + "/models/model_enet_4_classes_mask.h5",
    "VGG16":  directory + "/models/model_vgg_4_classes.h5",
    "VGG16 Masques":  directory + "/models/model_vgg_4_classes_mask.h5",
}


def run():
    #  GÉNÉRATEUR D'IMAGES

    # Chemin pour les images
    image_folder = directory + "/streamlit_app/assets/radios"

    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # Sélection de trois images aléatoires
    # random_images = random.sample(image_files, 3)

    # Afficher les images à l'écran
    st.write(" ")
    st_markdown('Essayons nos modèles !', 'h2')

    # Créer une rangée pour afficher les images et les noms
    col = st.columns(3)

    # Sélectionner initialement trois images aléatoires distinctes
    random_images = random.sample(image_files, 3)

    # Afficher les images initiales avec leurs noms
    image_elements = []
    for i, image_file in enumerate(random_images):
        image_path = os.path.join(image_folder, image_file)
        image_elements.append(col[i].image(image_path, caption=image_file, use_column_width=True))
        print(image_path)

    # Ajouter un bouton pour générer d'autres images
    if st.button("Générer d'autres images"):
        # Sélectionner à nouveau trois images aléatoires distinctes
        random_images = random.sample(image_files, 3)
        print(random_images)

    # Effacer d'abord les images existantes en réaffectant des valeurs vides
    for i in range(3):
        image_elements[i].empty()

    # Afficher les nouvelles images avec leurs noms
    for i, image_file in enumerate(random_images):
        image_path = os.path.join(image_folder, image_file)
        print(image_path)
        image_elements[i] = col[i].image(image_path, caption=image_file, use_column_width=True)

    # APPLICATION DU MODÈLE
    st_markdown('Sélectionner un modèle', 'h2')
    selected_model = st.selectbox("Select Model", list(model_paths.keys()), index = 0, disabled = True)

    upload = upload_image()
    c1, c2 = st.columns(2)

    if upload is not None:
        im = Image.open(upload)
        img = np.asarray(im)

        # Preprocess the image based on the selected model
        if selected_model == "EfficientNetB1" or selected_model == "EfficientNetB1 Masques":
            img = preprocess_input_model1(img)

        elif selected_model == "VGG16" or selected_model == "VGG16 Masques":
            img = preprocess_input_model2(img)

        # Expand dimensions to match the model's input shape
        img_with_channel = np.expand_dims(img, axis=0)  # Define img_with_channel here

        c1.header('Input Image')
        c1.image(im)

        # Load the selected model
        selected_model_path = model_paths[selected_model]
        model = load_model(selected_model_path)

        # Prediction on model
        preds = model.predict(img_with_channel)
        # Predict the class using the threshold
        predicted_classes = np.argmax(preds, axis=1)

        print(preds)
        print(predicted_classes)

        # COVID-19 = 0, LO = 1, SAIN = 2, VP =3
        class_names = ["COVID-19", "Lung Opacity", "Sain", "Viral Pneumonia"]

        c2.header('Output')
        c2.subheader('Classe prédite :')

        for predicted_class in predicted_classes:
            c2.write(class_names[predicted_class])

        # Get the corresponding probabilities
        predicted_class_probs = preds[0][predicted_classes]

        c2.subheader('Probabilité de la classe prédite:')
        rounded_proba = round(predicted_class_probs[0], 3)
        c2.write(rounded_proba)

        # GRADCAM
        st_markdown('Sélectionner une couche du modèle', 'h2')

        layers = [layer.name for layer in model.layers if (isinstance(layer, keras.layers.Conv2D)
                                                           and 'conv' in layer.name)]
        selected_layer = st.selectbox("Select layer", layers)
        if st.button("Générer Grad-CAM"):
            col1, col2, col3 = st.columns([4, 8, 3])
            with col1:
                st.write(' ')
            with col2:
                st.image(grad_cam(img, model, 0.5, selected_layer),
                         width=299,
                         caption=f"Grad-CAM sur la couche {selected_layer}")
            with col3:
                st.write(' ')
