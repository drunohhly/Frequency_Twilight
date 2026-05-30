import re

text = open("text.txt", "r", encoding="utf-8")
text = text.read()

text = text.lower()
text = re.sub(r'[^а-яё\s]', '', text)
text = re.sub(r'\s+', ' ', text)
