# import pytesseract
# from PIL import Image
# import faiss
# import numpy as np
# import os
# from sentence_transformers import SentenceTransformer
# from transformers import pipeline


# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# IMAGE_PATH = "handwritten.png"   # <-- change path if needed
# TOP_K = 3


# print(" Loading models...")

# embedder = SentenceTransformer("all-MiniLM-L6-v2")

# qa_pipeline = pipeline(
#     "question-answering",
#     model="deepset/roberta-base-squad2"
# )

# print(" Models loaded")


# def extract_text_from_image(image_path):
#     image = Image.open(image_path)
#     text = pytesseract.image_to_string(image)
#     return text.strip()


# def chunk_text(text, chunk_size=300):
#     words = text.split()
#     chunks = []
#     for i in range(0, len(words), chunk_size):
#         chunks.append(" ".join(words[i:i + chunk_size]))
#     return chunks


# def build_faiss_index(chunks):
#     embeddings = embedder.encode(chunks)
#     embeddings = np.array(embeddings).astype("float32")

#     dimension = embeddings.shape[1]
#     index = faiss.IndexFlatL2(dimension)
#     index.add(embeddings)

#     return index, embeddings


# def retrieve_context(question, chunks, index, top_k=TOP_K):
#     question_embedding = embedder.encode([question])
#     question_embedding = np.array(question_embedding).astype("float32")

#     _, indices = index.search(question_embedding, top_k)
#     return " ".join([chunks[i] for i in indices[0]])


# def ask_question(question, context):
#     result = qa_pipeline(
#         question=question,
#         context=context
#     )
#     return result["answer"]


# if __name__ == "__main__":

#     if not os.path.exists(IMAGE_PATH):
#         print(" Image not found:", IMAGE_PATH)
#         exit()

#     print("\n Running OCR...")
#     text = extract_text_from_image(IMAGE_PATH)

#     if len(text) == 0:
#         print(" No text extracted")
#         exit()

#     print(" OCR Done")

#     print("\n Chunking text...")
#     chunks = chunk_text(text)
#     print(f" Created {len(chunks)} chunks")

#     print("\n Building FAISS index...")
#     index, _ = build_faiss_index(chunks)
#     print(" FAISS index ready")

#     print("\n SYSTEM READY — Ask questions (type 'exit' to quit)\n")

#     while True:
#         question = input(" Your question: ")

#         if question.lower() == "exit":
#             print( "Exiting...")
#             break

#         context = retrieve_context(question, chunks, index)
#         answer = ask_question(question, context)

#         print("\n Answer:", answer)
#         print("-" * 60)



# from google import genai
import google.generativeai as genai
from PIL import Image
from datetime import datetime
import os


HISTORY_FILE = "image_summary_history.txt"
API_KEY=os.getenv("API_KEY")


client = genai.Client(api_key=API_KEY)


def extract_text_from_image(image_path: str) -> str:
    

    image = Image.open(image_path)

    prompt = """
    You are an intelligent assistant.
    Look only at the image provided.
    Describe its content and summarize it.
    Final summary MUST be exactly two lines.
    Do NOT add information not present in the image.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    summary_text = response.text.strip()

  
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"Image: {os.path.basename(image_path)}\n")
        f.write(f"Summary:\n{summary_text}\n")
        f.write("=" * 50 + "\n")

    return summary_text


summary = extract_text_from_image("invoices.png")
print(summary)

