import streamlit as st

st.title("Streamlit Tutorial App")
st.write("This is my first-ish streamlit app")

st.header("Start of the Checkbox section")
button1 = st.button("Click me")

if button1:
    st.success("Clicked!!")

like = st.checkbox("Like")
button2 = st.button("Submit")
if button2:
    if like:
        st.success("Successful")
    else:
        st.warning("unlike")

st.header("Start of the Radio button section")


radio = st.radio("What's your favorite food?",("Pizza","Burgers","Fries","Mac Cheese"))

button3 = st.button("Submit food")
if button3:
    if radio == "Pizza":
        st.success("Italianoo Pizzaria")

    elif radio == "Burgers":
        st.success("Mr Mcmuffin")

    elif radio == "Fries":
        st.success("Yummy fries")
    
    elif radio == "Mac Cheese":
        st.success("Heartattack on a plate")


st.header("Start of the Select Box section")


radio = st.selectbox("What's your favorite Animal?",("Dogs","Cats","Parrot","Snakes"))

button4 = st.button("Submit animal")
if button4:
    if radio == "Dogs":
        st.success("Woof!!")

    elif radio == "Cats":
        st.success("Purr!!!")

    elif radio == "Parrot":
        st.success("Krrrrrr!!")
    
    elif radio == "Snakes":
        st.success("Slimmy pals!!")

st.header("Start of the Multiselect Box section")

radio = st.multiselect("Most prized possession",["Watch","Car","Chain","Bike"])

button5 = st.button("Submit possessions")
if button5:
    if "Watch" in radio:
        st.success("Nice")

    elif "Car" in radio:
        st.success("Understandable")

    elif "Chain" in radio:
        st.success("So old school")
    
    elif "Bike" in radio:
        st.success("Damn bro you doing thaat bad in life??")
