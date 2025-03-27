# i will read uiconfigfile.ini

from configparser import ConfigParser

# configparser is a class that will help you to parse the entire text file   
class Config:
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        #  You can use the path from os.path.join search google 
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    # self.config["DEFAULT"] It has basically the excess of all the fields that is defined over here 
    # DEFAULT  is basically the root name for all the information that is present inside this 
    #  split(", ") means it will split by comma, if there is no comma it will not split over here
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")