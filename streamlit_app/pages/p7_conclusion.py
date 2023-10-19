import streamlit as st
from streamlit_app.texts import conclusion
from streamlit_app.config import st_markdown
import path
import sys

dir = path.Path(__file__).parent.parent.parent
sys.path.append(dir)

sidebar_name = "📑 Conclusion"


def display_tab(title, texts):
    st_markdown(title, 'h4')
    st.write(" ")

    for text in texts:
        st.markdown(text)


def run():
    st_markdown('Conclusions', 'h2')

    tab1, tab2, tab3 = st.tabs(["Conclusion", "Limites", "Axes d'amélioration"])

    with tab1:
        display_tab('Conclusion', conclusion.conclusion)

    with tab2:
        display_tab('Limites', conclusion.limites)

    with tab3:
        display_tab('Axes d\'amélioration', conclusion.axes_amelioration)
