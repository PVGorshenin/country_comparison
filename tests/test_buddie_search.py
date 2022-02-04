import pandas as pd
from country_comparison.search_a_buddie import search_a_buddie
from pytest import fixture, mark


@fixture
def get_config():
    return {'country_to_highlight': 'some_country'}

@fixture
def get_standings():
    return pd.DataFrame({'country': ['some_country',
                                     'country1',
                                     'country2',
                                     'country3'],
                         'gdp_ppp': [100, 0, 50, 110],
                         'some_val': [100, 20, 70, 120],
                         'anoth_val': [-100, -10, -40, -150]})


def test_serch_a_buddie(get_config, get_standings):
    res = search_a_buddie(get_standings, get_config)
    assert res == 'country3'