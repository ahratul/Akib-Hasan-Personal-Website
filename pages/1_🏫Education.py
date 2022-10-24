import streamlit as st
import loaders as hc
import time

st.title("Education")

st.write('\n')
st.subheader("🏫Education History🏫")
st.write("---")

with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)

# --- Education  2
st.write('\n')
st.write("🔜 👨‍🎓", "** Master’s in communication system and Networking | Technische Hochschule Köln **")
st.write("📍 Cologne, North Rhine-Westphalia ,Germany 🇩🇪")
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

# --- Education 1
st.write("👨‍🎓",
         "** Bachelor of Science in Electronic and Electrical Engineering | American International University-Bangladesh**")
st.write("📍 Dhaka, Bangladesh 🇧🇩")
st.write("05/2015 - 02/2020")
st.write(
    """
- ► Digital Design with System Verilog, VHDL and FPGAs.
- ► Microwave Engineering.
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
