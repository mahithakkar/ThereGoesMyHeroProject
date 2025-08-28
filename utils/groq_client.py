"""Groq_client.py:  to see if api key works. Send a simple chat prompt and get a reply. And later ( send context for rag answers). 
1. Validating if api exists (show streamlit error if missing)
2. Initialize a groq SDK thats ready to use
Design here would be minimal since the job of thing is to ensure that api works.
"""
import streamlit as st #for showing errors (if API key fails)
from groq import Groq #importing groq sdk
from config import Config #so groq_client can read the api key from env- no need to hardcode 


class GroqClient: 
    #constructor for class so when you run GroqClient() it makes a fresh obj and run this constructor each time
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY #initializing keys from config - config initalizes from env
        self.model = Config.GROQ_MODEL
        """goal: groq()- establishes a direct connection with groq without us handling the low level http. however, setting
        self.client = None because if the key is invalid, then app would crash. therefore initializing a method that we would 
        if the api key is valid and running, and then set up the client"""
        self.client = None
        self.initialize_client()
        
    def initialize_client(self):
        #so if .env is missing the api key then it would be empty 
        if not self.api_key: 
            st.error("KEY NOT FOUND, PLS ADD YOUR API KEY TO YOUR ENV!")
            return #so it fails without trying to reconnect
            
        
        #now if it reaches this point, then api key definately exists, but we have to check if its valid
        try:
            obj1 = Groq(api_key = self.api_key)
            self.client = obj1
            #established connection at this point
            #now testing with a simple request 
            #defining a new method test_connection defined below 
            self.test_connection()
            
        except Exception as e:
            st.error(f"Error initializing Groq Client : {e}")
        

    def test_connection(self) -> bool:
        """I will try sending a tiny message to see if teh connection to 
        groq client is connected and is actually valid"""
        try: 
            '''a way to send message- self.client 
            is the groq client object, .chat is to access the chat endpoint,
            .completions 
            '''
            #client is the remote control, then u press the chat button, completions
            #to tell it to generate some text and create method as the send button.
            response = self.client.chat.completions.create(
                messages=[{ "role": "user", "content": "Hello groq! My name is mahi and I am checking if youre working!",}],
                model=self.model,
            )
            return True
        except Exception as e:
            st.error(f"Groq API Connecti on failed {e}")
            
    """if the code reaches this point that means its valid and it
    works, however now this block of code is only accessible in this file itself
    here i will make it easy for the rest of the app to ask is groq ready and usable
    technically- i could use the test_connection method, but due to perforamnce trade offs 
    like seding a request each time would cost tokens, i would rather just do a local 
    check to see if groq is available right now.
    """
    def is_available(self) -> bool:
        return self.client is not None
    
    
    """now defining a method that an app can actually call to get a reply from groq"""
    def simple_message(self, prompt: str, max_tokens :int = 200, temperature: float  = 0.2) -> str:
        if not self.is_available():
            return "Groq client not available check your API key"
        try:
            resp = self.client.chat.completions.create(
                model = self.model ,
                messages= [{"role": "user", "content" : prompt}],
                max_tokens = max_tokens,
                temperature = temperature,
            )
            return resp.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {e}"
        
    

