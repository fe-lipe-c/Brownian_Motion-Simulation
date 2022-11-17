"""Notebook for the Brownian motion simulations."""

import numpy as np
import pandas as pd
import altair as alt

from brownian_motion import BM_increment, to_df

bm_list = BM_increment(dt=0.1, N=3000, seed=102)
df_bm = to_df(bm_list)

chart_bm = (
    alt.Chart(df_bm, title="Brownian motion")
    .mark_line()
    .encode(
        alt.X("index", title="Time"),
        alt.Y("bm", title="B"),
    )
    .properties(width=600, height=300)
)
chart_bm.save("bm_II.html")
