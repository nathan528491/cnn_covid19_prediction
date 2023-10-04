"""

Config file for Streamlit App

"""

from streamlit_app.member import Member


TITLE = "My Awesome App"

TEAM_MEMBERS = [
    Member(
        name="Hassan Burke",
        linkedin_url="#",
        github_url="#",
    ),
    Member(
        name="Matthieu Khairallah",
        linkedin_url="#",
        github_url="#",
    ),
    Member(
        name="Juliette Greco",
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
