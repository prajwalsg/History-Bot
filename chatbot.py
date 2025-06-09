import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key and base from env
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")

# Streamlit UI
st.set_page_config(page_title="History Chatbot", page_icon="🏛️")
st.title("🧠 History Chatbot")
st.write("Ask me simple history questions!")

if openai_api_key and openai_api_base:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["OPENAI_API_BASE"] = openai_api_base

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",
        temperature=0.5
    )

    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory)

    user_input = st.text_input("Your question:")

    if user_input:
        with st.spinner("Thinking..."):
            response = conversation.run(user_input)
            st.markdown(f"**Answer:** {response}")
else:
    st.warning("API Key or Base URL not found in .env file.")