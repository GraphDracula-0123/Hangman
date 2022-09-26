import requests
import random


word_site = "http://www.netzmafia.de/software/wordlists/deutsch.txt"
response = requests.get(word_site)
WORDS = response.content.splitlines()
#words = [WORDS[i].decode('utf-8') for i in range(len(WORDS))]


words = []
for i in range(len(WORDS)):
    try:
        words.append(WORDS[i].decode('utf-8'))
    except:
        continue
    
  
print(words)

