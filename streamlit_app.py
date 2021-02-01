from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.title('Recommender System using Pairwise Preference')
st.text('Here I will recommend songs to you based on your preference of a couple of songs.')
uploaded_file = st.file_uploader("Choose an image", ["jpg","jpeg","png"])
