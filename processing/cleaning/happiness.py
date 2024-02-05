import pandas as pd


input_filepath = '../../data/input/2023/DataForFigure2.1WHR2023.xls'
output_filepath = '../../data/intermediate/2023/happiness_cleaned.csv'

happy_df = pd.read_excel(input_filepath)

happy_df.rename({
    'Ladder score': 'happiness',
    'Country name': 'country',
    'Perceptions of corruption': 'corruption'
}, inplace=True, axis=1)

cols_to_save = ['country', 'happiness']

happy_df[cols_to_save].to_csv(
    output_filepath,
    index=None)