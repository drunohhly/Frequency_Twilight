import re
import nltk
import pymorphy3
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

#удаление стоп-слов
nltk.download('stopwords')
stop_words = set(stopwords.words('russian'))
tokens_without_prepositions = [word for word in tokens if word not in stop_words]

#лемматизация
morph = pymorphy3.MorphAnalyzer()
lemmas = [morph.parse(token)[0].normal_form for token in tokens_without_prepositions]
print(lemmas)
