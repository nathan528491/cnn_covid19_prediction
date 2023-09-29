#Importation des bibliothèques
import streamlit as st
from PIL import Image

#Page large
st.set_page_config(layout="wide")

#Creation des variables pour les images
logo = Image.open(r"C:\Users\Hassam\Documents\app\images\new_logo.png")
cases = Image.open(r"C:\Users\Hassam\Documents\app\images\cases.png")
spend = Image.open(r"C:\Users\Hassam\Documents\app\images\gov_spend.png")

#Paramètres du sidebar
sidebar_name = "CoviNet"
st.sidebar.image(logo, use_column_width=True)
st.sidebar.markdown(sidebar_name)
st.sidebar.info(
    """Auteurs : Hassan Burke, Juliette Greco, \n
Matthieu Khairallah, Nathan Lancman) \n
Cohort Data Scientist Juillet 2022 \n
DataScientest""")

#L'en-tête de la page
st.write("""
         # CoviNet
         ## Détection de la COVID-19 grâce au deep learning
         """)
#Titres et sous-titres
st.write(" ")
st.markdown("<h4 style='text-align: center; color: black;'> <em> Auteurs: Juliette Greco, Matthieu Khairallah, Nathan Lancman, Hassan Burke <em> </h4>", unsafe_allow_html=True,)
st.markdown("<h4 style='text-align: center; color: black;'> <em> Conseiller du groupe: Gaël Penessot<em> </h4>", unsafe_allow_html=True,)

st.write("---")
st.markdown("<h2 style='text-align: center; color: black;'>Introduction </h2>", unsafe_allow_html=True,)

st.write(" ")
st.markdown("<h3 style='text-align: center; color: black;'>Contexte </h3>", unsafe_allow_html=True,)
st.write("""
         L'arrivée de la pandémie de COVID-19 a marqué une période difficile pour les nations et leurs systèmes de santé dans le monde entier. La propagation rapide de la maladie,
          avec une estimation de 44 % de la population mondiale infectée au moins une fois entre mars 2020 à la fin de 2021, a submergé les services médicaux et les systèmes de santé. \n
         
         Le test PCR (réaction en chaîne de la polymérase) a été largement reconnu comme le "gold standard" pour la détection du COVID-19. Cependant, lors des pics de la
         pandémie, la demande accrue de tests PCR a parfois entraîné des ruptures d'approvisionnement, limitant ainsi la capacité de dépistage. Face à cette situation,
        l'imagerie médicale a constitué une aternative pour le diagnostic. Les radiographies pulmonaires et les tomodensitogrammes (CT-scans) sont devenus des outils essentiels
        pour identifier les signes distinctifs de l'infection pulmonaire causée par le virus.
         """)



# Display the image with a caption
#st.image(spend, caption="Image Caption")
#st.image(spend, caption="Croissance des depenses gouvernemental sur la santé pendant la pandemie Covid-19)")
#st.write("""source: [World Bank](https://openknowledge.worldbank.org/server/api/core/bitstreams/4fa6b841-6a76-45a3-a527-a2bcaeb37c97/content""")

st.write(" ")
st.markdown("<h3 style='text-align: center; color: black;'>Objectifs </h3>", unsafe_allow_html=True,)
st.write("""
         Les algorithmes de deep learning ont démontré leur capacité à apprendre des caractéristiques complexes à partir de données brutes, en particulier dans 
         le domaine de la vision par ordinateur (computer vision). Dans le contexte médical, cette technologie a suscité un vif intérêt pour son potentiel à développer 
         des modèles de classification automatisés d'images médicales, tels que les radiographies pulmonaires, afin d'alléger la pression sur des systèmes de santé 
         et des capacités d'essai déjà mis à rude épreuve. \n

         A l’aide d’une banque d’images de radiographies pulmonaires librement disponibles sur le site web Kaggle, nous avons entrainé des modèles de deep learning afin de 
         vérifier si les techniques d'apprentissage profond (deep learning) sont capable de détecter efficacement la présence, ou non, de COVID-19.
         """)




 
 