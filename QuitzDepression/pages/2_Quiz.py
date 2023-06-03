"""
* Depression quiz - quiz
*
* @author: Amine Aksu, Alina Ribeiro Pinto
* @version: 26.03.2023
"""

import streamlit as st
from PIL import Image
import base64
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# -------- user login --------
with open('/app/depressionquiz/QuitzDepression/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

fullname, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status == True:   # login successful
    col1, col2, col3 = st.columns(3)
    with col3:
        authenticator.logout('Logout', 'main')   # show logout button

    #Function to encode local image 

    img = Image.open("/app/depressionquiz/QuitzDepression/media/images/depression1.png")
    
    width, height = img.size


    new_width = int(width * 1)
    new_height = int(height * 1)

    resized_img = img.resize((new_width, new_height))

    #Sidebar Function
    st.image(resized_img, caption="Crying Woman", use_column_width=True)
    st.sidebar.header("© 2023")
    st.sidebar.markdown("`👩‍💻 Power by Alina, Amine and Vera with Streamlit`")
    
    def get_base64(bin_file):
        
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Function to display image ad background
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        header{{        
            opacity: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('/app/depressionquiz/QuitzDepression/media/background/BackEgg.png')

    # Define the questions and answer options using a dictionary
    questions = {
        "I have been able to laugh and see the funny side of things": {
            "As much as I always could": 0,
            "Not quite so much now": 1,
            "Definitely not so much now": 2,
            "Not at all": 3
        },

        "I have looked forward with enjoyment to things": {
            "As much as I ever did": 0,
            "Rather less than I used to": 1,
            "Definitely less than I used to": 2,
            "Hardly at all": 3
        },

        "I have blamed myself unnecessarily when things went wrong": {
            "Yes, most of the time": 3,
            "Yes, some of the time": 2,
            "Not very often": 1,
            "No, never": 0
        },
        "I have been anxious or worried for no good reason": {
            "No, not at all": 0,
            "Hardly ever": 1,
            "Yes, sometimes": 2,
            "Yes, very often": 3
        },
        "I have felt scared or panicky for no very good reason": {
            "Yes, quite a lot": 3,
            "Yes, sometimes": 2,
            "No, not much": 1,
            "No, not at all": 0
        },
        "Things have been getting on top of me": {
            "Yes, most of the time I haven't been able to cope at all.": 3,
            "Yes, sometimes I haven't been coping as well as usual.": 2,
            "No, most of the time I have coped quite well.": 1,
            "No, I have been coping as well as ever.": 0
        },
        "I have been so unhappy that I have had difficulty sleeping": {
            "Yes, most of the time": 3,
            "Yes, sometimes": 2,
            "Not very often": 1,
            "No, not at all": 0
        },
        "I have felt sad or miserable": {
            "Yes, most of the time": 3,
            "Yes, quite often": 2,
            "Not very often": 1,
            "No, not at all": 0
        },
        "I have been so unhappy that I have been crying": {
            "Yes, most of the time": 3,
            "Yes, quite often": 2,
            "Only occasionally": 1,
            "No, never": 0
        },
    }


    st.markdown("## With this study we would like to find out how many women suffer from postnatal depression in Switzerland. ")
    st.markdown("### Please select the answer that comes closest to how you have felt in the past 7 days:")
    st.write("<br>",unsafe_allow_html=True)

    totalScore=0
    counter=0
    for question, answers in questions.items():
        selected_answer = st.radio(question, list(answers.keys()))
        point = answers[selected_answer]
        totalScore += point

    question10 = "The thought of harming myself has occurred to me "
    answer10 = {
        "Yes, quite often ": 3,
        "Sometimes": 2,
        "Hardly ever ": 1,
        "Never ": 0
    }
    selected_answer = st.radio(question10, list(answer10.keys()))

    # Get the points for the selected answer
    point10 = answer10[selected_answer]

    # Display the final score

    if st.button('See results'):
        st.markdown("![Gif Therapy is medicine](../media/images/3.gif)")

        st.session_state['points']=totalScore+point10
        st.session_state['point10']=point10
        st.write("✅ Go to the results page to see the result")

    # Footer
    st.write("""
    <footer style='background-color: rgb(51,51,51); width:100%; right:0px; left:0px; bottom:0px; position:fixed'>
    <div style='padding: 30px; display: block; color:white; width:100%'>
        <p style='font-size:20px;'>Alina Ribeiro Pinto – Amine Aksu – Vera Gomez</p>
        <hr style='width:25%; height:3px; background-color:rgb(238,32,121); margin:2px;'>

    </div>

    </footer>
    """,unsafe_allow_html=True)

elif authentication_status == False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status == None:
    st.warning('Please enter your username and password')
    st.stop()
else:
    st.warning("unknow error")