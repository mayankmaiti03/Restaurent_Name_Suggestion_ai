from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os

os.environ['OPENAI_API_KEY']=openapi_key
llm=OpenAI(temperature=0.7)

def generate_restaurent_name_and_items(cuisine):
    # Chain 1 : Generate Name of the restaurent 
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want To open a restaurent for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain=LLMChain(llm=llm,prompt=prompt_template_name,output_key="restaurent_name")
    #Chain 2: Menu Items
    prompt_template_items=PromptTemplate(
        input_variables=['restaurent_name'],
        template="""Suggest some menu items for {restaurent_name}.Return it as a comma seperated string"""
    )
    food_items_chain=LLMChain(llm=llm,prompt=prompt_template_items,output_key="menu_items")
    chain=SequentialChain(
        chains=[name_chain,food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurent_name',"menu_items"]
    )
    
    response=chain({'cuisine':cuisine})
    return response

if __name__=="__main__":
    print(generate_restaurent_name_and_items("Italian"))