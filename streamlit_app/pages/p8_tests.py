# Importation des bibliothèques
import pandas as pd
import streamlit as st
# from PIL import Image
import plotly.express as px

# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
import path

directory = path.Path(__file__).parent.parent.parent

sidebar_name = "Testing"

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
    # st.dataframe(df)

    # fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])
    # fig.add_trace(go.Pie(labels=df.label,
    #                      values=df.value,
    #                      name="target"), 1, 1)
    # fig.add_trace(go.bar(x=df.label, y=df.value, base = df.label), 1, 2)
    # fig.add_trace(go.bar(df, x=df.label, y=df.value, base = df.label), 1, 2)

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

    fig1.update_layout(
        autosize=False,
        width=350)
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    fig2.update_layout(
        autosize=False,
        width=350,
        yaxis_title="Nombre d'images", )
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
    # st.dataframe(df_groupby.sort_values(by='sum').iloc[:, :-1])
    fig = px.bar(df_groupby.sort_values(by='sum'),
                 x=df_groupby.sort_values(by='sum').iloc[:, :-1].columns.values,
                 y=df_groupby.sort_values(by='sum').index.values,
                 orientation='h',
                 # log_x=True,
                 labels={'x': 'Nombre dimages', 'y': 'Source'},
                 color_discrete_map=color_theme)
    # fig.update_yaxes(visible=False, showticklabels=False)
    # show only part of y label
    # make the y label on 2 lines
    # fig.update_yaxes(tickfont=dict(size=8))
    # print([f"{df_groupby.sort_values(by='sum').index.values[i][8:18]} ..." for i in range(len(df_groupby))])

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


conf_test = pd.DataFrame([[233, 9, 8, 0],
                          [4, 231, 25, 1],
                          [6, 17, 205, 12],
                          [2, 0, 0, 247]])

conf_test = conf_test.apply(lambda x: (x * 100 / x.sum()), axis=1)


def plots_3():
    # make a classification matrix
    fig = px.imshow(conf_test,
                    labels=dict(x="Predicted", y="True"),
                    color_continuous_scale='Blues',
                    x=['COVID-19', 'Lung Opacity', 'Normal', 'Viral Pneumonia'],
                    y=['COVID-19', 'Lung Opacity', 'Normal', 'Viral Pneumonia'],
                    # add '%' to each cell
                    text_auto='.2f')

    fig.update_xaxes(side="bottom")
    st.plotly_chart(fig, theme="streamlit")


def run():
    plots_1()
    plots_2()
    plots_3()
