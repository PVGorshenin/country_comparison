import numpy as np
import pandas as pd
import streamlit as st
from country_comparison.compare import default_minmax_scaling
from country_comparison.plots.plot_rankings import plot_rankings_hor, highlight_buddie
from country_comparison.reads.read_config import read_config, update_config_from_slider
from country_comparison.search_a_buddie import search_a_buddie
from definitions import get_root


if __name__ == "__main__":
    config = read_config()

    df = pd.read_csv(config['match_table_filepath'])
    res_arr = np.zeros((df.shape[0], 1))

    config['root'] = get_root()
    config = update_config_from_slider(config)

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
    df = df[['country', 'unscaled_score', 'final_score'] + config['features_to_use']]
    df.to_csv(config['res_filepath'], index=None)

    df = df.sort_values(by='final_score', ascending=True).reset_index(drop=True)
    fig, ax = plot_rankings_hor(df, config)

    if config['is_buddie_highlight']:
        country_buddie = search_a_buddie(df, config)
        highlight_buddie(df, fig, ax, config, country_buddie)

    st.pyplot(fig)


