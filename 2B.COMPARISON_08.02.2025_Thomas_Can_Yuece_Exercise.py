#Read URLs:
import urllib.request

import spacy

# Load spaCy language models
nlp_en = spacy.load('en_core_web_sm')
nlp_tr = spacy.load('tr_core_news_md')

# Process manually chosen excerpts from the texts
doc_en = nlp_en("1.  The case originated in an application (no. 11236/09) against the Republic of Turkey lodged with the Court under Article 34 of the Convention for the Protection of Human Rights and Fundamental Freedoms (“the Convention”) by a Turkish national, Mr Mehmet Aytunç Altay (“the applicant”), on 17 February 2006.")
doc_tr = nlp_tr("1.  Davanın temelinde, Mehmet Aytunç Altay (“başvuran”) adlı bir Türk vatandaşı tarafından, İnsan Hakları ve Temel Özgürlüklerin Korunmasına ilişkin Sözleşme’nin (“Sözleşme”) 34. maddesine uygun olarak, 17 Şubat 2006 tarihinde, Türkiye Cumhuriyeti Devleti aleyhine Mahkemeye yapılmış olan başvuru (no. 11236/09) bulunmaktadır.")

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

# Analyse the word lengths:
lengths_en = analyze_word_lengths(doc_en)
lengths_tr = analyze_word_lengths(doc_tr)

print("English Word Lengths: ", lengths_en)
print("Turkish Word Lengths: ", lengths_tr)

# Sorting them from the shortest until the largest word length:
sorted_lengths_en = dict(sorted(lengths_en.items()))
sorted_lengths_tr = dict(sorted(lengths_tr.items()))

print("Sorted English Word Lengths:", sorted_lengths_en)
print("Sorted Turkish Word Lengths:", sorted_lengths_tr)

