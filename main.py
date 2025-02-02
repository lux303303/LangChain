from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

if __name__ == '__main__':
    messages = [
        SystemMessage("You are a helpful assistant."),
        HumanMessage("こんにちは！"),
    ]

    for chunk in  model.stream(messages):
        print(chunk.content, end="", flush=True)


