import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from os import path


def _highlight_basic_country(standings_df, config, ax):
    pos = standings_df.index[standings_df['country'] == config['country_to_highlight']][0]
    red_color = '#aa3333'
    ax.patches[pos].set_facecolor(red_color)
    return ax


def highlight_buddie(standings_df, fig, ax, config, country_buddie):
    pos = standings_df.index[standings_df['country'] == country_buddie][0]
    magenda_color = '#ff00ff'
    ax.patches[pos].set_facecolor(magenda_color)
    plt.savefig(path.join(config['root'], config['res_filepath'].replace('csv', 'jpeg')))
    st.pyplot(fig)


def plot_rankings_hor(standings_df: pd.DataFrame, config):
    ind = np.arange(standings_df.shape[0])

    standings_df = standings_df[['country', 'final_score']]

    fig, ax = plt.subplots(figsize=(12, 18))

    rects = ax.barh(ind, standings_df['final_score'].values, color='y')

    ax.set_yticks(ind)
    ax.set_yticklabels(standings_df['country'].values, rotation='horizontal')
    ax.set_xlabel("final_score")
    ax.set_title("final_score")

    ax = _highlight_basic_country(standings_df, config, ax)

    plt.savefig(path.join(config['root'], config['res_filepath'].replace('csv', 'jpeg')))
    st.pyplot(fig)

    return fig, ax
