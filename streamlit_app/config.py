"""

Config file for Streamlit App

"""

from streamlit_app.member import Member
import streamlit as st

TITLE = "CoviNet - Détection de la COVID-19 grâce au deep learning"

TEAM_MEMBERS = [
    Member(
        name="Hassan Burke",
        linkedin_url="https://www.linkedin.com/in/hassan-burke/",
        github_url="https://github.com/hbburke",
    ),
    Member(
        name="Juliette Greco",
        linkedin_url="https://www.linkedin.com/in/juliette-greco/",
        github_url="https://github.com/jltt-grc",
    ),
    Member(
        name="Matthieu Khairallah",
        linkedin_url="https://www.linkedin.com/in/matthieukhairallah/",
        github_url="https://github.com/matthieukhl",
    ),
    Member(
        name="Nathan Lancman",
        linkedin_url="https://www.linkedin.com/in/nathan-lancman/",
        github_url="https://github.com/nathan528491",
    ),
]


def st_markdown(string, tag='h1', text_align='center'):
    return st.markdown(f"<{tag} style='text-align: {text_align}; color: black;'>{string}</{tag}>", unsafe_allow_html=True)
