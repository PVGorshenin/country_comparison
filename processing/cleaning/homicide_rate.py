import pandas as pd


input_filepath = '../../data/input/2022/homicide_rate.csv'
res_filepath = '../../data/intermediate/2023/homicide_cleaned.csv'

res_colname = 'homicide_rate'

homi_df = pd.read_csv(input_filepath)

is_summarize_rate = homi_df['Indicator'] == 'Homicide rate'
homi_df = homi_df[is_summarize_rate]

is_max_year = homi_df['Year'] == homi_df.groupby('Country')['Year'].transform(max)
homi_df = homi_df[is_max_year]

homi_df.rename(columns={
    'Country': 'country',
    'value': res_colname
}, inplace=True)

homi_df[['country', res_colname]].to_csv(res_filepath, index=None)