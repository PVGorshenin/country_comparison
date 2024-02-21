import json
import pandas as pd


input_filepath = '../../data/intermediate/2023/numbeo.csv'
output_filepath = '../../data/intermediate/2023/numbeo_renamed.csv'


df = pd.read_csv(input_filepath)

numbeo_src_cols = df.columns
numbeo_cols = [col.lower().replace(' ', '_') for col in numbeo_src_cols]

numbeo_cols = ['country'] + ['_'.join(['numbeo', col]) for col in numbeo_cols[1:]]

rename_dct = {}
for feature in zip(numbeo_src_cols, numbeo_cols):
    rename_dct[feature[0]] = feature[1]

df.rename(rename_dct, axis=1, inplace=True)

df.to_csv(output_filepath, index=None)


