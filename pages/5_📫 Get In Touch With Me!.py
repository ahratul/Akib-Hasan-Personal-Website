import streamlit as st
import loaders as hc
import time

st.header(":mailbox: Get In Touch With Me!")
st.write("---")
with hc.HyLoader('LOADING', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
    time.sleep(2)

contact_form = """
<form action="https://formsubmit.co/ahratul740@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
import streamlit as st
import base64
import requests

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)


url = "https://raw.githubusercontent.com/ahratul/ahratul/output/github-contribution-grid-snake.svg"
r = requests.get(url) # Get the webpage
svg = r.content.decode() # Decoded response content with the svg string

render_svg(svg)
# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style1.css")


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