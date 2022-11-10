"""Different methods to simulate a brownian motion."""

import numpy as np
import pandas as pd
import altair as alt


def to_df(bm_list):
    """Convert a list of brownian motions to a dataframe."""
    df = pd.DataFrame(bm_list, columns=["bm"])
    df["index"] = df.index
    return df


def brownian_motion_increment(dt, N, seed=1):
    """Brownian motion using independent (equal) increments."""
    np.random.seed(seed)
    y = np.random.normal(loc=0, scale=dt, size=N)
    b = np.cumsum(y)
    return b


def brownian_motion_interpolation(bm_path):
    """Brownian motion through interpolation of a given path."""
    for i in range(len(bm_path)):
        n_mean = ()
        bs = np.random.normal(loc=)
