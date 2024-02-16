from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import requests


input_url = 'https://www.prisonstudies.org/highest-to-lowest/prison_population_rate?field_region_taxonomy_tid=All'
output_filepath = '../../data/intermediate/2023/prison.csv'

r = requests.get(input_url)

soup = BeautifulSoup(r.text, 'html.parser')

countries = soup.find('tbody').find_all('tr')

def get_country(country_html_block):
    return country_html_block.find('a').text.strip()

def get_incarceration_rate(country_html_block):
    value_class_name = 'views-field views-field-field-integer'
    return country_html_block.find('td', {
        'class': value_class_name
    }).text.strip()

country_dct = {
    'country': [],
    'incarceration_rate': []
}

for country in tqdm(countries):
    country_dct['country'].append(get_country(country))
    country_dct['incarceration_rate'].append(
        get_incarceration_rate(country)
    )

prison_df = pd.DataFrame(country_dct)

is_data_exist = prison_df['incarceration_rate'] != ''
prison_df = prison_df[is_data_exist]

prison_df['incarceration_rate'] = prison_df['incarceration_rate'].astype(int)

print(prison_df['incarceration_rate'].isnull().sum())

prison_df.to_csv(output_filepath, index=False)