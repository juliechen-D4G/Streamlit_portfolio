import streamlit as st

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stBadge { background-color: #e9ecef; }
    </style>
    """, unsafe_allow_html=True)

# Header & Content
st.title("Julie Chen")
st.subheader("Data Analyst & PMP® Certified Project Manager")

# SIDEBAR
with st.sidebar:
    st.markdown("### Contact")
    st.write("📧 juliechrystelle.chen@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/juliecchen/)")
    st.write("📍 Santiago, Chile / Remote")
    st.write("---")
    st.markdown("### Languages")
    st.write("🇫🇷 Native | 🇬🇧 C2 (Fluent) | 🇪🇸 Proficient")

# HEADER
col1, col2 = st.columns([2, 1])
with col1:
    st.title("Julie Chen")
    st.subheader("Data Analyst & PMP® Certified Project Manager")
    st.markdown("""
        **Bridging the gap between Data Intelligence and Public Policy.** With a background in **Sciences Po** (Public Policy), **MINES Paris** (Data Analysis), 
        and **Cambridge** (Sustainable Supply Chain), I specialize in transforming complex 
        datasets into actionable insights for social justice and environmental impact.
        """)

# EXPERTISE
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

st.write("---")
st.info("👈 **Explore my work in the sidebar menu**: Data journalism investigations, impact dashboards, and supply chain case studies.")
    
st.write("---")
st.caption("Portfolio built with Streamlit | 2026")
