import pandas as pd


last_year_of_observation = 2023
last_row_of_country_data = 196

input_filepath = '../../data/input/2023/imf-dm-export-20231214.xls'
res_filepath = '../../data/intermediate/2023/gdp_per_capita_cleaned.csv'

gdp_df = pd.read_excel(input_filepath)

gdp_df.rename(
    {'GDP per capita, current prices (Purchasing power parity; international dollars per capita)': 'country'},
     axis=1,
    inplace=True)

country_has_data = gdp_df[last_year_of_observation] != 'no data'
gdp_df = gdp_df[country_has_data]

gdp_df[last_year_of_observation] = gdp_df[last_year_of_observation].astype(float)

gdp_df = gdp_df.iloc[:last_row_of_country_data]

gdp_df['country'] = gdp_df['country'].map(lambda z: z.split(',')[0])

gdp_df[['country', last_year_of_observation]].dropna().to_csv(
    res_filepath,
    index=None
)


