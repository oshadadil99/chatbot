import streamlit as st
import streamlit_chat as message
from dotenv import load_dotenv
import os

from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain  
from langchain.schema import (
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
            page_icon="🤖"
    )


def main():
    init()

    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]

    st.header("Ask from Prince Vlad")

    with st.sidebar:
        user_input = st.text_input("Your Message: ",key="user_input")

    
    for i, msg in enumerate(st.session_state.messages):
        if isinstance(msg, HumanMessage):
            message.message(msg.content, is_user=True, key=f"user_{i}")
        elif isinstance(msg, AIMessage):
            message.message("Prince Vlad: " + msg.content, is_user=False, key=f"ai_{i}")


    if user_input:

        st.session_state.messages.append(HumanMessage(user_input))
        hf_api_token = os.getenv("HUGGINGFACE_API_KEY")
        model_name = "mistralai/Mistral-7B-Instruct-v0.3"
        
        llm = HuggingFaceHub(
            repo_id=model_name,
            huggingfacehub_api_token=hf_api_token
        )

        prompt = PromptTemplate(
            input_variables=["user_input"],
            template=" {user_input}\n"
        )

        chat_chain = LLMChain(
            llm=llm,
            prompt=prompt
        )
    
        with st.spinner("Thinking...."):
            response = chat_chain.run(user_input=user_input)
        st.session_state.messages.append(AIMessage(response))

        message.message(user_input, is_user=True)
        message.message("Prince Vlad: " + response, is_user=False)

if __name__ == "__main__":
    main()