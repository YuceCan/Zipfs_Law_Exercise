# Function to read text from a file
def load_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

# Load texts from files instead of URLs
text_en = load_text_from_file("english_text.txt")  
text_tr = load_text_from_file("turkish_text.txt")

#Import the following library for NLP-related tasks
import spacy

# Load English and Turkish language models in order to initialise NLP for processing texts of each language
nlp_en = spacy.load('en_core_web_sm')
nlp_tr = spacy.load('tr_core_news_md')

# Processing the texts by using the language model of each language:
doc_en = nlp_en(text_en)
doc_tr = nlp_tr(text_tr)

# Debugging: Print a sample of the downloaded texts
print("English Text Sample:", repr(text_en[:500]))  # Shows hidden characters
print("Turkish Text Sample:", repr(text_tr[:500]))  # Shows hidden characters

def analyze_word_lengths(doc):
    lengths = {}
    for token in doc:
        # Token must not be a punctuation, space or number and only contain letters
         if token.is_alpha:
            length = len(token.text)
            if length in lengths:
                lengths[length] += 1
            else:
                lengths[length] = 1
    return lengths

# Analyse the word lengths
lengths_en = analyze_word_lengths(doc_en)
lengths_tr = analyze_word_lengths(doc_tr)

print("English Word Lengths: ", lengths_en)
print("Turkish Word Lengths: ", lengths_tr)

# Sorting them from the shortest until the largest word length
sorted_lengths_en = dict(sorted(lengths_en.items()))
sorted_lengths_tr = dict(sorted(lengths_tr.items()))

print("Sorted English Word Lengths:", sorted_lengths_en)
print("Sorted Turkish Word Lengths:", sorted_lengths_tr)

# Import the following libraries:
import pandas as pd  # for data handling
import numpy as np  # for numerical operations
import matplotlib.pyplot as plt  # for plotting
import seaborn as sns  # for better visualisation

sns.set_theme(style="darkgrid")

# Plot Zipf's Law of Abbreviation (Word Length vs. Log(Frequency))

# English word length plot
plt.figure(figsize=(8, 5))
plt.scatter(sorted_lengths_en.keys(), np.log(np.array(list(sorted_lengths_en.values())) + 1))
plt.title("Zipf's Law of Abbreviation - English")
plt.xlabel("Word Length")
plt.ylabel("Log(Frequency)")

# Turkish word length plot
plt.figure(figsize=(8, 5))
plt.scatter(sorted_lengths_tr.keys(), np.log(np.array(list(sorted_lengths_tr.values())) + 1))
plt.title("Zipf's Law of Abbreviation - Turkish")
plt.xlabel("Word Length")
plt.ylabel("Log(Frequency)")

plt.show()
