from langchain_groq import ChatGroq

llm = ChatGroq(model="mixtral-8x7b-32768")

def run_agent(task):
    return llm.invoke(task)
