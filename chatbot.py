import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load environment variables from .env file
load_dotenv()

# Get Groq API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.set_page_config(page_title="History Chatbot", page_icon="🏛️")
st.title("🧠 History Chatbot")
st.write("Ask me simple history questions!")

if groq_api_key:
    # Initialize LLM with Groq
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama3-8b-8192",
        temperature=0.5
    )

    # Memory for conversation
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory)

    # User input
    user_input = st.text_input("Your question:")

    if user_input:
        with st.spinner("Thinking..."):
            response = conversation.run(user_input)
            st.markdown(f"**Answer:** {response}")
else:
    st.warning("Please set your GROQ_API_KEY in the .env file or Streamlit secrets.")
