import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = open("text.txt", "r", encoding="utf-8")
text = text.read()

#очищение текста
text = text.lower()
text = re.sub(r'[^а-яё\s]', '', text)
text = re.sub(r'\s+', ' ', text)

#токенизация
nltk.download('punkt_tab')
tokens = word_tokenize(text)
print(tokens)