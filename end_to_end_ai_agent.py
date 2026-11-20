from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
import os

from end_to_end_ai_agent_via_chain import get_weather_api_key
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchainhub import Client
from langchain_core.output_parsers import StrOutputParser


search_tool = DuckDuckGoSearchRun()

# Custom tool 
@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherapi.com/v1/current.json?key={get_weather_api_key()}&q={city}'

  response = requests.get(url)

  return response.json()


llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0.2)
parser = StrOutputParser()


# Step 2: Pull the ReAct prompt from LangChain Hub
client = Client()
prompt = client.pull("hwchase17/react") # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant. Use tools when required."
)


# Step 5: Invoke
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find the capital of Madhya Pradesh, then find its current weather condition."
        }
    ]
})


print("response", response["messages"][-1].content)