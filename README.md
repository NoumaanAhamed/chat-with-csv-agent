# Chat with CSV

This Streamlit application allows users to upload a CSV file and ask questions about the data. It uses Gemini model to provide insights and answers about the uploaded data interactively. The application also supports conversation history tracking.

## Features

- Upload a CSV file for analysis.
- Ask questions about the data in the CSV.
- Conversation history tracking for context-aware interactions.
- Configurable API key management for enhanced security.
- Clear conversation history with a button click.
- Langsmith monitoring and tracing for advanced analytics.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/NoumaanAhamed/chat-with-csv-agent
   cd chat-with-csv-agent
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root and add the following:
     ```env
     GOOGLE_API_KEY=<your-google-generative-ai-api-key>
     LANGSMITH_TRACING=<optional>
     LANGSMITH_ENDPOINT=<optional>
     LANGSMITH_API_KEY=<optional>
     LANGSMITH_PROJECT=<optional>
     ```
   - Replace `<your-google-generative-ai-api-key>` with your API key from Google Generative AI.

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Use the sidebar to configure your API key or use the default key from `.env`.

4. Upload a CSV file using the file uploader in the main app interface.

5. Type a question about the data in the CSV into the text input box and view the AI-generated response.

6. Manage conversation history using the "Clear Conversation History" button in the sidebar.

## Troubleshooting

- **Error: Missing API Key**: Ensure you have set up the `GOOGLE_API_KEY` environment variable or entered the key in the sidebar input.
- **Streamlit Error**: Verify that all required dependencies are installed, and the virtual environment is activated.
- **CSV File Upload Issues**: Confirm that the file is in `.csv` format and is not corrupted.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for UI
- [LangChain](https://www.langchain.com/) for experimental CSV agent tools.
- [Google Generative AI](https://cloud.google.com/ai-solutions/generative-ai) for AI model.
