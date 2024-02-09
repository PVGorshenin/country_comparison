import pandas as pd


input_filepath = '../../data/input/2022/median_age.xlsx'
output_filepath = '../../data/intermediate/2023/median_age_cleaned.csv'

age_df = pd.read_excel(input_filepath)

only_country_slice = age_df['Type']=='Country/Area'
age_df = age_df[only_country_slice]

age_df.rename(
    {'Region, subregion, country or area *': 'country'},
    axis=1,
    inplace=True
)

closing_year_of_last_five_years = '2020'
age_df['distance_to_30_years'] = age_df[closing_year_of_last_five_years].map(lambda z: abs(float(z) - 30))

age_df[['country', 'distance_to_30_years']].to_csv(output_filepath, index=None)