import urllib.request

# URLs of the English and the Turkish version of the document
url_en = 'https://hudoc.echr.coe.int/eng?i=001-192210'
url_tr = 'https://hudoc.echr.coe.int/eng?i=001-200254'

# Add User-Agent to request headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'}

# English text request
req_en = urllib.request.Request(url_en, headers=headers)
text_en = urllib.request.urlopen(req_en)
text_en = text_en.read()
text_en = text_en.decode("utf-8")

# Turkish text request (no other changes)
req_tr = urllib.request.Request(url_tr, headers=headers)
text_tr = urllib.request.urlopen(req_tr)
text_tr = text_tr.read()
text_tr = text_tr.decode("utf-8")

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