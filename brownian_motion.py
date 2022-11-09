"""Different methods to simulate a brownian motion."""

import numpy as np
import pandas as pd
import altair as alt


def to_df(bm_list):
    """Convert a list of brownian motions to a dataframe."""
    df = pd.DataFrame(bm_list, columns=["bm"])
    df["index"] = df.index
    return df


def brownian_motion_II(dt, N, seed=1):
    """Brownian motion using independent (equal) increments."""
    np.random.seed(seed)
    y = np.random.normal(loc=0, scale=dt, size=N)
    b = np.cumsum(y)
    return b
