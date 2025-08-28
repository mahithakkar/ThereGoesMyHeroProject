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
user_prompt = st.text_input("Type your message: ")
if user_prompt:
    with st.spinner("Mahi is thinking!"):
        reply = client.simple_message(user_prompt)
    st.markdown(f"Mahi says: {reply}")