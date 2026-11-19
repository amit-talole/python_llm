from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


from langchain_community.document_loaders import WebBaseLoader


model = ChatOpenAI(model_name="gpt-5.4-mini")

prompt = PromptTemplate(
    template='Ans the following question \n {question} based on the given text \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url ='https://www.flipkart.com/home-stylish-213-cm-7-ft-door-silk-blackout-curtain-pack-2/p/itm91633ef95ca0a?pid=CRNH7HHURBHGZCGB&lid=LSTCRNH7HHURBHGZCGB1Q8AOE&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJyZWNvIiwicHJwdCI6ImNscCIsIm1pZCI6ImZhY3RCYXNlZFJlY29tbWVuZGF0aW9uL3JlY2VudGx5Vmlld2VkIn0%3D&ctx=eyJkZWxpdmVyZWRCeSI6IiIsImRpc3BsYXlQcmljZSI6IjYzOCJ9&pageUID=1794850146091'

loader = WebBaseLoader(url)


docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question': 'What is the product name and price?', 'text': docs[0].page_content}))
