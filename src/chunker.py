from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = []

    for page in pages:

        page_chunks = splitter.split_text(
            page["text"]
        )

        for chunk in page_chunks:

            chunks.append({
                "page": page["page"],
                "content": chunk
            })

    return chunks