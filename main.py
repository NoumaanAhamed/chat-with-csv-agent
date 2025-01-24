import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize session state for conversation history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = ""

# Set up the Streamlit app
st.title("Chat with CSV")
st.write("Upload a CSV file and ask questions about the data.")

# Sidebar for API key input and history management
with st.sidebar:
    st.header("API Key Configuration")
    api_key = st.text_input("Enter your Google Generative AI API Key:", type="password")
    if not api_key:
        st.warning("Using default API key. For better performance, provide your own key.")
        api_key = os.getenv("GOOGLE_API_KEY")  # Fallback to default key from .env

    # Button to clear conversation history
    if st.button("Clear Conversation History"):
        st.session_state.conversation_history = ""
        st.success("Conversation history cleared!")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Initialize the Gemini model with the provided or default API key
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

    # Create the CSV agent
    agent_executor = create_csv_agent(model, uploaded_file, verbose=True, allow_dangerous_code=True)

    # Chat interface
    user_input = st.text_input("Ask a question about the CSV data:")

    if user_input:
        try:
            # Prepare the full input with conversation history
            full_input = f"Conversation History:\n{st.session_state.conversation_history}\n\nCurrent Question: {user_input}"

            # Get the response from the agent
            response = agent_executor.invoke(full_input)

            # Update the conversation history
            st.session_state.conversation_history += f"User: {user_input}\nAgent: {response}\n\n"

            # Display the response
            st.write("Response:")
            st.write(response['output'])
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Display conversation history
    if st.session_state.conversation_history:
        st.subheader("Conversation History")
        st.text(st.session_state.conversation_history)

else:
    st.write("Please upload a CSV file to get started.")