import PyPDF2
import csv
from collections import Counter

# Open the PDF file
with open('Data Scinece.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # Extract text from each page of the PDF
    extracted_text = []
    for page in pdf_reader.pages:
        extracted_text.append(page.extract_text())

# Join the extracted text into a single string
full_text = ' '.join(extracted_text)

# Split the text into words
words = full_text.split()

# Count the occurrence of each word
word_counts = Counter(words)

# Find the most repeated word
most_repeated_word = word_counts.most_common(1)[0][0]

# Store the extracted text in a CSV file
with open('extracted_text.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Text'])
    writer.writerow([full_text])

# Print the most repeated word
print("The most repeated word is:", most_repeated_word)
