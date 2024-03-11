import os
import spacy
import locale
from collections import defaultdict
import json

"""1.Index File"""

# Set the locale to Urdu (Pakistan)
locale.setlocale(locale.LC_ALL, 'ur_PK.UTF-8')

# Create a blank 'ur' model
nlp = spacy.blank("ur")

# Directory containing your text files
directory = './Urdu Corpus/'


# Output directory for the new files
output_directory = './Output/'

# Initialize index structures
index = defaultdict(lambda: {"frequency": 0, "postings": []})


# Load Urdu stopwords from file
with open("./urdu_stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = set(f.read().splitlines())

# Get list of all files in the directory
files = os.listdir(directory)

# Process each file
for file_name in files:
    # Only process .txt files
    if file_name.endswith('.txt'):
        # Construct full file path
        file_path = os.path.join(directory, file_name)

        # Load the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Process the text
        doc = nlp(text)

        unique_words = set()

        # Initialize an empty list to store non-stopwords
        non_stopwords = []
        # Loop through each token in the document
        for token in doc:
            # Check if the token is a word (is_alpha) and not a stopword
            if token.is_alpha and token.text.lower() not in stopwords:
                non_stopwords.append(token.text)

        # Sort the non-stopwords and print them
        sorted_non_stopwords = sorted(non_stopwords)
        # for word in sorted_non_stopwords:
        #     print(word)

        # Update index for each term
        for term in sorted_non_stopwords:
            index[term]["frequency"] += 1
            if file_name not in index[term]["postings"]:
                index[term]["postings"].append(file_name)


# Write the index to a file
output_file_path = os.path.join(output_directory, 'index.json')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(index, output_file, ensure_ascii=False, indent=4)



"""2.Postings File"""

# Initialize postings dictionary
postings = defaultdict(lambda: [])

# Process each file
for file_name in files:
    # Only process .txt files
    if file_name.endswith('.txt'):
        # Construct full file path
        file_path = os.path.join(directory, file_name)

        # Load the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Process the text
        doc = nlp(text)

        # Initialize an empty set to store non-stopwords
        non_stopwords = set()

        # Loop through each token in the document
        for i, token in enumerate(doc):
            # Check if the token is a word (is_alpha) and not a stopword
            if token.is_alpha and token.text.lower() not in stopwords:
                term = token.text
                non_stopwords.add(term)
                postings[term].append({"document": file_name, "position": i})

# Write postings to a file
postings_file_path = os.path.join(output_directory, 'postings.json')
with open(postings_file_path, 'w', encoding='utf-8') as postings_file:
    json.dump(postings, postings_file, ensure_ascii=False, indent=4)

"""3.Test File Search & Retrieval"""
import json

# Read the test file
with open('test.txt', 'r', encoding='utf-8') as test_file:
    test_text = test_file.read()

# Load the index file
with open('Output/index.json', 'r', encoding='utf-8') as index_file:
    index = json.load(index_file)

# Load the postings file
with open('Output/postings.json', 'r', encoding='utf-8') as postings_file:
    postings = json.load(postings_file)

# Tokenize the test text
test_tokens = test_text.split()

# Input a sequence of single terms
while True:
    term = input("Enter a term (or 'exit' to quit): ")
    if term.lower() == 'exit':
        break

    # Check if the term exists in the index
    if term in index:
        print(f"Term: {term}")
        print("Postings:")
        for posting in postings[term]:
            print(f"DocID: {posting['document']}, Position: {posting['position']}")
    else:
        print("Term not found in the inverted file.")
