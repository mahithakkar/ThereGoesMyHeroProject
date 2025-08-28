import streamlit as st
from utils.groq_client import GroqClient 

#setting up streamlit configuration 
st.set_page_config(
    page_title = "🩸 TGMH Insights 🩸",
    page_icon = "🩸",
    layout = "wide",
)

st.title("🤖 Chat with Mahi 🤖")

client = GroqClient() #making a groq client object- from groq client class and establishes the connection 

#groq client already handles the errors but for better UX here I am adding a fail check method 
if not client.is_available():
    st.stop()


#simple message exchange 
#user_prompt = st.text_input("Type your message: ")
#if user_prompt:
#    with st.spinner("Mahi is thinking!"):
#        reply = client.simple_message(user_prompt)
#   st.markdown(f"Mahi says: {reply}")
#checked and it works so proceeding to make a ui 


#next logical state is focusing on UI and chat message
#first step is to keep a simple chat history is session state 

#session state is a way to share vars for reruns from api reference streamlit docs 
#initally this would be empty 
if "messages" not in st.session_state:
    st.session_state.messages = [] #made a list of dictionary with each item as role: user/assistant, content: str 
    
#rendering existing messages
#so for each message "m" in the list: 
#key and value pair for each item
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

#input text on bottom 
prompt = st.chat_input("Ask any TGMH question!")

#on submit, append user then call groq then append assistant 
if prompt:
    st.session_state.messages.append({"role" : "user" , "content" : prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        with st.spinner("Mahi is thinking: "):
            reply = client.simple_message(prompt)
        st.markdown(reply)
    
    #adding it back to session state for history 
    st.session_state.messages.append({"role" : "assistant" , "content" : reply})
        
    
    