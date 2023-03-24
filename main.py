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
    
    df = pandas.read_csv('job_CS.csv', usecols=[3], header=None).dropna()
    csv_list = df.values.tolist()
    
    company_list = []
    for company_name in job_list:
        if any(company_name in el for el in csv_list):
            company_list.append(' ' + company_name)
