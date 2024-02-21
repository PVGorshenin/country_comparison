import pandas as pd

input_filepath = '../../data/input/2022/life_expectancy.csv'
output_filepath = '../../data/intermediate/2023/life_expectancy.csv'

last_year_of_observation = 2019
res_colname = 'life_expectancy'

expectancy_df = pd.read_csv(input_filepath)

redundunt_info_start_col_ix = 3
expectancy_df = expectancy_df.iloc[:, :redundunt_info_start_col_ix]

def exclude_header(exp_df):
    exp_df.columns = exp_df.iloc[0]
    exp_df = exp_df.iloc[1:]
    return exp_df

expectancy_df = exclude_header(expectancy_df)

expectancy_df['Year'] = expectancy_df['Year'].astype(int)
expectancy_df = expectancy_df[expectancy_df['Year'] == last_year_of_observation]

expectancy_df.columns = [col.lower() for col in expectancy_df.columns]

expectancy_df.rename({'both sexes': res_colname}, axis=1, inplace=True)

expectancy_df[['country', res_colname]].to_csv(output_filepath, index=None)