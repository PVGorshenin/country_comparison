import pandas as pd
import requests

from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://en.wikipedia.org/wiki/World_Heritage_Sites_by_country'
output_filepath = 'data/intermediate/2023/unesco.csv'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find("table",{"class":"wikitable sortable"})
countries = table.find('tbody').find_all('tr')

def get_country(country):
    return country.find_all('td')[0].find('a')['title']


def get_total_objects(country):
    return int(country.find_all('td')[4].text.strip())


country_dct = {
    'country': [],
    'unesco_objects': []
}

for country in tqdm(countries[1:-2]):
    country_dct['country'].append(get_country(country))
    country_dct['unesco_objects'].append(get_total_objects(country))

unesco_df = pd.DataFrame(country_dct)

unesco_df.to_csv(output_filepath, index=None)