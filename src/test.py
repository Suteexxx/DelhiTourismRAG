from src.pdf_loader import load_pdf

pages = load_pdf("data/delhi_facts.pdf")

print("Total pages:", len(pages))
print(pages[0]["text"][:300])