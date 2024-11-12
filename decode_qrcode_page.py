import streamlit as st
import numpy as np
import cv2

def decode_qrcode_page():
    st.title("Decoding QR Codes")

    qrcode = st.file_uploader("Upload your QR Code",
                     type=['jpg','jpeg', 'png'])

    if qrcode:
        file_bytes =np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image)

        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QR Code contains {decoded_info}")

