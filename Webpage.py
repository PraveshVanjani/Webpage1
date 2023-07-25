import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":globe_with_meridians:",layout="wide")

def load_lottieurl1 (url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

# - - - Load Assets - - -
lottie_coding = load_lottieurl1 ("https://lottie.host/7a693536-ed02-4830-891d-99cec597b012/1eCFJQoCYP.json")


# - - - Header Section - - -
with st.container ():
    st.subheader ("Hello, I am Pravesh Vanjani")
    st.title ("📜  Undegraduate Student from Lancaster University Management School")
    st.write ("Enthusiastic and driven individual working towards becoming a Certified Financial Analyst, I hold a BSc (Hons) in Accounting & Finance from Lancaster University Management School, a top-ranked institution in QS World University Rankings. My pursuit of excellence in the finance domain is complemented by my unwavering passion for coding and tech. Staying updated with the latest advancements and trends is a personal mission, enabling me to leverage technology to enhance financial analysis and decision-making processes.")
    st.write ("Beyond my academic achievements, my inquisitive nature and love for reading books have broadened my perspectives, fostering a holistic approach to problem-solving and critical thinking. Seeking a role where increased responsibility can be taken on, I am driven to utilize my analytical abilities and passion for technology to provide valuable insights that contribute to organizational success. I am excited about the prospect of contributing my diverse skill set to a company that values growth, innovation, and excellence")
    st.write ("[:desktop_computer: Click here to view my LinkedIn profile!](https://www.linkedin.com/in/pravesh-vanjani-a6b450163/)")


    st.write ("[👉  Click here to download my Curriculum Vitae!](https://1drv.ms/b/s!AvWO4qnLGLXYd5bwxlaDHaE76k4?e=REC5d8)")

# - - - Hobbies - - -
with st.container ():
    st.write ("- - -")
    left_column,right_column = st.columns (2)
with left_column:
    st.header ("📸  Photography")
    st.write ("##")
    st.write ("Discover my photography world on my captivating VSCO page where I showcase stunning visuals and immerse myself in the art of capturing moments. Click the link below to embark on a visual journey with me!")
    
    st.write ("[:camera:  Click here to view my photography page](https://vsco.co/praveshvanjani/gallery)")
    
    st.write ("[:camera:  Click here to view my Instagram photgraphy page](https://www.instagram.com/pv_photography3/)")

with right_column:
    st_lottie(lottie_coding, height= 400, key="coding")


# - - - Contact - - -
with st.container ():
    st.write ("- - -")
    st.header ("📥  Get In Touch With Me")
    st.write ("##")

    contact_form = """
<form action="https://formsubmit.co/p.vanjani@outlook.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Enter Your Name" required>
     <input type="email" name="email" placeholder="Enter Your Email" required>
     <textarea name="message" placeholder="Enter Your Message Here"></textarea>
     <button type="submit">Send</button>
</form>
"""


st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(st, file_name):
    css_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(st, "style/style.css")

    