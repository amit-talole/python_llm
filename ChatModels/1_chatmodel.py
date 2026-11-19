from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model_name="gpt-5.4-mini") 

model_response = model.invoke("What is the capital of india")

print(model_response.content)