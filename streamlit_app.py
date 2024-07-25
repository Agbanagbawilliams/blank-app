import streamlit as st

st.set_page_config(
    page_title="Multi App",
    page_icon="😁",
)

st.title("Main")
st.sidebar.success("Select a pages above.")

st.write("Welcome to my multi page")
st.write("This webpage was made using python and streamlit")
st.success("Check in the sidebar for more apps!")
