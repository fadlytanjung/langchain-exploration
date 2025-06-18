import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
ls_api_key      = os.getenv("LANGSMITH_API_KEY")
ls_endpoint     = os.getenv("LANGSMITH_ENDPOINT")
ls_project      = os.getenv("LANGSMITH_PROJECT")
ls_tracing_flag = os.getenv("LANGSMITH_TRACING", "false").lower() == "true"

llm = init_chat_model("openai:gpt-4.1-mini",openai_api_key=api_key)