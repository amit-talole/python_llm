from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
    )

model = ChatOpenAI(model_name="gpt-5.4-mini")   

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'nodejs'})

chain.get_graph().print_ascii()  # Print the graph of the chain

print(f"Result: {result}")

