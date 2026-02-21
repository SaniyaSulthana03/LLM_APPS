# import os
# from dotenv import load_dotenv
# load_dotenv()

# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# from langchain_groq import ChatGroq
# from langchain_community.embeddings import HuggingFaceEmbeddings


# with open("AI_psychology_medium.txt", "r", encoding="utf-8") as f:
#     text = f.read()


# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200
# )

# chunks = text_splitter.split_text(text)

# print(f"Total chunks created: {len(chunks)}")





# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )


# vectorstore = FAISS.from_texts(
#     texts=chunks,
#     embedding=embeddings
# )



# retriever = vectorstore.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 5}
# )


# from langchain_core.prompts import PromptTemplate

# summary_prompt = PromptTemplate(
#     input_variables=["context"],
#     template="""
# You are a professional summarizer.

# STRICT RULES:
# - Output MUST be at most 4 bullet points
# - Each bullet point ≤ 12 words
# - Do NOT add explanations
# - Do NOT repeat information
# - Give it in crisp manner 
# - I dont want lenghty answer short it  

# Context:
# {context}

# Very Short Summary:
# """
# )



# llm =  ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.3,
#     max_tokens=60,
#     api_key=os.getenv("GROQ_API_KEY")
# )


# rag_chain = (
#     {"context": retriever}
#     | summary_prompt
#     | llm
#     | StrOutputParser()
# )


# summary = rag_chain.invoke("Summarize the document")

# print(summary)



# import os
# import json
# from datetime import datetime
# from dotenv import load_dotenv

# # ------------------ ENV SETUP ------------------
# load_dotenv()

# # ------------------ LANGCHAIN IMPORTS ------------------
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from langchain_groq import ChatGroq
# from langchain_community.embeddings import HuggingFaceEmbeddings

# # ------------------ FILE PATHS ------------------
# TEXT_FILE = "AI_psychology_medium.txt"
# HISTORY_FILE = "rag_history.json"

# # ------------------ LOAD TEXT ------------------
# with open(TEXT_FILE, "r", encoding="utf-8") as f:
#     text = f.read()

# # ------------------ TEXT SPLITTING ------------------
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200
# )

# chunks = text_splitter.split_text(text)
# print(f"Total chunks created: {len(chunks)}")

# # ------------------ EMBEDDINGS ------------------
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # ------------------ VECTOR STORE ------------------
# vectorstore = FAISS.from_texts(
#     texts=chunks,
#     embedding=embeddings
# )

# retriever = vectorstore.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 5}
# )

# # ------------------ PROMPT ------------------
# summary_prompt = PromptTemplate(
#     input_variables=["context"],
#     template="""
# You are a professional summarizer.

# STRICT RULES:
# - Output MUST be at most 4 bullet points
# - Each bullet point ≤ 12 words
# - Do NOT add explanations
# - Do NOT repeat information
# - Keep it very short and crisp

# Context:
# {context}

# Very Short Summary:
# """
# )

# # ------------------ LLM ------------------
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.3,
#     max_tokens=60,
#     api_key=os.getenv("GROQ_API_KEY")
# )

# # ------------------ RAG CHAIN ------------------
# rag_chain = (
#     {"context": retriever}
#     | summary_prompt
#     | llm
#     | StrOutputParser()
# )

# # ------------------ HISTORY FUNCTION ------------------
# def save_rag_history(query, response):
#     history = []

#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#             history = json.load(f)

#     history.append({
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "query": query,
#         "response": response
#     })

#     with open(HISTORY_FILE, "w", encoding="utf-8") as f:
#         json.dump(history, f, indent=4)

# # ------------------ RUN ------------------
# if __name__ == "__main__":
#     query = "Summarize the document"

#     summary = rag_chain.invoke(query)

#     print("\n--- SUMMARY ---")
#     print(summary)

#     save_rag_history(query, summary)
#     print("\nSummary saved to history")




import os
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings


HISTORY_FILE = "rag_history.json"



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

summary_prompt = PromptTemplate(
    input_variables=["context"],
    template="""
You are a professional summarizer.

STRICT RULES:
- Output MUST be at most 4 bullet points
- Each bullet point ≤ 12 words
- Do NOT add explanations
- Do NOT repeat information
- Keep it very short and crisp

Context:
{context}

Very Short Summary:
"""
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    max_tokens=60,
    api_key=os.getenv("GROQ_API_KEY")
)


def save_rag_history(query, response):
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)

    history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "query": query,
        "response": response
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

def summarize_text_with_rag(text_file_path: str, query: str = "Summarize the document") -> str:
    """
    Loads a text file, performs RAG-based summarization,
    and stores query-response history in JSON.
    """


    with open(text_file_path, "r", encoding="utf-8") as f:
        text = f.read()

  
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    # -------- Vector store --------
    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    # -------- RAG chain --------
    rag_chain = (
        {"context": retriever}
        | summary_prompt
        | llm
        | StrOutputParser()
    )

    # -------- Run RAG --------
    response = rag_chain.invoke(query)

    # -------- Save history --------
    save_rag_history(query, response)

    return response


summary = summarize_text_with_rag("AI_psychology_medium.txt")
print(summary)