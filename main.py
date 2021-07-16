import requests
from bs4 import BeautifulSoup

URL = 'https://www.fortypoundhead.com/tools_bullshit_generator.asp'

print('Retrieving from URL: ', URL)

page_text = requests.get(URL)
soup = BeautifulSoup(page_text.content, 'html.parser')

bullshit = soup.body.find('h1', text='Buzzword Bullshit Generator').findNext('p').findNext('p').findNext('p').text

print('Some bullshit: ', bullshit)
