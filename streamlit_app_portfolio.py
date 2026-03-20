import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Julie Chen | Data, Policy & Impact",
    page_icon="🌍",
    layout="wide"
)

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stBadge {
        background-color: #e9ecef;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    # st.image("your_photo.jpg", caption="Julie Chen") 
    st.markdown("### Contact")
    st.write("📧 juliechrystelle.chen@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/juliecchen/)")
    st.write("📍 Santiago, Chile / Remote")
    st.write("---")
    st.markdown("### Languages")
    st.write("🇫🇷 Native | 🇬🇧 C2 (Fluent) | 🇪🇸 Proficient")

# --- HEADER ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Julie Chen")
    st.subheader("Data Analyst & PMP® Certified Project Manager")
    st.markdown("""
    **Bridging the gap between Data Intelligence and Public Policy.** With a background in **Sciences Po** (Public Policy), **MINES Paris** (Data Analysis), 
    and **Cambridge** (Sustainable Supply Chain), I specialize in transforming complex 
    datasets into actionable insights for social justice and environmental impact.
    """)

# --- SECTION: TRI-DIMENSIONAL EXPERTISE ---
st.write("---")
st.header("Core Expertise")

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("### 🏛️ Policy & Justice")
    st.write("Public policy analysis, social equity frameworks, and regulatory compliance.")
    st.caption("Double MA - Sciences Po Grenoble")

with kpi2:
    st.markdown("### 📊 Data Intelligence")
    st.write("Interactive data storytelling, web scraping, and advanced visualization.")
    st.caption("Data Analysis Certified - MINES Paris")

with kpi3:
    st.markdown("### 🚀 Strategic Leadership")
    st.write("PMO expertise, budget management, and sustainable value chain optimization.")
    st.caption("PMP® Certified & Cambridge SCM")

# --- SECTION: NAVIGATION ---
st.write("---")
st.info("👈 **Explore my work in the sidebar menu**: Data journalism investigations, impact dashboards, and supply chain case studies.")

# --- FOOTER ---
st.write("---")
st.caption("Portfolio built with Streamlit | 2026")

# --- SUMMARY PAGES ----
climate_page = st.Page(
    "Sustainability/Climate_change.py", title="Climate Change", icon="🌱"
)
gender_page = st.Page(
    "Social_Justice/Gender_Equality.py", title="Gender Equality", icon="⚖️"
)


# Page d'accueil (votre fichier actuel)
home_page = st.Page(
    "streamlit_app_portfolio.py", 
    title="Home", 
    icon="🏠", 
    default=True
)

# --- 2. CRÉATION DE LA NAVIGATION AVEC SECTIONS ---

pg = st.navigation({
    "Main": [home_page],
    "Sustainability": [climate_page],
    "Social Justice": [gender_page]
})

# --- 3. EXÉCUTION ---
pg.run()
