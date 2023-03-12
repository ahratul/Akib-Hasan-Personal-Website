import streamlit as st
import loaders as hc
import time

st.title("Work History")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("👨‍💼Work History👨‍💼")
with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)
st.write("---")

st.markdown("Current Job")
st.write("🚧", "** DevOps Engineer | SPYCE5 GMBH **")
st.write("📍 Berlin ,Germany 🇩🇪")
st.write("Employment type: Part-Time")
st.write("01/03/2023- Present")

st.write("---")



# --- JOB 1
st.write("🚧", "** Master Thesis Student | Fraunhofer Institute for Production Technology IPT **")
st.write("📍 Aachen, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type: Full-Time")
st.write("01/03/2023- Present")

st.write("---")


st.write("🚧", "** Working Student Software Developer | Resolve Biosciences GMBH **")
st.write("📍 Monheim am Rhein, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type : Part-Time")
st.write("15/11/2022-28/02/2023")

st.write("---")

# --- JOB 2

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

# --- JOB 3
st.write('\n')
st.write("🚧", "** Working Student Software Developer | xarvio® Digital Farming Solutions GMBH **")
st.write("📍 Cologne, North Rhine-Westphalia ,Germany 🇩🇪")
st.write("Employment type Part-Time")
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

JOB_REFERENCE = {
    "Job Reference From Previous Company ": "https://drive.google.com/file/d/1GeWT2y0mgHR9uiZOwXa3yQrQdOC_WbYX/view?usp=sharing",
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