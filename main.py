import os 
import streamlit as st 
from dotenv import load_dotenv 
import google.generativeai as gen_ai

load_dotenv()

st.set_page_config(
    page_title="Chat With Gemini Pro !!",
    page_icon = "🖥️",
    layout="centered"
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


gen_ai.configure(api_key = GOOGLE_API_KEY)

model = gen_ai.GenerativeModel("gemini-1.5-pro")

def translate_role_for_streamlit(user_role):
    if user_role=="model":
        return "assistant"
    else:
        return user_role 
    

# initialize chat session if not present
# this code creates and empty history to be filled....
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    
# above code is important coz here is where the model is involved

    
st.title("🤖 Gemini Pro -  Chatbot")


# display chat history ( dont let previous queries go away )
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        

# input field for users message

user_prompt = st.chat_input("Ask Gemini Pro .. ")

if user_prompt:
    # add users message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    
    # Send users message to Gemini Pro and get response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    # st.session_state.chat_session -->> this is THE model
    # that is how we are getting responses
    
        
    # display geminis response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
        

#   EXPLAINS HOW ARE WE GETTING STRUCTURE

# Function	Purpose
# st.chat_input("Ask something...")	Creates a chat input box at the bottom.
# st.chat_message("user")	Displays a chat bubble for the user.
# st.chat_message("assistant")	Displays a chat bubble for AI responses.

    
        