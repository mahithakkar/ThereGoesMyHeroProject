"""
This is a container class that creates all settings for the apps in one place. other files can import this class to
get configuration values.
"""
import os #for talking to the os- its env variables, file paths and simple os functions since the python app needs to talk to os.
from dotenv import load_dotenv #makes sure .env file gets attached to the OS's env so os functions can read from it.

load_dotenv() #this function that we just imported makes the program look for a file called .env. if it exists, then loads it into process env.


class Config:
   # Streamlit Configuration AS GLOBAL VARS- these are then used in app.py for configuration. defined according to streamlit documentation
    PAGE_TITLE = "🩸 TGMH Insights 🩸"
    PAGE_ICON = "🩸"
    LAYOUT = "wide"
 
   #from by running the load_dotenv() function, I already put the key in the env now the os.getenv gets the key from the env.
   #saves it in a global var so accessible from Config.GROQ_API_KEY
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile") #the versatile model is fallback if model not mentioned
  
  
