import streamlit as st

sidebar_name = "Conclusion"


def run():
    st.markdown("<h2 style='text-align: center; color: black;'>Conclusions </h2>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Conclusion", "Limites", "Axes d'amélioration"])

    with tab1:
        st.markdown("<h4 style='text-align: center; color: black;'>Conclusion </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.markdown("-   Les modèles que nous avons testé ont été évalués en tenant compte de plusieurs critères "
                    "essentiels en milieu clinique : la précision du diagnostic, le taux de faux positifs et de faux "
                    "négatifs, ainsi que l'efficacité en termes de temps et de puissance de calcul.")
        st.markdown(
            "-   Notre choix de retenir EfficientNetB1 comme modèle optimal s'est basé sur son équilibre entre une "
            "haute précision de classification et une grande efficacité en termes de ressources.")
        st.markdown(
            "-   **Notre modèle obtient de meilleures performances sur un support moins efficace dans la détection de "
            "la COVID-19, la radiographie, que celui de Yang et al. (2020) entraîné sur des CT-scans.**")
        st.markdown(
            "-   les résultats obtenus sont prometteurs et suggèrent que l'application de techniques d'apprentissage "
            "en profondeur dans le domaine médical est non seulement viable mais aussi extrêmement bénéfique.**")

    with tab2:
        st.markdown("<h4 style='text-align: center; color: black;'>Limites </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.markdown(
            "-   Nous avons observé que l'application de masques numériques pour cibler la région pulmonaire pourrait "
            "avoir des effets négatifs sur la performance du modèle, soulevant des questions sur l'efficacité de "
            "cette technique.")
        st.markdown(
            "-   Bien que l'ensemble de vingt mille images soit considérable, une base de données de taille plus "
            "importante pourrait fournir de meilleurs résultats.")
        st.markdown(
            "-   Bien que nous n'ayons pas pu constater de différences significatives entre les sources d'images, "
            "nous ne pouvons pas exclure qu'un ensemble d'images plus standardisé (provenant d'un seul hôpital, "
            "par exemple) puisse améliorer les performances du modèle.")

    with tab3:
        st.markdown("<h4 style='text-align: center; color: black;'>Axes d'amélioration </h4>", unsafe_allow_html=True, )
        st.write(" ")
        st.markdown("-   La robustesse des modèles face à des images de mauvaise qualité n'a pas été testée.")
        st.markdown(
            "-   nous avons identifié tardivement que les couches «Dense» utilisées dans la comparaison initiale des "
            "modèles n'étaient pas uniformes. Ceci pourrait avoir introduit un biais dans nos résultats et mérite "
            "d'être corrigé dans des recherches futures.")
