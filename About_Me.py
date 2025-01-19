import streamlit as st
import pandas

# ----Configuration----

st.set_page_config(page_title="My Portfolio", page_icon="📊", layout="wide")

# ----Header----

with st.container():
    col1, col2 = st.columns([1, 3])
    
    # Photo de profil
    with col1:
        st.image("images/doraemon.jpeg", width=150)

    # Présentation
    with col2:
        st.title("👋 Bonjour, je suis Edgar Peronnin")
        st.write("📊 **Data Scientist | Machine Learning Engineer**")
        st.write("Passionné par l'IA et l'analyse de données, je développe des solutions innovantes pour transformer les données en décisions stratégiques.")

        # Liens Réseaux Sociaux
        st.markdown("[LinkedIn](https://www.linkedin.com/in/edgar-peronnin-018086226/) | [GitHub](https://github.com/eddd33)")

# ----------------- COMPÉTENCES -----------------
st.markdown("---")
st.header("🛠️ Compétences Techniques")

cols = st.columns(3)
skills = [
    ["📊 Data Science", "💻 Python, SQL", "📈 Machine Learning"],
    ["🧠 Deep Learning", "🌐 NLP & Computer Vision", "🔢 Statistiques & Mathématiques"],
]

for col, skill_list in zip(cols, skills):
    for skill in skill_list:
        col.write(f"- {skill}")

# ----------------- PROJETS -----------------
st.markdown("---")
st.header("🚀 Projets Récents")

bib_proj = "🔍 Quand l'IA nous aide à trouver un mot de passe robuste"
bib_description = """Article retraçant la conception d'une preuve de concept 
                ayant pour but de détecter la robustesse d'un mot de passe en fonction de son 
                pattern et de la ressemblance avec des mots de passe ayant déjà fuité. Cet article 
                a été co-rédigé dans le cadre de mon stage de fin d'études au CERT Michelin 
                avec Pierre Raufast et Maxime Escourbiac."""

with st.expander(f"**{bib_proj}**"):
    st.write(bib_description)
    st.markdown("[🔗 Voir l'article'](https://blogit.michelin.io/when-ai-help-us-find-a-strong-password/)")

projects = {
    "📸 Reconnaissance d'images en Deep Learning": "Utilisation de CNN pour classifier des images avec TensorFlow et PyTorch.",
    "📊 Analyse Prédictive de Ventes": "Modélisation de séries temporelles pour prédire les ventes futures."
}

for project, description in projects.items():
    with st.expander(f"**{project}**"):
        st.write(description)
        st.markdown("[🔗 Voir le projet](https://github.com/tonprofil)")

# ----------------- PIED DE PAGE -----------------
st.markdown("---")
st.write("💡 Portfolio développé avec [Streamlit](https://streamlit.io/) | 🚀 © 2025 Edgar Peronnin")