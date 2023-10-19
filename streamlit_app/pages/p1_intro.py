import streamlit as st
from PIL import Image
from streamlit_app.texts import intro
from streamlit_app.config import st_markdown
import path
import sys

dir = path.Path(__file__).parent.parent.parent
sys.append.path(dir)

sidebar_name = "🏠 Introduction"

# Creation des variables pour les images qu'on va charger plus tard
nnet = Image.open(r"streamlit_app/assets/images/nnet7.jpeg")


def run():
    print(dir)
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image(nnet, width=200)

    st.write(" ")

    # Titres et sous-titres
    st_markdown('<em> Auteurs: Juliette Greco, Matthieu Khairallah, Nathan Lancman, Hassan Burke <em>', 'h4')
    st_markdown('<em> Conseiller du groupe: Gaël Penessot<em>', 'h4')

    st.write("---")

    st_markdown('Introduction', 'h2')
    st.write(" ")

    st_markdown('Contexte', 'h3')
    st.write(intro.contexte)
    st.write(" ")

    st_markdown('Objectifs', 'h3')
    for objectif in intro.objectifs:
        st.markdown(objectif)
