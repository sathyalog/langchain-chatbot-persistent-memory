from langchain_openrouter import ChatOpenRouter
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

model = ChatOpenRouter(model=os.environ.get("MODEL"))   

conversation_history = [
    SystemMessage(content="""
    You are a helpful AI assistant who answers queries with a bit of humour. Use emojis to make your response looks attractive. Give friendly answers while maintaining the professional tone.
    """)
]

while True:
    user_input = input("You: ")
    conversation_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["quit", "exit"]:
        break
    ##usually we will give user_input here but we are giving conversation history to maintain context in the conversation
    response = model.invoke(conversation_history) 
    conversation_history.append(AIMessage(content=response.content))
    print(response.content)
print(f"Conversation History: {conversation_history}")