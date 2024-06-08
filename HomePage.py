from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Md_Akib_Hasan_.pdf"
profile_pic = current_dir / "assets" / "cv.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Serendipity | Md Akib Hasan"
PAGE_ICON = "✨"
NAME = "Md Akib Hasan"
DESCRIPTION = """
I am an experienced IT professional with over 5 years of diverse experience in IT support, IT administration, network engineering, DevOps, and backend development. I am currently pursuing a Master's in Communication System and Networking at Technische Hochschule Köln, with one course remaining to complete. I am proficient in English and at an intermediate level in German. My expertise includes solving complex problems, network configuration, NAS, Linux, SOPHOS Firewall, SOPHOS Access Points, and Cisco devices. I am seeking a full-time position where I can leverage my skills and continue to grow professionally. 
"""


EMAIL = "ahratul740@gmail.com"

SOCIAL_MEDIA = {
    "🌐 LinkedIn": "https://www.linkedin.com/in/akibhasanratul/",
    "🐙 GitHub": "https://github.com/ahratul",
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
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
    <div style="text-align: justify; color: black;">
    <ul style="list-style-type: none; padding-left: 0;">
        <li>💻 Computer Hardware</li>
        <li>🛠️ Technical Support</li>
        <li>☁️ Cloud-Based System Management</li>
        <li>📝 IT Ticketing Process Optimization</li>
        <li>🔍 System Auditing and Vulnerability Management</li>
        <li>📚 IT Documentation Management</li>
        <li>🏃‍♂️ Agile Methodologies</li>
        <li>🎓 Cisco Certified</li>
        <li>🖥️ Windows Server</li>
        <li>🔥 Firewalls, VMware</li>
        <li>🖇️ Microsoft Office</li>
        <li>👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Big Query</li>
        <li>📊 Data Visualization: PowerBi, Plotly</li>
        <li>📚 Modeling: Logistic Regression, Linear Regression, Decision Tree, Neural Network, Anomaly Detection</li>
        <li>☁️ Cloud Computing: AWS, GCP, Oracle, Azure</li>
        <li>🗄️ Databases: Postgres, MongoDB, MySQL, Oracle</li>
        <li>🧮 API: Flask, FastAPI, Lambda</li>
        <li>📎 Microsoft Office: Word, PowerPoint, Excel</li>
        <li>🎛️ Repository: GitHub, Bitbucket</li>
        <li>🐛 Debugging</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
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
