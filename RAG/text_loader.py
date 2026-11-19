from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model_name="gpt-5.4-mini")

prompt = PromptTemplate(
    template='Generate  summary for following poem \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'text': docs[0].page_content}))




