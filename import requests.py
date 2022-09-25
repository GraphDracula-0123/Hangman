import requests
import random
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

words = [WORDS[i].decode('utf-8') for i in range(len(WORDS))]


random_word = random.choice(words)
print(random_word)