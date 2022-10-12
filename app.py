from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "cv.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Md Akib Hasan"
PAGE_ICON = ":wave:"
NAME = "Md Akib Hasan"
DESCRIPTION = """ Software Developer with Specialized in Cloud Computing, Experience working as a Data Analyst. """

EMAIL = "ahratul740@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/akibhasanratul/",
    "GitHub": "https://github.com/ahratul",
}

JOB_REFERENCE = {
    "Job Reference From Previous Company ": "https://drive.google.com/file/d/1GeWT2y0mgHR9uiZOwXa3yQrQdOC_WbYX/view?usp=sharing",
}

PUBLICATIONS = {
    "📖  Unmanned Aerial Vehicle for Cleaning the High Rise Buildings --> (This paper represents a design of an "
    "ardupilot mega (APM) based remote-controlled unmanned aerial vehicle system for cleaning the high rise buildings "
    "windows. The design is developed with the remote-controlled system, which allows the workers to give security "
    "and maintenance of a surrounding area. )IEEE · Jan 15, 2019":
        "https://ieeexplore.ieee.org/document/8644476/references#references",
}

PROJECTS = {
    "🏆 Developing APIs with Google Cloud's Apigee API Platform": "https://www.coursera.org/account/accomplishments/specialization/certificate/WJ3YGE2DMXME",
    "🏆 Preparing for the Google Cloud Associate Cloud Engineer Exam": "https://www.coursera.org/account/accomplishments/certificate/XSNHZXFKYDZC",
    "🏆 Essential Google Cloud Infrastructure: Foundation": "https://www.coursera.org/account/accomplishments/certificate/B9J3HJBUJUZA",
    "🏆  Google Cloud Fundamentals: Core Infrastructure": "https://www.coursera.org/account/accomplishments/certificate/LNK4JT5CU2SX",
    "🏆  Reliable Google Cloud Infrastructure: Design and Process": "https://www.coursera.org/account/accomplishments/certificate/GCLTPKVTEZNN",
    "🏆  Google Cloud Big Data and Machine Learning Fundamentals": "https://coursera.org/share/4e1957007b18571628bde76503275a5b",
    "🏆  Elastic Google Cloud Infrastructure: Scaling and Automation": "https://www.coursera.org/account/accomplishments/certificate/6WP3KNQCFFW9",
    "🏆  Architecting with Google Compute Engine Specialization": "https://www.coursera.org/account/accomplishments/specialization/certificate/SP87Q9Q8V8YB",
    "🏆  How Google does Machine Learning": "https://www.coursera.org/account/accomplishments/certificate/QDLBCBUU35RT",
    "🏆  API Design and Fundamentals of Google Cloud's Apigee API Platform": "https://coursera.org/share/08fc56980d5bf9bb06cd0f3d5d44ff95",
    "🏆  End-to-End Machine Learning with TensorFlow on GCP": "https://www.coursera.org/account/accomplishments/certificate/UU4KXSTWRDUE",
    "🏆  Smart Analytics, Machine Learning, and AI on GCP": "https://www.coursera.org/account/accomplishments/certificate/UVLJBNRRMJ6Y",
    "🏆  Getting Started With Application Development": "https://www.coursera.org/account/accomplishments/certificate/H5STHPGRQWJR",
    "🏆  Networking in Google Cloud: Defining and Implementing Networks": "https://www.coursera.org/account/accomplishments/certificate/NHSLRRRBY4RJ",
    "🏆  Managing Security in Google Cloud": "https://www.coursera.org/account/accomplishments/certificate/UREBWVSAA227",
    "🏆  API Security on Google Cloud's Apigee API Platform": "https://www.coursera.org/account/accomplishments/certificate/PUVNCB2ULTTP",
    "🏆  Full Stack Software Developer Assessment": "https://www.coursera.org/account/accomplishments/certificate/2W43VWJGNT94",
    "🏆  Storing, Retrieving, and Processing JSON data with Python": "https://www.coursera.org/account/accomplishments/certificate/UNHTNDPG2LBC",
    "🏆  Developing APIs with Google Cloud's Apigee API Platform": "https://www.coursera.org/account/accomplishments/specialization/certificate/WJ3YGE2DMXME",
    "🏆  DevOps on AWS: Release and Deploy": "https://www.coursera.org/account/accomplishments/certificate/TPEKYKUURG78",
    "🏆  Containerization Using Docker": "https://www.coursera.org/account/accomplishments/certificate/Z8RUHPJ7VRYY",
    "🏆  Beginners Guide to YAML Syntax": "https://www.coursera.org/account/accomplishments/certificate/8QWFG6NCMRNM",
    "🏆  Neural Network Visualizer Web App with Python": "https://www.coursera.org/account/accomplishments/certificate/L7T3XMTC6L27",
    "🏆  GUI Programming: Create a Login System in Python": "https://www.coursera.org/account/accomplishments/certificate/PBR9PZ3QMTBT",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
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
        label=" 📄 Download Resume",
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

# -----education-history------

st.write('\n')
st.subheader("Education History")
st.write("---")

# --- Education 1
st.write("🏫",
         "** Bachelor of Science in Electronic and Electrical Engineering | American International University-Bangladesh**")
st.write("05/2015 - 02/2020")
st.write(
    """
- ► Digital Design with System Verilog, VHDL and FPGAs.
- ► Microwave Engineering.
"""
)

# --- Education  2
st.write('\n')
st.write("🏫", "** Master’s in communication system and Networking | Technische Hochschule Köln **")
st.write("04/2020 - Present")
st.write(
    """
- ► Machine Learning
- ► Large Cloud Based Software Development
- ► Next Generation Networking
- ► Digital Signal Processing.
- ► Cryptography.

"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "** Internship in Data Analyst | xarvio® Digital Farming Solutions**")
st.write("10/2021 - 12/2021")
st.write(
    """
- ► Cleaned unstructured data for data analysis and Confidential tasks and pipelines.
- ► Analyzed over 22 years data (2000-2022) to make Dose Response model
- ► Used Python and the Soil API to get raw data and reprocessed it for a data science tasks .
- ► Used Natural Language Processing ML libraries to train a Robust Regression model for Nonlinear data analysis.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "** Working Student Software Developer | xarvio® Digital Farming Solutions**")
st.write("01/2022 - 08/2022")
st.write(
    """
- ► Proficient in creating high-volume micro services and APIs.
- ► Expertise in Django, Python, and Python application frameworks like Django REST, Flask, and Fast Api.
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing.
- ► Working with server less Amazon Web Services (AWS) technologies Like Lambda to minimize the cost.
- ► Proven track record with testing, editing, and debugging web apps

"""
)

# --- Job Reference ---
st.write('\n')
st.subheader("Job Reference")
st.write("---")
for project, link in JOB_REFERENCE.items():
    st.write(f"[{project}]({link})")

# --- Publications ---
st.write('\n')
st.subheader("Publications")
st.write("---")
for project, link in PUBLICATIONS.items():
    st.write(f"[{project}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
