# Simple LangChain Chatbot Exploration in Jupyter Lab

## Overview

This project explores LangChain by building a simple chatbot entirely within Jupyter Lab. It demonstrates:

- Installing and configuring LangChain and python-dotenv
- Loading environment variables from a `.env` file
- Initializing an OpenAI‐backed chat model
- Streaming assistant responses interactively in notebook cells

## Files
```
/project
├── README.md        # documentation
├── main.py          # if wanna running in CLI
└── notebook.ipynb   # jupyter notebook for project
```
## Setup

1. **Clone or download** this repo.
2. **Create and activate** a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .\.venv\Scripts\activate     # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install langchain openai python-dotenv ipywidgets jupyterlab
   ```
4. **Create a `.env` file in project root**:
   ```dotenv
   OPENAI_API_KEY=sk-your-key-here
   TRAVILY_API_KEY=<travily-api-key>
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
   LANGSMITH_API_KEY=<langsmith-api-keyL
   LANGSMITH_PROJECT=<your-project-name>
   ```

## Running in Jupyter Lab

1. **Start Jupyter Lab**:
   ```bash
   jupyter lab
   ```
2. **Open host url** in the Lab interface
3. **Run the setup cell** to load environment variables and initialize the LLM.
4. **Use the interactive chat cell** to send messages and stream assistant replies.

## Customization

• Change the model name in the notebook’s `init_chat_model` call. • Modify the streaming function or UI widgets as desired.

## Troubleshooting

- **Widgets not loading**: Ensure `ipywidgets` is installed and the labextension is enabled.
- **API key errors**: Confirm your `.env` is in the project root and loaded with `python-dotenv` before usage.

Enjoy exploring LangChain live in Jupyter Lab!

