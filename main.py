import streamlit as st
import streamlit_chat as message
from dotenv import load_dotenv

def main():
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

    st.header("Ask from Prince Vlad")

    message("Hello how are you")
    message("I'm good", is_user=True)

    with st.sidebar:
        user_input = st.text_input("Your Message: ",key="user_input")

if __name__ == "__main__":
    main()