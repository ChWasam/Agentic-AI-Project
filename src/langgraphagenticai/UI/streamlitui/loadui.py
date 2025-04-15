
# Our main aim is to display that entire ui
# In ui i have some sidebar and in the sidebar i have some information.
# 1st we load all the configration '
#  Loading the entire streamlit ui 



import streamlit as st
import os
from datetime import date

#  The message that we are going to write im the ui page is either human mesage or ai message 
from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphagenticai.UI.uiconfigfile import Config

# src.langgraphagenticai.ui.uiconfigfile  => This is actually the modular structure 


# This ui part we can hardcode over here or it is better to write it in the form of class
class LoadStreamlitUI:
    def __init__(self):
        self.config =  Config() # config
        # Here we need some configuration details. Whenever we are creating frontend there should be some kind of configuration inside the fields (like in ui slect llm or select model )
        # In ui there is some content inside the fields like dropdown has some content in ui. That content inside the field should be comming from the  configuration file
        # now when you load the ui the first thing loaded over here is the config  

        self.user_controls = {}


    #  this is just about what are the keys that we are saving in the session 
    # initialize_session(self) is to make sure to create all those keys so that the session is being mentained 
    #  Once we initialize the session all the keys will be specifically available so that you can maintain the state 
    # 
    def initialize_session(self):
        return {
        #  All These keys are basially used in the later stages when we build more applications rn it is not required so don't worry about it 
        # as we will build more usecases we will talk specificly where we are using this 
    
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }
    #  As soon as we load it what are the things that are visible over here 
    #  We created another function over here 
    # As soon as the ui gets loaded everything should get loaded 
    

    #  Over here we have set our basic page configuration 



    def load_streamlit_ui(self):
        #  Basic configurations with respect to the streamlit 
        page_title = self.config.get_page_title() or "Default Title"
        st.set_page_config(page_title= "🤖 " + page_title, layout="wide")
        st.header("🤖 " + page_title)
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
 
            # LLM selection
            #  Here i am creating a field called  selected_llm 
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            #  I am wriring this inside my user_controls over here and user_controls is a dictionary over here 
            # So that we can read this anywhere we want 

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # We are saving that is a  session state that whatever the session is going on 
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
            

            #  Here we are just initializing the entire session 
            # Initialization session is noting but to create all those keys in initialize_session(self) so that the session is mentained  

            #  You are initializing session 
            #  Which all  sessions you are initializing are given below 
            #  "current_step": "requirements",
            # "requirements": "",
            # "user_stories": "",
            # "po_feedback": "",
            # "generated_code": "",
            # "review_feedback": "",
            # "decision": None
            #  For different usecases we will use these 

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
                #  Till this point left side of the ui will be loaded 
                # the flow will be from left to right 
                # First left then right side will  be loaded 
                #  now what about the right side window 

            #  now once i am defining the specific session state where should we save this session state 
            # that is inside this particular function initialize_session()
            #  this is just about what are the keys that we are saving in the session 
        return self.user_controls
    

    # Now go to main 