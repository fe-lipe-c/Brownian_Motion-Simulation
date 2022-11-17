"""Different methods to simulate a brownian motion."""

import numpy as np
import pandas as pd
import altair as alt


def to_df(bm_list):
    """Convert a list of brownian motions to a dataframe."""
    df = pd.DataFrame(bm_list, columns=["bm"])
    df["index"] = df.index
    return df


def BM_increment(dt, N, seed=1):
    """Brownian motion using independent (equal) increments."""
    np.random.seed(seed)
    y = np.random.normal(loc=0, scale=dt, size=N)
    b = np.cumsum(y)
    b = np.insert(b, 0, 0)
    return b


def BM_interpolation(bm_path, time_index, alpha=0.5):
    """Brownian motion through interpolation of a given path.

    alpha: parameter for the convex sum between s_0 and s_1 to get s.
    """

    interp_path = []
    new_time_index = []

    for s_0 in time_index[:-1]:

        s_1 = time_index[time_index.index(s_0) + 1]
        s = alpha * s_0 + (1 - alpha) * s_1
        B_0 = bm_path[time_index.index(s_0)]
        B_1 = bm_path[time_index.index(s_1)]

        bs_mean = ((s_1 - s) * B_0 + (s - s_0) * B_1) / (s_1 - s_0)
        bs_var = (s_1 - s) * (s - s_0) / (s_1 - s_0)

        B_s = np.random.normal(loc=bs_mean, scale=bs_var, size=1)
        interp_path.extend([B_0, B_s[0]])
        new_time_index.extend([s_0, s])

    interp_path.append(bm_path[-1])
    new_time_index.append(time_index[-1])

    return interp_path, new_time_index
