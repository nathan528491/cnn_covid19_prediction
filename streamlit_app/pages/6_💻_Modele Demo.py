import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import os
import random
import seaborn as sns
import cv2
from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

import tensorflow as tf
import keras
from keras_tuner.tuners import RandomSearch
from keras.applications import EfficientNetB1
from keras.layers import GlobalAveragePooling2D, Dense, Dropout
from keras.models import Sequential, load_model
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.applications.efficientnet import preprocess_input

# Page large
st.set_page_config(layout='wide')

#Titre de la page
st.write('''
         # CoviNet
         ## Détection de la COVID-19 grâce au deep learning
         ''')

#Creation des variables pour les images qu'on va charger plus tard
logo = Image.open(r"C:\Users\Hassam\Documents\app\images\new_logo.png")

#Paramètres du sidebar
sidebar_name = "CoviNet"
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown(sidebar_name)
st.sidebar.info(
    """Auteurs : Hassan Burke, Juliette Greco, \n
Matthieu Khairallah, Nathan Lancman) \n
Cohort Data Scientist Juillet 2022 \n
DataScientest""")

# Générateur d'images
image_folder = r"C:\Users\Hassam\Documents\app\radios"

image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Sélection de trois images aléatoires
random_images = random.sample(image_files, 3)

# Afficher les images à l'écran
st.markdown('<h2 style="color:black;">Générateur d\'images aléatoires</h2>', unsafe_allow_html=True)

# Créer une rangée pour afficher les images et les noms
row = st.columns(3)

# Fonction pour sélectionner trois images distinctes aléatoirement
def select_random_images(image_files):
    return random.sample(image_files, 3)

# Sélectionner initialement trois images aléatoires distinctes
random_images = select_random_images(image_files)

# Afficher les images initiales avec leurs noms
image_elements = []
for i, image_file in enumerate(random_images):
    image_path = os.path.join(image_folder, image_file)
    image_elements.append(row[i].image(image_path, caption=image_file, use_column_width=True))

# Ajouter un bouton pour générer d'autres images
if st.button("Générer d'autres images"):
    # Sélectionner à nouveau trois images aléatoires distinctes
    random_images = select_random_images(image_files)

    # Effacer d'abord les images existantes en réaffectant des valeurs vides
    for i in range(3):
        image_elements[i].empty()

    # Afficher les nouvelles images avec leurs noms
    for i, image_file in enumerate(random_images):
        image_path = os.path.join(image_folder, image_file)
        image_elements[i] = row[i].image(image_path, caption=image_file, use_column_width=True)
    
#Le modèle
st.markdown('<h2 style="color:black;">Notre modèle basé sur EfficientNetB1</h2>', unsafe_allow_html=True)

#File uploader
#@st.cache_resource(hash_funcs={"MyUnhashableClass": lambda _: None})
upload = st.file_uploader('Insert image for classification', type=['png','jpg'])
c1, c2 = st.columns(2)
if upload is not None:
  im = Image.open(upload)
  img = np.asarray(im)
  
  # Redimensionner l'image à la taille attendue par le modèle (240x240)
  image = cv2.resize(img, (240, 240))
  img = preprocess_input(image)
  img = np.expand_dims(img, 0)
  img = img.reshape(240, 240)
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertissez en RVB si nécessaire
  img_resized = cv2.resize(img_rgb, (240, 240))
  img_with_channel = np.expand_dims(img_resized, axis=0)
  c1.header('Input Image')
  c1.image(im)
  c1.write(img.shape)

  #Chargement de notre modèle
  enet = load_model(r"C:\Users\Hassam\Documents\app\modeles\efficientNet_4classes_31unfrozen.h5")

  #Prediction on model
  preds = enet.predict(img_with_channel)
  # Choix du seuil
  threshold = 0.5
  # Prédiction de la classe en utilisant le seuil
  y_pred = (preds > threshold).astype(int)
  
  c2.header('Output')
  c2.subheader('Predicted class :')
  if y_pred == 0:
    c2.write("COVID-19")
  elif y_pred == 1:
    c2.write("Lung Opacity")
  elif y_pred == 2:
    c2.write("Sain")
  else:
    c2.write("Viral Pneumonia")
  
  # Obtenir l'indice de la classe prédite avec la probabilité la plus élevée
  predicted_class_index = np.argmax(preds)

  # Obtenir la probabilité associée à la classe prédite
  predicted_class_prob = preds[0][predicted_class_index]

  # Afficher l'indice de la classe prédite
  c2.header('Output')
  c2.subheader('Predicted class index:')
  c2.write(predicted_class_index)

  # Afficher la probabilité associée à la classe prédite
  c2.subheader('Predicted class probability:')
  c2.write(predicted_class_prob)






