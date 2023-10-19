# Importation des bibliothèques
import streamlit as st
from PIL import Image
from streamlit_app.texts import dataviz
from streamlit_app.config import st_markdown
import plotly.express as px
import path
import pandas as pd

directory = path.Path(__file__).parent.parent.parent

sidebar_name = "📊 DataViz"

# Creation des variables pour les images qu'on va charger plus tard
radios_classe = Image.open(directory + "/streamlit_app/assets/images/images_classes.png")
moyennes = Image.open(directory + "/streamlit_app/assets/images/moyenne_type.png")
diff = Image.open(directory + "/streamlit_app/assets/images/diff.png")
eigen = Image.open(directory + "/streamlit_app/assets/images/eigen.png")
img_pix = Image.open(directory + "/streamlit_app/assets/images/pix_dist_norm.png")
pix_dist = Image.open(directory + "/streamlit_app/assets/images/source_pix_dist.png")

full_df = pd.read_csv(directory + '/data/metadata.csv')
full_df['target'] = full_df['FILE NAME'].apply(lambda x: x[:1])
full_df['target'] = full_df['target'].replace(
    {'C': 'COVID-19', 'N': 'Normal', 'V': 'Viral Pneumonia', 'L': 'Lung Opacity'})
liste_labels = ['Normal', 'Lung Opacity', 'Covid-19', 'Viral Pneumonia']
color_theme = {'Normal': '#008FD5', 'Lung Opacity': '#FC4F30', 'COVID-19': '#E5AE38', 'Viral Pneumonia': '#6D904F'}

df = pd.DataFrame(dict(
    label=['Normal', 'Lung Opacity', 'COVID-19', 'Viral Pneumonia'],
    value=[10192, 6012, 3616, 1345]))


def plots_1():
    fig1 = px.pie(df,
                  values='value',
                  names='label',
                  color='label',
                  title='Proportion de la variable cible',
                  color_discrete_map=color_theme)

    fig2 = px.bar(df,
                  x='label',
                  y='value',
                  color='label',
                  title='Distribution de la variable cible',
                  color_discrete_map=color_theme)

    fig1.update_layout(autosize=False, width=350)
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    fig2.update_layout(
        autosize=False,
        width=350,
        yaxis_title="Nombre d'images")
    fig2.update_xaxes(visible=False)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, theme="streamlit")
    with col2:
        st.plotly_chart(fig2, theme="streamlit")


def plots_2():
    df_groupby = full_df.groupby('target')['URL'].value_counts().unstack(0)
    df_groupby['sum'] = df_groupby.sum(axis=1)
    df_groupby = df_groupby[['Normal', 'Lung Opacity', 'COVID-19', 'Viral Pneumonia', 'sum']]
    fig = px.bar(df_groupby.sort_values(by='sum'),
                 x=df_groupby.sort_values(by='sum').iloc[:, :-1].columns.values,
                 y=df_groupby.sort_values(by='sum').index.values,
                 orientation='h',
                 # log_x=True,
                 labels={'x': 'Nombre d\'images', 'y': 'Source'},
                 color_discrete_map=color_theme)

    fig.update_layout(
        yaxis={
            'tickmode': 'array',
            'tickvals': list(range(0, len(df_groupby))),
            'ticktext': [f"{df_groupby.sort_values(by='sum').index.values[i][8:18]} ..." for i in
                         range(len(df_groupby))],
        },
        xaxis_title="Nombre d'images",

    )
    st.plotly_chart(fig, theme="streamlit")


def run():
    # Titre de la page
    st_markdown('Visualisation des Données', 'h2')

    # Création des tabs pour chaque élément de la data viz
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Métadonnées", "Échantillon par Classe", "Moyennes par Classe",
                                            "Différences Entres Classes", "Distribution des Pixels"])

    # Chargement des images et descriptions pour tab 1
    with tab1:
        st_markdown('Métadonnées', 'h4')
        st.write(" ")

        st_markdown("Nombres d'images par classe", 'h4', 'left')
        plots_1()
        st.write(dataviz.images_par_classes)

        st.write("---")

        st_markdown("Provenance des images", 'h4', 'left')
        plots_2()
        st.write(dataviz.provenance_images)

    # Chargement des images et descriptions pour tab 2
    with tab2:
        st_markdown("Échantillon par Classe", 'h4')
        st.write(" ")

        st.image(radios_classe)
        st.write(dataviz.echantillon_par_classe)

    # Chargement des images et descriptions pour tab 3
    with tab3:
        st_markdown('Moyennes par Classe', 'h4')
        st.write(" ")

        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.image(moyennes)

        st.write(dataviz.moyenne_par_classe)

    # Chargement des images et descriptions pour tab 4
    with tab4:
        st_markdown('Différences Entres Classes', 'h4')
        st.write(" ")

        st.image(diff)
        st.write(dataviz.differences_images)

    # Chargement des images et descriptions pour tab 5
    with tab5:
        st_markdown('Distribution des Pixels', 'h4')
        st.write(" ")

        st_markdown('Exemple', 'h4', 'left')
        st.image(img_pix)
        st.write(dataviz.exemple_distribution_pixel)

        st.write("---")

        st_markdown('Distribution par Classe', 'h4', 'left')
        st.image(pix_dist)
        st.write(dataviz.distribution_par_classe)

    # # Chargement des images et descriptions pour tab 6
    # with tab6:
    #     st_markdown('Eigenimages', 'h4')
    #     st.write(" ")

    #     st.image(eigen)
    #     st.write("""Nous avons généré des eigenimages pour chaque image de chaque classe.""")
