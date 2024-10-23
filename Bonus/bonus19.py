import streamlit as sl
from PIL import Image

# Application title
sl.subheader("Color to Grayscale Converter")

with sl.expander("Start Camera"):
 # Start the camera
    camera_image = sl.camera_input("Take a photo")

# File upload section
uploaded_image = sl.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])


if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to gray
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    sl.image(gray_img, caption ="Grayscale Image")

elif uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert('L')
    sl.image(gray_img, caption="Grayscale Image")
