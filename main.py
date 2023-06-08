import requests
from bs4 import BeautifulSoup
import pandas
import eel

eel.init('web')
@eel.expose

def JPC():
    link = ('https://www.linkedin.com')
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')

# collecting data from the page by findindg a class and creating a new list
    job_list = []
    result = soup.find_all("a", {"class": "hidden-nested-link"})
    for i in result:
        job_list.append(i.text.strip())

# reads a csv file with a list of already applied positions and removes the rows that contains NULL values
    df = pandas.read_csv('jobs.csv', usecols=[3], header=None).dropna()
    csv_list = df.values.tolist()

# finds the same companies on the page and compares them from the csv file
    company_list = []
    for company_name in job_list:
       if any(company_name in el for el in csv_list):
           company_list.append(' ' + company_name)
    return company_list
JPC()

try:
    eel.start('index.html', mode='chrome', host='localhost')
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
