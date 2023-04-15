import streamlit as st
import loaders as hc
import time

st.title("Publications")
st.write("---")
with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)

PUBLICATIONS = {

    "📖 Dose-Response Curve Fitting for Individual Herbicide and Individual Weed Combination with Gompertz Function -->The primary focus of this paper is to examine the analysis of dose-response to find the maximum efficacy for individual herbicides against individual weeds. Such studies have become a standard for weed science. The data was collected from different parts of Germany from 2000 to 2021 and is still collected from the field. The biggest challenge was creating the dataset and fitting the nonlinear data to create the Gompertz growth model. The most used growth models are the four pl logistic curve, five pl logistic curve, sigmoid function, and power-law function. In this project, results will be compared with the most used growth functions, and it will help us see how the Gompertz model is consistent in creating the best growth model.": "https://www.researchgate.net/publication/369884960_Dose-Response_Curve_Fitting_for_Individual_Herbicide_and_Individual_Weed_Combination_with_Gompertz_Function/stats",
    
    
    "📖  Unmanned Aerial Vehicle for Cleaning the High Rise Buildings --> (This paper represents a design of an "
    "ardupilot mega (APM) based remote-controlled unmanned aerial vehicle system for cleaning the high rise buildings "
    "windows. The design is developed with the remote-controlled system, which allows the workers to give security "
    "and maintenance of a surrounding area. )IEEE · Jan 15, 2019":
        "https://ieeexplore.ieee.org/document/8644476/references#references",


}

# --- Publications ---
st.write('\n')
st.subheader("📰Publications📰")
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
