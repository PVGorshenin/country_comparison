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

def treat_uk(prison_df):

    uk_mean_stat =\
        0.89 * prison_df.loc[prison_df['country']=='United Kingdom: England & Wales', 'incarceration_rate'].values +\
        0.09 * prison_df.loc[prison_df['country']=='United Kingdom: Northern Ireland', 'incarceration_rate'].values + \
        0.02 * prison_df.loc[prison_df['country']=='United Kingdom: Scotland', 'incarceration_rate'].values

    uk_regions_mask = prison_df['country'].map(lambda z: 'United Kingdom' in z)
    prison_df = prison_df[~uk_regions_mask]

    prison_df.reset_index(drop=True, inplace=True)

    prison_df.loc[prison_df.shape[0]+1] = ['United Kingdom', int(uk_mean_stat[0])]
    return prison_df


def treat_bosnia(prison_df):

    bosnia_mean_stat = \
            0.62 * prison_df.loc[prison_df['country']=='Bosnia and Herzegovina: Federation', 'incarceration_rate'].values +\
            0.38 * prison_df.loc[prison_df['country']=='Bosnia and Herzegovina: Republika Srpska', 'incarceration_rate'].values

    bosnia_regions_mask = prison_df['country'].map(lambda z: 'Bosnia' in z)
    prison_df = prison_df[~bosnia_regions_mask]

    prison_df.reset_index(drop=True, inplace=True)

    prison_df.loc[prison_df.shape[0]+1] = ['Bosnia and Herzegovina', int(bosnia_mean_stat[0])]

    return prison_df


prison_df = treat_uk(prison_df)
prison_df = treat_bosnia(prison_df)


print(prison_df['incarceration_rate'].isnull().sum())

prison_df.sort_values(by='country').to_csv(output_filepath, index=False)