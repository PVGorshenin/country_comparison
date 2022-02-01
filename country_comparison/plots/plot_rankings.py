import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from definitions import get_root
from os import path


def plot_rankings_hor(standings_df: pd.DataFrame, config):
    ind = np.arange(standings_df.shape[0])

    root = get_root()

    standings_df = standings_df[['country', 'final_score']].sort_values(by='final_score',
                                                                        ascending=True).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(12, 18))

    rects = ax.barh(ind, standings_df['final_score'].values, color='y')

    ax.set_yticks(ind)
    ax.set_yticklabels(standings_df['country'].values, rotation='horizontal')
    ax.set_xlabel("final_score")
    ax.set_title("final_score")

    pos = standings_df.index[standings_df['country'] == config['country_to_highlight']][0]
    red_color = '#aa3333'
    ax.patches[pos].set_facecolor(red_color)

    plt.savefig(path.join(root, config['res_filepath'].replace('csv', 'jpeg')))

    st.pyplot(fig)