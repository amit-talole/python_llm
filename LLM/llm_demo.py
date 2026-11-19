from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model_name="gpt-5.4-mini")

result = llm.invoke("What is the capital of india")

print(result)   