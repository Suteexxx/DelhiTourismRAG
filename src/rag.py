from src.retriever import retrieve
from src.llm import generate_answer

def ask(question):

    docs = retrieve(question)

    context = ""

    sources = []

    for doc in docs:

        context += doc["content"] + "\n\n"

        sources.append(
            f"Page {doc['page']}"
        )

    prompt = f"""
You are an expert Delhi Tourism Assistant. 

Use the following pieces of retrieved context to answer the user's question. If the context doesn't contain the exact answer, use your general knowledge about Delhi to provide a comprehensive response, but prioritize any specific details present in the context.

Retrieved Context:
{context}

User Question: {question}
Answer:
"""

    answer = generate_answer(
        prompt
    )

    return answer, list(set(sources))