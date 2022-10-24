from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "cv.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Serendipity | Md Akib Hasan"
PAGE_ICON = "✨"
NAME = "Md Akib Hasan"
DESCRIPTION = """ Software Developer with Specialized in Cloud Computing, Experience working as a Data Analyst. """

EMAIL = "ahratul740@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/akibhasanratul/",
    "GitHub": "https://github.com/ahratul",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume ",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- 👋️  Hello, I am Akib Hasan.
- ‍🎓️  Soon to be graduated with a Masters in Communication and Network Systems from TH Köln.
- 🌇  Living in Cologne Germany for my Masters degree. 
- 💪🏻  Excellent team-player and displaying strong sense of initiative on tasks
- 📜  Certified in into CCNAv7
- 📙  In the future, I want to be a Certified  Cloud Architecture Engineer.
- 💪🏻  My strength in Cloud Engineering, Web application design, Data Analysis, Visualization and Prediction.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻   Programming: Python (Scikit-learn, Pandas), SQL, Big Query
- 📊     Data Visualization: PowerBi, Plotly
- 📚     Modeling: Logistic Regression, Linear regression, Decision tree, Neural Network, Anomaly Detection
- ☁     Cloud Computing: AWS, GCP, Oracle,Azure
- 🗄️     Databases: Postgres, MongoDB, MySQL, Oracle
- 🧮️     API: Flask , Fast, Lambda
- 📎     Microsoft Office: Word, Powerpoint ,Excel
- 🎫     Jira
- 🎛️     Repository: Github, Bitbucket
- 📒     Confluence
- 🐛     Debugging



"""
)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    
    
    
    """,
    unsafe_allow_html=True,
)
