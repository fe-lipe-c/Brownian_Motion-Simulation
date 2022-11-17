"""Notebook for the Brownian motion simulations."""

import numpy as np
import pandas as pd
import altair as alt

from brownian_motion import BM_increment, BM_interpolation, to_df

# Brownian path with independent increments

bm_list = BM_increment(dt=0.1, N=3000, seed=102)
df_bm = to_df(bm_list)

chart_bm = (
    alt.Chart(df_bm, title="Brownian motion")
    .mark_line()
    .encode(
        alt.X("index", title="Time"),
        alt.Y("bm", title="B"),
    )
    .properties(width=800, height=400)
)
chart_bm.save("bm_II.html")

# Interpolation of a given BM path

seed = 10
N = 10
dt = 1
M = 5

bm_list = []
time_list = []
df_bm = []
chart_bm = []


for i in range(M):
    if i == 0:
        bm_list.append(BM_increment(dt, N, seed))
        time_list.append([i for i in range(len(bm_list[0]))])
    else:
        bm_interp, time_index = BM_interpolation(bm_list[-1], time_list[-1])
        bm_list.append(bm_interp)
        time_list.append(time_index)

    df_temp = to_df(bm_list[-1])
    df_temp["time"] = time_list[-1]
    df_bm.append(df_temp)

    chart_ = (
        alt.Chart(df_bm[-1], title="Brownian motion - interpolation {}".format(i))
        .mark_line()
        .encode(
            alt.X("time", title="Time"),
            alt.Y("bm", title="B"),
        )
    )
    chart_bm.append(chart_)


chart_total = chart_bm[0] | chart_bm[1] | chart_bm[2] | chart_bm[3] | chart_bm[4]
chart_total.properties(width=200, height=400)

chart_total.save("BM_interpolation.html")
