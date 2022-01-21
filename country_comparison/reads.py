from definitions import get_root
import yaml

def read_config():
    with open(get_root()+'/config.yaml') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)