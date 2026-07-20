from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

load_dotenv(override=True)

model = ChatOpenRouter(model=os.environ.get("MODEL"))   

conversation_history = []

while True:
    user_input = input("You: ")
    conversation_history.append(user_input)
    if user_input.lower() in ["quit", "exit"]:
        break
    ##usually we will give user_input here but we are giving conversation history to maintain context in the conversation
    response = model.invoke(conversation_history) 
    conversation_history.append(response.content)
    print(response.content)
print(f"Conversation History: {conversation_history}")