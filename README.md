# Simple LangChain Chatbot Exploration in Jupyter Lab

## Overview

This project explores LangChain by building a simple chatbot entirely within Jupyter Lab. It demonstrates:

• Installing and configuring LangChain and python-dotenv • Loading environment variables from a `.env` file • Initializing an OpenAI‐backed chat model • Streaming assistant responses interactively in notebook cells

## Files

• `README.txt`        ── This file. • `.env`              ── Store your API keys here: OPENAI\_API\_KEY=sk-… • `notebook.ipynb`    ── Jupyter notebook demonstrating setup and interactive chat loop.

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
   pip install langchain openai python-dotenv ipywidgets
   ```
4. **Enable ipywidgets** (if not already):
   ```bash
   jupyter labextension install @jupyter-widgets/jupyterlab-manager
   ```
5. **Create a **`` in project root:
   ```dotenv
   OPENAI_API_KEY=sk-your-key-here
   ```

## Running in Jupyter Lab

1. **Start Jupyter Lab**:
   ```bash
   jupyter lab
   ```
2. **Open **`` in the Lab interface.
3. **Run the setup cell** to load environment variables and initialize the LLM.
4. **Use the interactive chat cell** to send messages and stream assistant replies.

## Customization

• Change the model name in the notebook’s `init_chat_model` call. • Modify the streaming function or UI widgets as desired.

## Troubleshooting

- **Widgets not loading**: Ensure `ipywidgets` is installed and the labextension is enabled.
- **API key errors**: Confirm your `.env` is in the project root and loaded with `python-dotenv` before usage.

Enjoy exploring LangChain live in Jupyter Lab!

