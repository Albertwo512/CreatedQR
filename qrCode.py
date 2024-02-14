import qrcode
import streamlit as st

filename = "qrcodes/qrcode.png"

def generate_qrcode(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img= qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

st.set_page_config(page_title="Generador de QR", layout="centered")
st.image("qrcodes/Generar-código-QR-Thumbnail.jpg", use_column_width=True)
st.title("Generador de QR")
url = st.text_input("Ingresa URL...")

if st.button("Generar QR"):
    generate_qrcode(url, filename)
    st.image(filename,use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    
    download = st.download_button(label="Download QR", data=image_data,file_name="qr_generado.png")
