from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

keywords = ['дистанційна', 'курс', 'програмування', 'Python']

with open("prometheus.html", "r", encoding="utf-8") as f:
  text = f.read()

soup = BeautifulSoup(text, 'html.parser')

text = ' '.join([p.get_text() for p in soup.find_all('p')])

word_count = {keyword: text.lower().count(keyword) for keyword in keywords}

plt.bar(word_count.keys(), word_count.values(), color='blue')

plt.xlabel('Ключові слова')
plt.ylabel('Частота')
plt.title('Частота зустрічей ключових слів на сайті prometheus.org.ua')

plt.show()
