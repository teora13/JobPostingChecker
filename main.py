import requests
from bs4 import BeautifulSoup


link = ('https://www.linkedin.com')
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
    
    job_list = []
    result = soup.find_all("a", {"class": "hidden-nested-link"})
    for i in result:
        job_list.append(i.text.strip())
    print(job_list)
