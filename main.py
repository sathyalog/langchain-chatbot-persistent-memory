from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
import os

load_dotenv(override=True)

model = ChatOpenRouter(model=os.environ.get("MODEL"))   

response =model.invoke("Hello, how are you?")

print(response)