import pandas as pd
import requests

from bs4 import BeautifulSoup

url = 'https://www.numbeo.com/quality-of-life/rankings_by_country.jsp'
output_filepath = '../../data/intermediate/2023/numbeo.csv'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
numbeo_cols = soup.find_all('tr')[1]

numbeo_dict = {}
for col in numbeo_cols.find_all('th'):
    numbeo_dict[col.text] = []


for country in soup.find_all('tr')[2:]:
    for i, feature in enumerate(country.find_all('td')):
        numbeo_dict[list(numbeo_dict.keys())[i]].append(feature.text)

numbeo_dict.pop('Rank')

numbeo_df = pd.DataFrame(numbeo_dict)

numbeo_df.to_csv(output_filepath, index=None)

