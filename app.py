import streamlit as st
import openai
from streamlit_chat import message
from langchain.memory import ConversationBufferMemory
from langchain import LLMChain
from langchain.llms import OpenAI
from langchain import PromptTemplate
import speech_recognition as sr
from util import *

#Initialization
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory(
        memory_key="chat_history", input_key="human_input"
    )
recognizer = sr.Recognizer()

#Langchain
@st.cache_data
def get_response(text):

    llm = LLMChain(
        llm = OpenAI(openai_api_key=st.session_state['OPENAI_API_KEY']),
        prompt = prompt,
        memory = st.session_state['memory'])
   
    response = llm.predict(human_input=text)

    return response

# UI 
st.set_page_config(page_title="Voiced Based GPT", layout='wide')
sidebar()
st.header("VOICED BASED CHATGPT")
st.markdown("""Welcome! Click the button to record your message and get response from GPT
""")

container = st.container()
response_container = st.container()
with container:
    with st.form(key='my_form', clear_on_submit=True):
        submit_button = st.form_submit_button(label='Record Message')

    if submit_button:
        API_KEY = st.session_state['OPENAI_API_KEY']
        if not API_KEY:
            st.error("Invalid [OpenAI API key](https://beta.openai.com/account/api-keys).")
        else:
            with sr.Microphone() as source:
                audio = recognizer.record(source, duration=5)
                text = recognizer.recognize_google(audio)
                response = get_response(text)
                st.session_state['past'].append(text)
                st.session_state['generated'].append(response)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
