import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "LLM Project"

groq_api_key = os.getenv("GROQ_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries."),
        ("user","question: {question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm = ChatGroq(model_name=llm,groq_api_key=groq_api_key)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    return answer

## Title of the app
st.title("Enchaned Q&A Chatbot with LLM")

llm = st.sidebar.selectbox("Select LLM Model",["gemma2-9b-it","llama3-8b-8192","deepseek-r1-distill-llama-70b"])
temperature = st.sidebar.slider("Temperature",0.0,1.0,0.5)
max_tokens = st.sidebar.slider("Max Tokens",50,200,100)

st.write("Go ahead and ask anything")
user_input = st.text_input("You: ")

if user_input:
    response = generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provie query")