import streamlit as st
import loaders as hc
import time

st.title("Projects")
st.subheader("📚Projects📚")
st.write("---")
with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)

HANDS_ON_PROJECT = {
    "🧪  Create-Growth-Models-With-Gompertz-Four-PL-Five-PL-Sigmoid-Power-Law": "https://ahratul-dose-responsecurved-with-different-grow-homepage-uy3vus.streamlit.app/",
    "🧪  Neural-Network-With-Streamlit-Flask-Web-Visualizer": "https://ahratul-neural-network-with-streamlit-flask-web-visu-app-7jni48.streamlitapp.com/",
    "🧪  Support-Vector-Machine-LogisticRegression-RandomForestClassifier-With-Streamlit-": "https://ahratul-support-vector-machine-logisticregression-ra-app-giizd1.streamlitapp.com/",
    "🧪  Data-Visualization-Streamlit-Web-App": "https://ahratul-data-visulalization-streamlit-web-app-app-12bty7.streamlitapp.com/",
    "🧪  Selenium-Architecture--In-Docker--Containers": "https://github.com/ahratul/Selenium-Architecture--In-Docker--Containers",
    "🧪  European-Train-Stations-Maps": "https://ahratul-european-train-stations-maps-app-g3jlbi.streamlitapp.com/",
    "🧪  KMeans-Clustering-Customization-Streamlit-Web-App": "https://ahratul-kmeans-clustering-customization-streamlit-we-app-7srkf6.streamlitapp.com/",
    "🧪  Predicting-Wage-of-Players-And-the-nations": "https://ahratul-predicting-wage-of-player-app-bi5xhh.streamlitapp.com/",
    "🧪  World-Population-EDA-With-World-Map-Visualization": "https://ahratul-world-population-eda-with-world-map-visualiz-app-dvnhfz.streamlitapp.com/",
    "🧪  Hotel-Booking-Demand-EDA-Visualization": "https://ahratul-hotel-booking-demand-eda-visualization-app-j8kpox.streamlitapp.com/",
    "🧪  Iris Classification WebApp": "https://ahratul-iris-species-webapp-with-streamlit-app-m8eaqt.streamlit.app/",
}

PROJECTS = {
    "🏆  Kubernetes in AWS: Create Cluster in EKS in your own VPC": "https://www.coursera.org/account/accomplishments/certificate/ME6BZKG2HVLN",
    "🏆  Kubernetes: Basic Architecture and First Deployment": "https://www.coursera.org/account/accomplishments/certificate/6P3T7ZS3VEXT",
    "🏆  Build a Machine Learning Web App with Streamlit and Python": "https://www.coursera.org/account/accomplishments/certificate/X39R728EYLHU",
    "🏆  Create digit recognition web app with Streamlit": 'https://www.coursera.org/account/accomplishments/certificate/YMB27RX2SU25',
    "🏆  Deploy a Web Application in AWS Elastic Kubernetes Service": "https://www.coursera.org/account/accomplishments/certificate/7X7PBM4NNY9U",
    "🏆  Developing APIs with Google Cloud's Apigee API Platform": "https://www.coursera.org/account/accomplishments/specialization/certificate/WJ3YGE2DMXME",
    "🏆  Preparing for the Google Cloud Associate Cloud Engineer Exam": "https://www.coursera.org/account/accomplishments/certificate/XSNHZXFKYDZC",
    "🏆  Essential Google Cloud Infrastructure: Foundation": "https://www.coursera.org/account/accomplishments/certificate/B9J3HJBUJUZA",
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
    "🏆  DevOps on AWS: Release and Deploy": "https://www.coursera.org/account/accomplishments/certificate/TPEKYKUURG78",
    "🏆  Containerization Using Docker": "https://www.coursera.org/account/accomplishments/certificate/Z8RUHPJ7VRYY",
    "🏆  Beginners Guide to YAML Syntax": "https://www.coursera.org/account/accomplishments/certificate/8QWFG6NCMRNM",
    "🏆  Neural Network Visualizer Web App with Python": "https://www.coursera.org/account/accomplishments/certificate/L7T3XMTC6L27",
    "🏆  GUI Programming: Create a Login System in Python": "https://www.coursera.org/account/accomplishments/certificate/PBR9PZ3QMTBT",

}

# --- Hands_on_projects ---
st.write('\n')
st.subheader("👨‍🔬 👨‍🔬 Some of my Python Projects 🐍🐍 ")
st.write("---")
for project, link in HANDS_ON_PROJECT.items():
    st.write(f"[{project}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


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
