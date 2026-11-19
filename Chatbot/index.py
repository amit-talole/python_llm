from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate

load_dotenv()

# RAG Based Chatbot

# Step 1a - Indexing (Document Ingestion)

video_id = "l07K2cdLofM" # only the ID, not full URL
try:
    ytt_api = YouTubeTranscriptApi()

    # If you don’t care which language, this returns the “best” one
    transcript = ytt_api.fetch(video_id, languages=["hi", "en"])

    transcript_list = transcript.to_raw_data()
    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    # print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")


# Step 1b - Indexing (Text Splitting)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript], metadatas=[
        {
            "video_id": video_id,
            "source": "youtube"
        }
    ])

print(len(chunks))

# Step 1c & 1d - Indexing (Embedding Generation and Storing in Vector Store)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="youtube_videos_v2",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)


vector_store.add_documents(
    documents=chunks
)

print("Documents stored:", len(chunks))


# Optional: Inspect one stored document
data = vector_store.get()

# print("data", data)




# Step 2 - Retrieval
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
retriever.invoke('What is LLM') # here we are just testing the retriever, it will return the top 4 relevant chunks from the vector store based on the query.
                                     #  means ask a question here 
# print("retriever.invoke('What is deepmind'):", retriever.invoke('What is deepmind'))
# Step 3 - Augmentation

llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0.2)
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question          = "" # here we are just testing the retriever, it will return the top 4 relevant chunks from the vector store based on the query.
retrieved_docs    = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

# print("context_text:", context_text)
# print("question:", question)

# final_prompt = prompt.invoke({"context": context_text, "question": question})


#Step 4 - Generation

# answer = llm.invoke(final_prompt)
# print("answer.content:", answer.content)


## Building a Chain
def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

parallel_chain.invoke('What is AI Cost?') # here we are just testing the parallel_chain, it will return the context and question in a dictionary format.

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

resultTwo = main_chain.invoke('Can you summarize the video')

print("resultTwo:", resultTwo)