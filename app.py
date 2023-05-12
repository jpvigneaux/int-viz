import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder")

df = pd.read_csv('gapminder_tidy.csv')  #The data

continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

with st.sidebar:
    continent = st.selectbox(label='Choose a continent', options=continent_list)
    metric = st.selectbox(label='Choose a metric', options=metric_list)

query = f"continent=='{continent}' & metric=='{metric}'"   #query with formatted string
df_gdp_o = df.query(query)   
fig = px.line(df_gdp_o, x='year', y='value', color='country', title='GDP for Countries in Oceania')


st.plotly_chart(fig, use_container_width=True)
