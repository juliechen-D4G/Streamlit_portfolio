import streamlit as st
import pandas as pd
import plotly.express as px
import os
import kaggle

# 1. TITRE SIMPLE (Vérifie qu'il n'y a pas de virgule à la fin)
st.title("Climate Change | Data Viz")

# 2. CONFIGURATION API (Assure-toi que c'est bien ici)
os.environ['KAGGLE_USERNAME'] = st.secrets["KAGGLE_USERNAME"]
os.environ['KAGGLE_KEY'] = st.secrets["KAGGLE_KEY"]

@st.cache_data
def load_major_city_data():
    dataset = "berkeleyearth/climate-change-earth-surface-temperature-data"
    file_name = "GlobalLandTemperaturesByMajorCity.csv"
    kaggle.api.dataset_download_file(dataset, file_name, path='./data')
    try:
        df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.zip")
    except:
        df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    return df.dropna(subset=['AverageTemperature'])

# 3. AFFICHAGE
try:
    df = load_major_city_data()
    st.success("Données chargées avec succès !")
    st.write("Aperçu des données :")
    st.dataframe(df.head(10))
except Exception as e:
    st.error(f"Erreur : {e}")

st.write(df['City'].unique())


