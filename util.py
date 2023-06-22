import streamlit as st
from langchain import LLMChain
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.memory import ConversationBufferMemory
import speech_recognition as sr

template = """I want you to act as a helpful and friendly chatbot that answers questions truthfully.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template)


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown("## How to use\n"
                    "1. Record by clicking on the microphone\n")
        API_KEY = st.sidebar.text_input("Enter your OPENAI API-KEY",
                                        placeholder="Paste your OpenAI API key here",
                                        type='password')
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "Voice based GPT allows user to speak with GPT and get response back."
        )
        st.markdown("---")
        st.markdown("Privacy")
        st.markdown(
            "Your conversation and voice will not saved at all."
        )
        st.markdown("This tool is a work in progress")

        if API_KEY:
            set_openai_api_key(API_KEY)







