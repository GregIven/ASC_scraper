from pdfminer.high_level import extract_text

text = extract_text("ASC_AL.pdf")

print(text)