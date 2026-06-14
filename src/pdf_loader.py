import fitz

def load_pdf(path):
    doc = fitz.open(path)

    pages = []

    for page_num in range(len(doc)):
        page = doc[page_num]

        pages.append({
            "page": page_num + 1,
            "text": page.get_text()
        })

    return pages 