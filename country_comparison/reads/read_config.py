from definitions import get_root
import streamlit as st
import yaml

def read_config():
    with open(get_root()+'/config.yaml') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)


def update_config_from_slider(config):
    for feature in config['features_to_use']:
        abs_min = 0
        abs_max = 10
        direction = 1
        if config['feature_weights'][feature] < 0:
            direction = -1
        abs_score = st.sidebar.slider(feature,
                                      min_value=abs_min,
                                      max_value=abs_max,
                                      value=int(abs(config['feature_weights'][feature])*10),
                                      step=1)
        config['feature_weights'][feature] = abs_score / abs_max * direction
    return config