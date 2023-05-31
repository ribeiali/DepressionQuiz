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

st.sidebar.header("© 2023")
st.sidebar.markdown("`👩‍💻 Power by Alina, Amine and Vera with Streamlit`")

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
add_bg_from_local('media/background/BackWhiteSheep.png')


# Function to giving the final result 
if 'points' in st.session_state:
    st.write("##### `You have scored: "+str(st.session_state["points"])+" points`")
    points=st.session_state["points"]
    point10=st.session_state["point10"]

    if point10>0:
        st.markdown("### WARNING SUICIDAL RISK")
        st.markdown(">**Advice: immediate discussion required. Refer to PCP mental health specialist or emergency resource for further assessment and intervention as appropriate.**")
    else:
        if points <=8:
            st.markdown("### With this point depression is not likely")
            st.markdown(">**Advice: Continue support**")
        elif points >=9 and points<=11 :
            st.markdown("### With this point Depression is possible")
            st.markdown(">**Advice: Support, re-screen in 2-4 weeks. Consider referral to primary care provider(PCP).t**")
        
        elif points >=12 and points<=13 :
            st.markdown("### With this points there is a fairly high possibility of depression")
            st.markdown(">**Advice: Monitor, support and offer education. Refer to PCP.**")
        
        elif points >=14:
            st.markdown("### With this points there is a probable depression ")
            st.markdown(">**Advice: Diagnostic assessment and treatment by PCP and/or specialist.**")

else:
    st.markdown("**Take the quiz and then come back to check the results please**")

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
