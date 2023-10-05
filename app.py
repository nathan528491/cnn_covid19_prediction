from collections import OrderedDict
import streamlit as st
import streamlit_app.config as config

from streamlit_app.pages import (p1_intro, p2_dataviz, p3_methodologie, p4_modelisation, p5_resultats, p6_modele_demo,
                                 p7_conclusion)

st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://datascientest.com/wp-content/uploads/2020/03/cropped-favicon-datascientest-1-32x32.png",
)

# Chargement du style CSS
# with open("streamlit_app/style.css", "r") as f:
#     style = f.read()
#
# st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# Pages
TABS = OrderedDict(
    [
        (p1_intro.sidebar_name, p1_intro),
        (p2_dataviz.sidebar_name, p2_dataviz),
        (p3_methodologie.sidebar_name, p3_methodologie),
        (p4_modelisation.sidebar_name, p4_modelisation),
        (p5_resultats.sidebar_name, p5_resultats),
        (p6_modele_demo.sidebar_name, p6_modele_demo),
        (p7_conclusion.sidebar_name, p7_conclusion),

    ]
)


def run():
    st.sidebar.image(
        "streamlit_app/assets/logo-datascientest.png",
        width=200,
    )
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    st.write("""
             # CoviNet
             ## Détection de la COVID-19 grâce au deep learning
             """)

    tab.run()


if __name__ == "__main__":
    run()
