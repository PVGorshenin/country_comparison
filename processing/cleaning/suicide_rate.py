import pandas as pd


inp_filepath = '../../data/input/2022/suicide_rate.csv'
res_filepath = '../../data/intermediate/2023/suicide_cleaned'

suicide_df = pd.read_csv(inp_filepath)
last_year_of_observation = '2019'
res_colname = 'suicide_rate'

def exclude_header(sui_df):
    sui_df.columns = sui_df.iloc[0].values
    sui_df = sui_df.iloc[1:]
    return sui_df

suicide_df = exclude_header(suicide_df)

suicide_df = suicide_df[suicide_df['Sex'] == 'Both sexes']

def remove_confidence_interval(complex_val):
    return complex_val.split(' ')[0]

for year_col in range(2000, 2020):
    suicide_df[str(year_col)] = suicide_df[str(year_col)].map(
        lambda z: remove_confidence_interval(z)
    ).astype(float)

suicide_df.rename({
    'Country': 'country',
    last_year_of_observation: res_colname
}, axis=1, inplace=True)

suicide_df[['country', res_colname]].to_csv(res_filepath, index=None)