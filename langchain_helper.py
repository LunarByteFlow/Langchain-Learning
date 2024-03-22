from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
# from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


def generate_pet_name(animal_type, animal_color):
    llm_huggingface = HuggingFaceEndpoint(repo_id="google/gemma-7b",temperature = 1, max_length=10)
    pet_prompt_template = PromptTemplate(input_variables = ['animal_type','animal_color'] ,template = "I have a {animal_type} of color {animal_color}, Give me 5 unique 10 letter Names for my pet" )

    name_chain = LLMChain(llm = llm_huggingface, prompt = pet_prompt_template, output_key="pet_name")
    response = name_chain.invoke({"animal_type": animal_type, "animal_color": animal_color})
    return response
if __name__ == "__main__":
    print(generate_pet_name("cow","yellow") )
    