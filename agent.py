from langchain.chat_models import init_chat_model

def run_agent(task: str):
    llm = init_chat_model(
        model_provider="groq",
        model="llama-3.1-70b-versatile",
    )
    return llm.invoke(task)
