import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [500, 500] + [18.848298, -96.917510],
    columns=['lat', 'lon'])

st.map(map_data)
st.dataframe(map_data)
