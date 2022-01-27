import numpy as np
import pandas as pd
from country_comparison.compare import default_minmax_scaling
from country_comparison.plots import plot_rankings_hor
from country_comparison.reads import read_config

config = read_config()

df = pd.read_csv(config['match_table_filepath'])
res_arr = np.zeros((df.shape[0], 1))

for feature in config['features_to_use']:
    clips = {}
    if feature in config['feature_clips']:
        clips = config['feature_clips'][feature]

    feature_arr = df[feature].values.reshape(-1, 1)
    curr_score = default_minmax_scaling(feature_arr, **clips) * config['feature_weights'][feature]
    df[feature] = curr_score
    res_arr += curr_score

df['unscaled_score'] = res_arr
df['final_score'] = default_minmax_scaling(res_arr)
df[['country', 'unscaled_score', 'final_score'] +
   config['features_to_use']].to_csv(config['res_filepath'], index=None)

plot_rankings_hor(df, config)