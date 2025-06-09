import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="History Chatbot", page_icon="🏛️")
st.title("🧠 History Chatbot")
st.write("Ask me simple history questions!")

# Get API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

if groq_api_key:
    # Set up Groq LLM
    llm = ChatGroq(model_name="llama3-8b-8192", api_key=groq_api_key)

    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory)

    user_input = st.text_input("Your question:")

    if user_input:
        with st.spinner("Thinking..."):
            response = conversation.run(user_input)
            st.markdown(f"**Answer:** {response}")
else:
    st.error("GROQ_API_KEY not found. Please set it in .env file.")
