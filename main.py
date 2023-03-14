import requests
from bs4 import BeautifulSoup


link = ('https://www.linkedin.com')
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
