import pandas as pd


input_filepath = '../../data/input/2023/DataForFigure2.1WHR2023.xls'
output_filepath = '../../data/intermediate/2023/happiness_cleaned.csv'

happy_df = pd.read_excel(input_filepath)

happy_df.rename({
    'Ladder score': 'happiness',
    'Country name': 'country',
}, inplace=True, axis=1)

cols_to_save = ['country', 'happiness']

happy_df = happy_df[cols_to_save]
#taken from different years
happy_df.loc[happy_df.shape[0]+1] = ['Azerbaijan', 5.17]
happy_df.loc[happy_df.shape[0]+1] = ['Belarus', 5.53]
happy_df.loc[happy_df.shape[0]+1] = ['Kuwait', 6.1]
happy_df.loc[happy_df.shape[0]+1] = ['Oman', 6.683]
happy_df.loc[happy_df.shape[0]+1] = ['Qatar', 6.74]

happy_df[cols_to_save].to_csv(
    output_filepath,
    index=None)