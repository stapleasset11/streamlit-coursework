import streamlit as st

st.title("Lesson 01: Streamlit Layouts")
def clean_text(text):
    text = text.replace("`", "").replace("-\n", "").replace("\n", " ").strip()
    return text

st.header("Side bar")
st.sidebar.image("logos/rick-and-morty-6344804_1280.jpg",width=100)

st.sidebar.header("Options")

text = st.sidebar.text_area("Paste your text here...")

clearButton = st.sidebar.button("Clear Text")

if clearButton:
    col1,col2 = st.columns(2)
    col1_expander = \
    col1.expander("Expand Original")

    col2_expander = \
    col2.expander("Expand Cleaned")

    with col1_expander:
        col1_expander.header("Original Text")
        col1_expander.write(text)

    with col2_expander:
        col2_expander.header("Cleaned Text")
        clean = clean_text(text)
        col2_expander.success(clean)