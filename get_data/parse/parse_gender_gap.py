from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests


input_url = 'https://en.wikipedia.org/wiki/Global_Gender_Gap_Report'
output_filepath = '../../data/intermediate/2023/gender_gap.csv'

r = requests.get(input_url)

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find("table",{"class":"wikitable sortable"})
countries = table.find('tbody').find_all('tr')

def get_country(country):
    return country.find_all('td')[0].find('a')['title']


def get_equality_score(country):
    last_year_russia_has_data_rel = -2
    eq_score_str = country.find_all('td')[last_year_russia_has_data_rel].text.strip()
    if eq_score_str == 'N/A':
        return np.NAN
    return float(eq_score_str)


country_dct = {
    'country': [],
    'gender_equality_score': []
}

still_header = 2

for country in countries[still_header:]:
    country_dct['country'].append(get_country(country))

    n_cols = 18
    assert len(country.find_all('td')) == n_cols

    country_dct['gender_equality_score'].append(get_equality_score(country))

gender_equality_df = pd.DataFrame(country_dct)

gender_equality_df.to_csv(output_filepath, index=False)