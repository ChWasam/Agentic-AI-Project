import streamlit as st
import os
from datetime import date

#  The message that we are going to write im the ui page is either human mesage or ai message 
from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config

# src.langgraphagenticai.ui.uiconfigfile  => This is actually the modular structure 


# This ui part we can hardcode over here or it is better to write it in the form of class
class LoadStreamlitUI:
    def __init__(self):
        self.config =  Config() # config
        # Here we need some configuration details. Whenever we are creating frontend there should be some kind of configuration inside the fields (like in ui slect llm or select model )
        # In ui there is some content inside the fields like dropdown has some content in ui. That content inside the field should be comming from the  configuration file
        # now when you load the ui the first thing loaded over here is the config  


        #  As soon as we load it what are the things that are visible over here 
        self.user_controls = {}

    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }
  


    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
                   
            
            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] =="Chatbot with Tool":
                # API key input
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            
            
        
        return self.user_controls()