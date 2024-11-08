import streamlit as st
import spacy

#Caching
@st.cache_data()
def load_model(model_name):
    nlp = spacy.load(model_name)
    return nlp


nlp = load_model("en_core_web_lg")

def extract_entities(ent_types,text):
    result = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            result.append((ent.text,ent.label_))
    return result

st.title("Lesson 02: Forms in Streamlit")

form1 = st.sidebar.form(key="Options")
form1.header("Params")
ent_types = \
form1.multiselect("Chooose params to extract",['PERSON','ORG','GPE'])

form1.form_submit_button("Submit")

text = st.text_area("Sample text....","James enjoys playing Basketball in Florida for the Salvation Army.")

hits = extract_entities(ent_types, text)
st.write(hits)