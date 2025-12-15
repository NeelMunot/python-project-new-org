from pypdf import PdfReader

reader = PdfReader("4_PBL_Programming.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)
