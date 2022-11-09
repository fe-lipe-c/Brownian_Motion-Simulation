"""Notebook for the Brownian motion simulations."""

import numpy as np
import pandas as pd

from brownian_motion import brownian_motion_II, to_df

bm_list = brownian_motion_II(0.1, 3000, seed=102)
df_bm = to_df(bm_list)

chart_bm = (
    alt.Chart(df_bm)
    .mark_line()
    .encode(
        alt.X("index"),
        alt.Y("bm"),
    )
)
chart_bm.save("bm_II.html")
