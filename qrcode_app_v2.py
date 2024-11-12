import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from generate_qrcode_page import generate_qr_code

st.set_page_config (page_title=" QRCode App",
                    page_icon=":smile:")

options = ['Create QR Code', 'Decode QR Code', 'About Me']
page_selection =st.sidebar.selectbox("Menu", options)

if page_selection == 'Create QR Code':
    generate_qr_code()
elif page_selection == 'Decode QR Code':
    decode_qrcode_page()
elif page_selection == 'About Me':
    st.write("Z")
