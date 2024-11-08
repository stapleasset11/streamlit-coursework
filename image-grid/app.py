import streamlit as st
import glob
import os

def load_images():
    image_files = glob.glob(os.path.join(os.getcwd(), "images/*.jpg"))
    manuscripts = []

    st.write(len(image_files))
    for image_file in image_files:
        image_file = image_file.replace("\\","/")
        parts = image_file.split("/")
        if parts[6] not in manuscripts:
            manuscripts.append(parts[6])
    manuscripts.sort()
    # st.write(manuscripts)
        
    return image_files, manuscripts
    

st.title("Data Image Grid Display")
image_files,manuscripts = load_images()
view_manuscripts = st.multiselect("Select picture",manuscripts)
n = st.number_input("Select grid width",1,5,3)

view_images = []
for image_file in image_files:
    if any (manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)

groups = [view_images[i:i+n] for i in range(0,len(view_images),n)]
cols = st.columns(n)
# for group in groups:
#     cols[n]
    
for group in groups:
    
    for i, image_file in enumerate(group):
        if i < n:  
            cols[i].image(image_file, use_container_width=True)