#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Depression quiz - Home Page
*
* @author: Alina Ribeiro Pinto
* @version: 27.03.2023
"""
# Imports
import streamlit as st
import webbrowser
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(
        page_title="Home",
        page_icon="🏠",
    )
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
    st.sidebar(
        authenticator.logout('Logout', 'main')   # show logout button
    )

    # Title and subtitle 
    st.write("# Depression quiz")


    st.markdown("""
        With this study we would like to find out how many women suffer from postnatal depression in Switzerland. 
        
        In the following quiz you will be provided with 10 questions: please, tell the truth. Depression is not a joke.
        Stay Safe.
        
    """)

    # button for starting the Quiz 
    if st.button("📝 Go to quiz"):
        webbrowser.open_new_tab('https://ribeiali-depressionquiz-quitzdepression1-home-yfd81a.streamlit.app/Quiz')

    #st.image("./media/images/depression1.png")

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


# Function for Title, Page Icon and Sidebar
