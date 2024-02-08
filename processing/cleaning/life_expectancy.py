import pandas as pd

input_filepath = '../../data/input/2022/life_expectancy.csv'
output_filepath = '../../data/intermediate/2023/life_expectancy.csv'

last_year_of_observation = 2019

exp_df = pd.read_csv(input_filepath)

redundunt_info_start_col_ix = 3
exp_df = exp_df.iloc[:, :redundunt_info_start_col_ix]

def exclude_header(exp_df):
    exp_df.columns = exp_df.iloc[0]
    exp_df = exp_df.iloc[1:]
    return exp_df

exp_df = exclude_header(exp_df)

exp_df['Year'] = exp_df['Year'].astype(int)
exp_df = exp_df[exp_df['Year']==last_year_of_observation]

exp_df.columns = [col.lower() for col in exp_df.columns]

exp_df.rename({'both sexes': 'life_expectancy'}, axis=1, inplace=True)

exp_df.to_csv(output_filepath, index=None)