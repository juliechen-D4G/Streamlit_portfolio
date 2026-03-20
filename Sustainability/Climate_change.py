import streamlit as st
import pandas as pd
import plotly.express as px
import os
import kaggle

# Page Title and Intro
st.title("Climate Change| Data Viz"),
st.write("In this page we will explore Climate Change data")

# --- CONFIGURATION API KAGGLE ---
os.environ['KAGGLE_USERNAME'] = st.secrets["KAGGLE_USERNAME"]
os.environ['KAGGLE_KEY'] = st.secrets["KAGGLE_KEY"]

@st.cache_data
def load_major_city_data():
    dataset = "berkeleyearth/climate-change-earth-surface-temperature-data"
    file_name = "GlobalLandTemperaturesByMajorCity.csv"
    
    # Téléchargement via l'API
    kaggle.api.dataset_download_file(dataset, file_name, path='./data')
    
    # Lecture du fichier (plus besoin de chunks ici car le fichier est léger)
    # Note : Kaggle télécharge souvent le fichier compressé en .zip
    try:
        df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv.zip")
    except:
        df = pd.read_csv("./data/GlobalLandTemperaturesByMajorCity.csv")
        
    # Nettoyage
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df['Month'] = df['dt'].dt.month
    df = df.dropna(subset=['AverageTemperature'])
    return df

st.header("🌡️ Analyse des Températures : Grandes Métropoles")

try:
    with st.spinner('Chargement des données Berkeley Earth...'):
        df = load_major_city_data()
    
    # On affiche les données seulement si le chargement a réussi
    st.dataframe(df.head(10))

except Exception as e:
    st.error(f"Erreur lors du chargement des données : {e}")
