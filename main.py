import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = ""

st.title("Chat with CSV")
st.write("Upload a CSV file and ask questions about the data.")

csv_file_path = "data.csv"  # Path to your CSV file on the server
preloaded_df = pd.read_csv(csv_file_path)

st.write("Don't have a CSV file? Download the sample ecommerce CSV below, modify it if needed, and upload it back to the app.")
csv_file = preloaded_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sample CSV",
    data=csv_file,
    file_name="sample_data.csv",
    mime="text/csv",
)

st.write("Here are some questions you can ask:")
st.write("1. How many products are there in the dataset?")
st.write("2. What is the price of the hat?")
st.write("3. Give me a list of all the products?")
st.write("4. What was my previous question?")

with st.sidebar:
    st.header("API Key Configuration")

    model_choice = st.radio("Select a model to use:", ("Google Generative AI", "OpenAI"))

    if model_choice == "Google Generative AI":
        api_key = st.text_input("Enter your Google Generative AI API Key(optional):", type="password")
        if not api_key:
            st.warning("( Optional ) Not providing an API key will opt in for a default key.")
            api_key = os.getenv("GOOGLE_API_KEY")
    else:
        api_key = st.text_input("Enter your OpenAI API Key:", type="password")
        if not api_key:
            st.warning("Please provide an OpenAI API key to use this option.")

    if st.button("Clear Conversation History"):
        st.session_state.conversation_history = ""
        st.success("Conversation history cleared!")

    st.info("Clear the Input field first and then click the button to clear the conversation history.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    if model_choice == "Google Generative AI":
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    else:
        model = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

    agent_executor = create_csv_agent(model, uploaded_file, verbose = True,allow_dangerous_code=True)

    user_input = st.text_input("Ask a question about the CSV data:")

    if user_input:
        try:
            full_input = f"Conversation History:\n{st.session_state.conversation_history}\n\nCurrent Question: {user_input}"

            response = agent_executor.invoke(full_input)

            st.session_state.conversation_history += f"User: {user_input}\nAgent: {response}\n\n"

            st.write("Response:")
            st.write(response['output'])
        except Exception as e:
            st.error(f"An error occurred: {e}")

    if st.session_state.conversation_history:
        st.subheader("Conversation History")
        st.text(st.session_state.conversation_history)

else:
    st.write("Please upload a CSV file to get started.")
