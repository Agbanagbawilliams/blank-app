import streamlit as st
import random
import time

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #F0DEAB;">
  <a class="navbar-brand" target="_blank">Beach</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/">About me <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/Project" target="_blank">Project</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://newwebpage-nr9d95duhpvvbdx6mqjedc.streamlit.app/Project" target="_blank">Chatbot</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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
