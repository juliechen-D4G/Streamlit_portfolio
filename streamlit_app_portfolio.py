import streamlit as st

# 1. Global Config
st.set_page_config(
    page_title="Julie Chen | Data, Policy & Impact",
    page_icon="🌍",
    layout="wide"
)

# 2. Define Pages (En pointant vers les fichiers correspondants)
home_page = st.Page(
    "Home/about_me.py",  # <-- On pointe vers le nouveau fichier
    title="Home", 
    icon="🏠", 
    default=True
)

climate_page = st.Page(
    "Sustainability/Climate_change.py", 
    title="Climate Change", 
    icon="🌱"
)

gender_page = st.Page(
    "Social_Justice/Gender_Equality.py", 
    title="Gender Equality", 
    icon="⚖️"
)

# 3. Navigation setup
pg = st.navigation({
    "Main": [home_page],
    "Sustainability": [climate_page],
    "Social Justice": [gender_page]
})

# 4. Run the selected page
pg.run()
