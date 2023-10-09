"""

Config file for Streamlit App

"""

from streamlit_app.member import Member
import streamlit as st

TITLE = "CoviNet - Détection de la COVID-19 grâce au deep learning"

TEAM_MEMBERS = [
    Member(
        name="Hassan Burke",
        linkedin_url="#",
        github_url="#",
    ),
    Member(
        name="Juliette Greco",
        linkedin_url="#",
        github_url="#",
    ),
    Member(
        name="Matthieu Khairallah",
        linkedin_url="#",
        github_url="#",
    ),
    Member(
        name="Nathan Lancman",
        linkedin_url="#",
        github_url="#",
    ),
]

PROMOTION = "Promotion Bootcamp Data Scientist - July 2023"


def st_markdown(string, tag='h1', text_align='center'):
    return st.markdown(f"<{tag} style='text-align: {text_align}; color: black;'>{string}</{tag}>", unsafe_allow_html=True)
