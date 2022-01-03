import numpy as np
from sklearn.preprocessing import MinMaxScaler


def default_minmax_scaling(feature_arr: np.array, left_quantile_clip: float = 0,
                           right_quantile_clip: float = 1) -> np.array:

    feature_arr = np.clip(feature_arr, np.quantile(feature_arr, left_quantile_clip),
                          np.quantile(feature_arr, right_quantile_clip))
    res_arr = MinMaxScaler().fit_transform(feature_arr)
    return res_arr


