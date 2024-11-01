import streamlit as st
import streamlit_chat as message
from dotenv import load_dotenv
import os

from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  # Use LLMChain for chaining prompts and models

def init():
    load_dotenv()

    if os.getenv("HUGGINGFACE_API_KEY") is None or os.getenv("HUGGINGFACE_API_KEY") == "":
        print("HUGGINGFACE_API_KEY is not set")
        exit(1)
    else:
        print("HUGGINGFACE_API_KEY is set")


    st.set_page_config(
            page_title= "My chat bot",
            page_icon="🤖"
    )


def main():
    init()

    st.header("Ask from Prince Vlad")
    
    with st.sidebar:
        user_input = st.text_input("Your Message: ",key="user_input")

    if user_input:
        message(user_input, is_user=True)

if __name__ == "__main__":
    main()