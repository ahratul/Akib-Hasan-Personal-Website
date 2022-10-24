import streamlit as st
import loaders as hc
import time

st.title("Publications")
st.subheader("📰Publications📰")
st.write("---")
with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)

PUBLICATIONS = {
    "📖  Unmanned Aerial Vehicle for Cleaning the High Rise Buildings --> (This paper represents a design of an "
    "ardupilot mega (APM) based remote-controlled unmanned aerial vehicle system for cleaning the high rise buildings "
    "windows. The design is developed with the remote-controlled system, which allows the workers to give security "
    "and maintenance of a surrounding area. )IEEE · Jan 15, 2019":
        "https://ieeexplore.ieee.org/document/8644476/references#references",
}

# --- Publications ---
st.write('\n')
st.subheader("Publications")
st.write("---")
for project, link in PUBLICATIONS.items():
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
