#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Share page, with QR code.
*
* @author: Alina Ribeiro Pinto
* @version: 27.03.2023
"""
import streamlit as st
import qrcode
from PIL import Image


# Sidebar 
st.sidebar.header("© 2023")
st.sidebar.markdown("`👩‍💻 Power by Alina, Amine and Vera with Streamlit`")

st.markdown("## Share this depression quiz")
st.markdown("##### A project developed in ZHAW")


# Fuction to set a qrcode for our website 
import streamlit as st

# URL must be changed in case of production, "qrcode" must be installed on the promt with the comand "pip install qrcode"
# img=qrcode.make('localhost:8501/Home')
# img.save("media/qr.png")
# st.image("media/qr.png")



# Footer 
st.write("""
<footer style='background-color: rgb(51,51,51); width:100%; right:0px; left:0px; bottom:0px; position:fixed'>
<div style='padding: 30px; display: block; color:white; width:100%'>
    <hr style='width:25%; height:3px; background-color:rgb(238,32,121); margin:2px;'>
    <p style='font-size:20px;'>Alina Ribeiro Pinto – Amine Aksu – Vera Gomez</p>
</div>

</footer>
""",unsafe_allow_html=True)