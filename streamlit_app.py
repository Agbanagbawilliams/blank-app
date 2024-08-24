import streamlit as st
import random
import time

st.set_page_config(page_title="Chatbot", page_icon="💬")

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hi Human remember to follow me on scratch https://scratch.mit.edu/users/Williamsagb/",
            "Hello friend follow do not forget to follow me on scratch https://scratch.mit.edu/users/Williamsagb/",
            "Hi friend play my games that i created https://scratch.mit.edu/users/Williamsagb/",
            "Hi do not forget to like my games and project https://scratch.mit.edu/users/Williamsagb/",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Text here?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# ---- Sidebar Message ----
st.sidebar.text("Created by 💖 Williams")
