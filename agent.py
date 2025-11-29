import os
from langchain_openai import ChatOpenAI
from tools import get_rendered_html, download_file, post_request, run_code, add_dependencies

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment!")

llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
    api_key=OPENAI_API_KEY
)

def run_agent(task):
    return llm.invoke(task)
