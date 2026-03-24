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

    def parse_coord(coord):
        if pd.isna(coord):
            return None
        coord = str(coord)
        if coord[-1] in ['N', 'E']:
            return float(coord[:-1])
        elif coord[-1] in ['S', 'W']:
            return -float(coord[:-1])
        return float(coord)
    
    df['Latitude'] = df['Latitude'].apply(parse_coord)
    df['Longitude'] = df['Longitude'].apply(parse_coord)
    return df.dropna(subset=['AverageTemperature'])

# 3. AFFICHAGE
try:
    df = load_major_city_data()
    st.success("Données chargées avec succès !")
    st.write("Aperçu des données :")
    st.dataframe(df.head(10))
except Exception as e:
    st.error(f"Erreur : {e}")

st.header("🌍 Carte Interactive des Températures Mondiales")

try:
    df = load_major_city_data()

    # --- PRÉPARATION DES DONNÉES POUR LA CARTE ---
    # Pour que l'animation soit fluide et lisible, on groupe par année et par ville
    # On calcule la température moyenne annuelle par ville
    map_df = df.groupby(['Year', 'City', 'Country', 'Latitude', 'Longitude'])['AverageTemperature'].mean().reset_index()

    # On filtre pour ne garder qu'une donnée tous les 5 ou 10 ans 
    # Cela évite que la carte soit trop lourde à charger dans le navigateur
    year_step = st.slider("Choisir l'intervalle d'années (Précision)", 1, 20, 10)
    map_df = map_df[map_df['Year'] % year_step == 0]

    # Add an absolute size column
    map_df['size_col'] = map_df['AverageTemperature'] + abs(map_df['AverageTemperature'].min()) + 1

    # --- CRÉATION DE LA CARTE ---
    fig = px.scatter_geo(
        map_df,
        lat="Latitude",
        lon="Longitude",
        color="AverageTemperature",
        hover_name="City",
        size="size_col", # Optionnel : la taille du point varie avec la température
        animation_frame="Year",      # C'est ici que la magie du "curseur temporel" opère
        projection="natural earth",
        color_continuous_scale=px.colors.sequential.YlOrRd, # Dégradé Jaune -> Orange -> Rouge
        range_color=[map_df['AverageTemperature'].min(), map_df['AverageTemperature'].max()],
        labels={'AverageTemperature': 'Temp (°C)'},
        title="Évolution de la température des grandes métropoles"
    )

    # Optimisation de la mise en page
    fig.update_layout(height=600, margin={"r":0,"t":50,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

    # --- NOTE MÉTHODOLOGIQUE ---
    st.caption("""
    **Note :** Les points représentent les 100 plus grandes villes mondiales du dataset Berkeley Earth. 
    Utilisez le curseur en bas de la carte pour observer l'évolution depuis 1750.
    """)

except Exception as e:
    st.error(f"Erreur lors de la création de la carte : {e}")


