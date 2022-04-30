from shotchart import draw_plotly_court, filt_hexbins


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


import streamlit as st

st.title('NBA data analytics')

# functions:
filt_hexbins()


# fig
fig = go.Figure()
### draw_plotly_court(go.Scatter())


st.plotly_chart(fig, use_container_width=True)

# for streamlit need to create a req.text file!