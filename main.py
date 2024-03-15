from langchain_community.llms import HuggingFaceEndpoint
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
# from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
from langchain.chains import SequentialChain
load_dotenv()
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm_huggingface = HuggingFaceEndpoint(repo_id="google/gemma-7b",temperature = 0.7, max_length=64)
# prompt template 
first_prompt_template = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about celebrity {name}"
    
)
first_chain = LLMChain(llm = llm_huggingface,prompt = first_prompt_template, verbose = True, output_key = 'person')

second_prompt_template = PromptTemplate(
    input_variables = ['person'],
    template = "When was {person} born"
)

second_chain = LLMChain(llm = llm_huggingface,prompt = second_prompt_template, verbose = True,output_key='dob')

# parent_chain = SimpleSequentialChain(chains=[first_chain,second_chain],verbose = True)
parent_chain = SequentialChain(
    chains=[first_chain,second_chain],input_variables = ['name'], output_variables = ['person','dob'],verbose = True
    )


st.title("Welcome to Our Hugging Face Simple Chatbot")
input_text = st.text_input("Enter the topic You want to Search...")
if input_text:
    st.write(parent_chain({'name':input_text}))
