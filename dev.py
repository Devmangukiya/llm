import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq