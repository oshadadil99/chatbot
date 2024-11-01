import streamlit as st
import streamlit_chat as message
from dotenv import load_dotenv
import os

from langchain_community.llms import HuggingFaceHub
#from langchain.chat_models import ChatModel
from langchain_community.chat_models import ChatModel

from langchain.schemas import (
      SystemMessage,
      HumanMessage,
      AIMessage
)

def init():
    load_dotenv()

    if os.getenv("HUGGINGFACE_API_KEY") is None or os.getenv("HUGGINGFACE_API_KEY") == "":
        print("HUGGINGFACE_API_KEY is not set")
        exit(1)
    else:
        print("HUGGINGFACE_API_KEY is set")


    st.set_page_config(
            page_title= "My chat bot",
            page_icon="</>"
    )


def main():
    init()
   
    st.header("Ask from Prince Vlad")
    with st.sidebar:
        user_input = st.text_input("Your Message: ",key="user_input")

if __name__ == "__main__":
    main()