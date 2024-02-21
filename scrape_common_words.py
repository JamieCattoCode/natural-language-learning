import requests
import csv
from bs4 import BeautifulSoup

# Request the URL and create soup
url = 'https://vocab.chat/blog/most-common-portuguese-words.html'
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

# Get the inner text of all tags with class 'vocab'
vocab_tags = soup.find_all(class_="vocab")
vocab_list = [element.get_text() for element in vocab_tags]

# Get the inner text of all tags with class 'pos'
pos_tags = soup.find_all(class_="pos")
# Remove the first and last character from the 'pos' tags' inner texts
word_type_list = [element.get_text()[1:-1] for element in pos_tags]

# Get the inner text of all tags with class 'definition'
definition_tags = soup.find_all(class_="definition")
definition_list = [element.get_text()[1:-1] for element in definition_tags]

# Write all of the values to the CSV
csv_filename = 'portugese_vocabulary.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Type', 'Definition', 'Association'])
    for vocab, word_type, definition in zip(vocab_list, word_type_list, definition_list):
        writer.writerow([vocab, word_type, definition, ''])
