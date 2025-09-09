import os
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="File Handling Project", page_icon="📂", layout="centered")

# --- Custom Anime Black Background ---
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpaperaccess.com/full/8349732.gif");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.8);
    color: white;
}

h1, h2, h3, h4, h5, h6, p, span, label {
    color: white !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🌌 File Handling Project - Anime Theme")

def list_files():
    path = Path('')
    files = [str(f) for f in path.rglob('*') if f.is_file()]
    return files

# --- Create File ---
def create_file():
    st.subheader("📄 Create a File")
    filename = st.text_input("Enter file name:")
    content = st.text_area("Enter content to write in file:")
    if st.button("Create File"):
        p = Path(filename)
        if not p.exists():
            with open(p, "w") as f:
                f.write(content)
            st.success(f"File `{filename}` created successfully ✅")
        else:
            st.warning(f"File `{filename}` already exists ⚠️")

# --- Read File ---
def read_file():
    st.subheader("📖 Read a File")
    files = list_files()
    if files:
        filename = st.selectbox("Select a file to read:", files)
        if st.button("Read File"):
            with open(filename, "r") as f:
                data = f.read()
            st.code(data, language="text")
            st.success("File read successfully ✅")
    else:
        st.info("No files found in this directory.")

# --- Update File ---
def update_file():
    st.subheader("✏️ Update a File")
    files = list_files()
    if files:
        filename = st.selectbox("Select a file to update:", files)
        choice = st.radio("Choose update option:", ["Rename", "Overwrite", "Append"])
        
        if choice == "Rename":
            newname = st.text_input("Enter new file name:")
            if st.button("Rename File"):
                Path(filename).rename(newname)
                st.success(f"File renamed to `{newname}` ✅")
        
        elif choice == "Overwrite":
            new_content = st.text_area("Enter new content:")
            if st.button("Overwrite File"):
                with open(filename, "w") as f:
                    f.write(new_content)
                st.success("File overwritten successfully ✅")
        
        elif choice == "Append":
            append_content = st.text_area("Enter content to append:")
            if st.button("Append File"):
                with open(filename, "a") as f:
                    f.write(append_content)
                st.success("Content appended successfully ✅")
    else:
        st.info("No files found in this directory.")

# --- Delete File ---
def delete_file():
    st.subheader("🗑️ Delete a File")
    files = list_files()
    if files:
        filename = st.selectbox("Select a file to delete:", files)
        if st.button("Delete File"):
            os.remove(filename)
            st.success(f"File `{filename}` deleted successfully ✅")
    else:
        st.info("No files found in this directory.")

# --- Menu ---
menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Choose an option", menu)

if choice == "Create":
    create_file()
elif choice == "Read":
    read_file()
elif choice == "Update":
    update_file()
elif choice == "Delete":
    delete_file()
