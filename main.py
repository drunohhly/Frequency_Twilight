import re
import nltk
import pymorphy3
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

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

#подсчет частотых слов и создание словаря
word_counts = Counter(lemmas)
most_common_words = word_counts.most_common(20)
print(most_common_words)

#сортировка по частотности
sorted_common_words = sorted(most_common_words, key=lambda x: x[1], reverse=True)

#сортировка на отдельные списки для создания осей
words = [item[0] for item in sorted_common_words]
numbers = [item[1] for item in sorted_common_words]

#создание диаграммы
plt.figure(figsize = (8,5)) #установка ширины и высоты для холста, на котором выведется диаграмма
plt.bar(words, numbers, color = '#e9a0b2')

#настройка подписи осей
plt.title('Частота встречаемости слов')
plt.xlabel('Слова')
plt.ylabel('Частотность')

#редактирование внешнего вида для лучшей читамости
plt.xticks(rotation = 45) #поворот слов на 45 градусов
plt.tight_layout()

plt.show()

