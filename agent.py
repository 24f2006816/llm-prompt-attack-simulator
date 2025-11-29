from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def run_agent(task: str):
    return llm.invoke(task).content
