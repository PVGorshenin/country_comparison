import pandas as pd


input_filepath = '../../data/input/2023/API_SI.POV.GINI_DS2_en_csv_v2_6555935.csv'
output_filepath = '../../data/intermediate/2023/gini_cleaned.csv'

gini_df = pd.read_csv(input_filepath)

last_year_of_observation = 2022
gini_df['gini'] = gini_df[str(last_year_of_observation)].values

def fill_nans(gini_df, last_year_of_observation):
    n_years_to_go_past = 10
    for i_shift in range(1, n_years_to_go_past+1):
        is_now_null = gini_df['gini'].isnull()
        gini_df.loc[is_now_null, 'gini'] = gini_df.loc[is_now_null, str(last_year_of_observation-i_shift)].values

    return gini_df

gini_df = fill_nans(gini_df, last_year_of_observation)

gini_df.rename(
    {'Country Name': 'country'},
    axis=1,
    inplace=True
)

gini_df.loc[~gini_df['gini'].isnull(), ['country', 'gini']].to_csv(output_filepath, index=None)

