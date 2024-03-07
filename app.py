import streamlit as st
from utils import  generate_response


# Page Config
st.set_page_config("Billionaire 2023", page_icon="💸")


# Submit handler
def handle_submit(query):
    """
    Submit handler:
    """

    # Handle the response
    with st.spinner('Thinking...'):
        response = generate_response(query)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
        #write_message('assistant', response)
      

# Write to UI
def write_message(role, content):
    """
    This is a helper function that writes a message to the UI
    """
    with st.chat_message(role):
        st.markdown(content)

# Session state initialization
if "messages" not in st.session_state: # or st.sidebar.button("Clear message history"):
            st.session_state["messages"] = [{"role": "assistant", "content": "What's up?"}]   

# Write previous messages to UI from session
for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])   

# Handle any user input
prompt = st.chat_input("What's up?")
#if prompt := st.chat_input("What's up?"):
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    #st.chat_message("user").write(prompt)
    # Display user message in chat message container
    write_message('user', prompt)
    
    # Generate a response
    with st.chat_message("assistant"):
        handle_submit(prompt)
    

   
