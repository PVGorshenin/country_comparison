import numpy as np
from country_comparison.compare import default_minmax_scaling
from pytest import fixture, mark


@fixture
def range10():
    return np.array(range(11)).reshape(-1, 1)


@fixture
def range100():
    return np.array(range(101)).reshape(-1, 1)


@mark.parametrize('lq_clip, rq_clip, answer', [(0, 1, 10),
                                       (.01, .99, 9.1836735)])
def test_scaling_short_inp(range10, lq_clip, rq_clip, answer):
    answ = default_minmax_scaling(range10, lq_clip, rq_clip)
    assert np.isclose(answ[1], answer)


@mark.parametrize('lq_clip, rq_clip, answer', [(0, 1, 1),
                                       (.01, .99, 0)])
def test_scaling_short_inp(range100, lq_clip, rq_clip, answer):
    answ = default_minmax_scaling(range100, lq_clip, rq_clip)
    assert np.isclose(answ[1], answer)