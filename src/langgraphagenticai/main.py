import streamlit as st
import json
from src.langgraphagenticai.UI.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.Graph.graph_builder import GraphBuilder
from src.langgraphagenticai.UI.streamlitui.display_result import DisplayResultStreamlit

# MAIN Function START
def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
   
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui() # Loading it from streamlit ui  


    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else:
        user_message = st.chat_input("Enter your message:")

    #  First all this will be visible over here / ui is loaded 
    #  Then we will say hey the person is giving any type of input or not 
    #  if giving input then we will load the llm models by using the key specfied in that particular field 
    #  load_streamlit_ui() has all the information because here we have something called user controls 


#  Go to LLM and setup LLM 
    if user_message:
            try:
                # Configure LLM
                obj_llm_config = GroqLLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()
                
                if not model:
                    st.error("Error: LLM model could not be initialized.")
                    return  # Exit here; the code below won't run

                # Initialize and set up the graph based on use case
                usecase = user_input.get('selected_usecase')
                if not usecase:
                    st.error("Error: No use case selected.")
                    return  # Exit here; the code below won't run
                
                #  if usecase is missing, the error is shown, and st.success(...) and subsequent code are never reached.
                #  This is the purpose of the bare return.
                
#  Go to graph now write graph_builder file 
                ### Graph Builder
                graph_builder=GraphBuilder(model)
                try:
                    graph = graph_builder.setup_graph(usecase)
                    DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
                except Exception as e:
                    st.error(f"Error: Graph setup failed - {e}")
                    return    # Exit here; the code below won't run
                

            except Exception as e:
                 raise ValueError(f"Error Occurred with Exception : {e}")