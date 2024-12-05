import streamlit as st
import loaders as hc
import time

st.title("Work History")

# --- WORK HISTORY ---
st.write('\n')
st.subheader(                       "👨‍💼Work History👨‍💼"                   )
with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)


# --- JOB 1
st.write("🚧", "** IT Administrator |  REHUB digitale Planer **")
st.write("📍 Köln, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type: Part-Time")
st.write("01/01/2023- Present")
st.write(
    """
- ► Supported and maintained all company data and technological infrastructure for
    both international and nationwide locations.
- ► Upgraded, repaired, and configured computers, application software, servers, and
    various other peripherals.
- ► Provided end-user and remote support and technical assistance for server and
    client computers, enterprise applications, telecommunication systems, network
    components, etc.
- ► Provide initial response and manage problem resolution process for outages and
    problems.
- ► Supports server, network, and desktop-based software and applications.
- ► Provides day-to-day technical support to employee’s desktop systems software &
    hardware.
- ► Highly developed verbal and written communications
- ► Demonstrated knowledge of TCP/IP networking and the OSI model.

"""
)

st.write("---")

# --- JOB 2
st.write("🚧", "** Master Thesis Student | Fraunhofer Institute for Production Technology IPT **")
st.write("📍 Aachen, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type: Full-Time")
st.write("01/05/2023- 30/11/2023")
st.write(
    """
- ► Developed and successfully implemented a novel cyber-attack detection system
    utilizing Long Short-Term Memory (LSTM) neural networks in conjunction with side
    sensor data from CNC machines
- ► Demonstrated a deep understanding of cybersecurity principles and the ability to
    apply cutting-edge machine-learning techniques to enhance the security of critical
    industrial systems.
"""
)

st.write("---")

# --- JOB 3
st.write("🚧", "** DevOps Engineer | SPYCE5 GMBH **")
st.write("📍 Berlin ,Germany 🇩🇪")
st.write("Employment type: Part-Time")
st.write("01/03/2023- 01/05/2023")
st.write(
    """
- ► Led the design and implementation of AWS solutions for diverse clients, demonstrating expertise in architecting scalable and secure cloud infrastructure.
- ► Played a key role in enhancing security by implementing IAM policies, VPC configurations, and best practices for data protection.
- ► Demonstrated proficiency in architecting solutions using services like EC2, S3, RDS, and Lambda, ensuring high availability and fault tolerance.
"""
)


# --- JOB 4
st.write("---")

st.write("🚧", "** Working Student Software Developer | Resolve Biosciences GMBH **")
st.write("📍 Monheim am Rhein, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type : Part-Time")
st.write("15/11/2022-28/02/2023")
st.write(
    """
- ► Apache Airflow: Used Apache Airflow to schedule and automate data pipeline workflows for molecular cartography analysis.
- ► OpenCV:  Used OpenCV to develop computer vision algorithms for processing and analyzing molecular imaging data in molecular cartography.
- ► Computer Vision: Used Computer vision techniques to extract information from molecular imaging data in order to visualize molecular structures and analyze molecular interactions in molecular cartography.

"""
)

st.write("---")

# --- JOB 5
st.write('\n')
st.write("🚧", "** Working Student Software Developer | xarvio® Digital Farming Solutions GMBH **")
st.write("📍 Cologne, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type: Part-Time")
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


st.write("---")

# --- JOB 6

st.write("🚧", "** Internship in Data Analyst | xarvio® Digital Farming Solutions GMBH **")
st.write("📍 Cologne, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type: Full-time")
st.write("10/2021 - 12/2021")
st.write(
    """
- ► Cleaned unstructured data for data analysis and Confidential tasks and pipelines.
- ► Analyzed over 22 years data (2000-2022) to make Dose Response model
- ► Used Python and the Soil API to get raw data and reprocessed it for a data science tasks .
- ► Used Natural Language Processing ML libraries to train a Robust Regression model for Nonlinear data analysis.
"""
)

st.write("---")


JOB_REFERENCE = {
    "Job Reference From BASF ": "https://drive.google.com/file/d/1GeWT2y0mgHR9uiZOwXa3yQrQdOC_WbYX/view"
                                            "?usp=sharing",
    
    "Job Reference From Resolve Biosciences GMBH": "https://drive.google.com/file/d/1F8FeQgT13Oi5JwAXB8dEiASJLD5xBjk6/view?usp=sharing",
    "Job Reference From Fraunhofer Institute for Production Technology IPT": "https://drive.google.com/file/d/1OI0wR2C55b2QAymEXDw1kvWftX-4lRdA/view?usp=sharing",
 }


# --- Job Reference ---
st.write('\n')
st.subheader("Job Reference")
st.write("---")
for project, link in JOB_REFERENCE.items():
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
