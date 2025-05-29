from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('https://es.wikipedia.org/wiki/Python')
html = response.read()  # hasta aqui solo leimos el contenido del texto plano

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

# Si solo queremos obtener los tags <a> o hipervinculos de la pagina:
links = soup.find_all('a')

print(text)
print(links)