from langchain.agents import create_agent
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchainhub import Client



search_tool = DuckDuckGoSearchRun()


def get_weather_api_key():
    """
    This function retrieves the weather API key from environment variables.
    """
    return os.getenv("WEATHER_API_KEY")

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


# Step 2: Pull the ReAct prompt from LangChain Hub
client = Client()
prompt = client.pull("hwchase17/react") # pulls the standard ReAct agent prompt


# Step 1: Create Agent
agent = create_agent(
    model=llm,
    tools=[search_tool, get_weather_data],
    system_prompt="You are a helpful assistant. Use tools when required."
)

# Step 2: Wrap Agent inside RunnableLambda
agent_runnable = RunnableLambda(
    lambda x: agent.invoke({
        "messages": [
            {"role": "user", "content": x["input"]}
        ]
    })
)

# Step 3: Create LCEL chain
chain = agent_runnable | RunnableLambda(
    lambda response: response["messages"][-1].content
)

# Step 4: Invoke Chain
response = chain.invoke({
    "input": "Find the capital of Maharashtra, then find its current weather condition."
})

print("Response:", response)