#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Results page
*
* @author: Alina Ribeiro Pinto
* @version: 27.03.2023
"""

# Imports
import streamlit as st
import base64
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import requests


def transalteText(text,option):
    sourceLan="en"
    payload = {
        "source_language": sourceLan,
        "target_language": option,
        "text": text
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "cabf61fc38msh6466c5b2fa9ba74p1875fcjsn64972fd03062",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    return data['data']['translatedText']


st.sidebar.header("© 2023")
st.sidebar.markdown("`👩‍💻 Power by Alina, Amine and Vera with Streamlit`")

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
    col1, col2, col3 = st.beta_columns(3)
    with col3:
        authenticator.logout('Logout', 'main')   # show logout button

    # Function to encode local image  
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
    add_bg_from_local('/app/depressionquiz/QuitzDepression/media/background/BackWhiteSheep.png')

    option = st.selectbox(
        'Choose your language',
        ('en', 'it', 'de','fr')
    )
    sourceLan="en"
    title=""
    message=""

    

    # Function to giving the final result 
    if 'points' in st.session_state:
        st.write("##### `You have scored: "+str(st.session_state["points"])+" points`")
        points=st.session_state["points"]
        point10=st.session_state["point10"]

        if point10>0:
            title="WARNING SUICIDAL RISK"
            message="Advice: immediate discussion required. Refer to PCP mental health specialist or emergency resource for further assessment and intervention as appropriate"
        else:
            if points <=8:
                title="### With this point depression is not likely"
                message="Advice: Continue support"

            elif points >=9 and points<=11 :
                title="### With this point Depression is possible"
                message=">**Advice: Support, re-screen in 2-4 weeks. Consider referral to primary care provider(PCP).t"
            
            elif points >=12 and points<=13 :
                title="With this points there is a fairly high possibility of depression"
                message=">**Advice: Monitor, support and offer education. Refer to PCP."
            
            elif points >=14:
                title="With this points there is a probable depression"
                message="Advice: Diagnostic assessment and treatment by PCP and/or specialist."

    else:
        title="Quiz not taken"
        message="Take the quiz and then come back to check the results please"

    # Security Contacts 
    st.markdown("----")
    st.markdown("""
    - 🇨🇭/🇩🇪 Föderation der Schweizer Psychologinnen und Psychologen
    - 🇨🇭/🇫🇷 Fédération Suisse des Psychologues
    - 🇨🇭/🇮🇹 Federazione Svizzera delle Psicologhe e degli Psicologi 


    Phone number: `+41 31 388 88 00`
    
    - Verband Tel `143` - Die Dargebotene Hand
    - Pro Juventute helpline for children and young people `147`

    **Open 24/7**
    """)
    
    url = "https://text-translator2.p.rapidapi.com/translate"


    if st.button("Translate"):
       
        translated_text=transalteText(title,option)
        st.markdown("### "+translated_text)

        translated_text=transalteText(message,option)
        st.markdown("> "+translated_text)
       
       
        warn="""
            >WARNING Please bear in mind that this Quiz  has been designed and created primarily for educational and informative purposes.
            It does not aim to provide one and was not designed to do so."""
        translated_text=transalteText(warn,option)
        st.markdown(translated_text)
       
        warn="""
            > Also, this questionnaire has a high sensitivity as a screening tool, it is not intended to be a substitute for professional clinical advice. The result is not a
        diagnosis, but indicative only."""
        translated_text=transalteText(warn,option)
        st.markdown(translated_text)
    else:
        title="### "+title       
        message="> "+message
        st.markdown(title)
        st.markdown(message)
            # Warning Message 
   
        st.markdown("""
            > **WARNING:** Please bear in mind that this Quiz  has been designed and created primarily for educational and informative purposes.
            >It does not aim to provide one and was not designed to do so.""")
        st.markdown("""  
            > Also, this questionnaire has a high sensitivity as a screening tool, it is not intended to be a substitute for professional clinical advice. The result is not a
        diagnosis, but indicative only.
        """)



                
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

