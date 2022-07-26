##############
import pandas as pd
from urllib.request import urlopen # para leer el link
from bs4 import BeautifulSoup # quitar etiquetas html
import nltk
from nltk.corpus import stopwords # stopwords
from nltk.tokenize import word_tokenize
################

## source 

link = "https://www.epdlp.com/texto.php?id2=557"

## Leer el texto ##
html = urlopen(link).read()
soup = BeautifulSoup(html, features="html.parser")


texto = soup.get_text() # extrae texto
texto = texto.lower() # estandarizo minuscula

quitar = '().&",' # limpieza de algunos caracteres

for caracter in quitar:
    texto = texto.replace(caracter,"")


#text_tokens = word_tokenize(texto)

#text_tokens = texto.split()
#words.count(p)

## Limpieza de stopwords para el diccionario
nltk.download('stopwords')
nltk.download('punkt')

stopwords = set(stopwords.words('spanish'))
word_tokens = word_tokenize(texto)

texto_sin_sw = [w for w in word_tokens if not w.lower() in stopwords]
  
texto_sin_sw = []
  
for w in word_tokens:
    if w not in stopwords:
        texto_sin_sw.append(w)

## cuenta frecuencia de cada palabra

freq = [texto_sin_sw.count(p) for p in texto_sin_sw]

## Diccionario
dicc = dict(list(zip(texto_sin_sw,freq)))
print(dicc)

################
## a dataframe para visualizar mejor

df = pd.DataFrame(list(dicc.items()), columns=['palabra', 'Frecuencia'])

df.sort_values(by='Frecuencia', ascending=False)

