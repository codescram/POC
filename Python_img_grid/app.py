import streamlit as st;

import glob

with st.container(horizontal_alignment="center"):
    st.image("images/photographicsplash.png", width=200)

st.html('<h1 style="font-weight:normal; text-align:center; text-transform:uppercase;">Raj Photography Samples</h1>')

def load_images():
    image_files = glob.glob("images/*/*.jpg")
    manuscript=[]
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscript:
            manuscript.append(parts[1])

    return image_files, manuscript

image_files, manuscript = load_images()


view_manuscript = st.multiselect("Select Category(s)", manuscript)
n = st.number_input("Change Column Count", 1, 5, 3)


view_images =[]
for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscript):
        view_images.append(image_file)

groups =[]
for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

col = st.columns(n)
for group in groups:
    for i, image_file in enumerate(group):
        col[i].image(image_file)