import pandas as pd


input_filepath = '../../data/input/2023/world_press_index.csv'
res_filepath = '../../data/intermediate/2023/press_cleaned.csv'

press_df = pd.read_csv(input_filepath, sep=';')

press_df.rename(columns={
    'Country_EN': 'country',
    'Score': 'press_freedom'
}, inplace=True)


press_df[['country', 'press_freedom']].to_csv(res_filepath, index=False)