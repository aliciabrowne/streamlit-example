from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.title('Recommender System using Pairwise Preference')
st.text('Here I will recommend songs to you based on your preference of a couple of songs.')
uploaded_file = st.file_uploader("Choose an image", ["jpg","jpeg","png"])

if use_default_image:
    opencv_image = cv2.imread('musicrecsys.png')
    
if opencv_image is not None:
  st.subheader('Use the sliders on the left to position the start and end points')
  start_x = st.sidebar.slider("Start X", value= 24 if use_default_image  else 50, min_value=0, max_value=opencv_image.shape[1], key='sx')
  start_y = st.sidebar.slider("Start Y", value= 332 if use_default_image  else 100, min_value=0, max_value=opencv_image.shape[0], key='sy')
  finish_x = st.sidebar.slider("Finish X", value= 309 if use_default_image  else 100, min_value=0, max_value=opencv_image.shape[1], key='fx')
  finish_y = st.sidebar.slider("Finish Y", value= 330 if use_default_image  else 100, min_value=0, max_value=opencv_image.shape[0], key='fy')
  marked_image = opencv_image.copy()
  circle_thickness=(marked_image.shape[0]+marked_image.shape[0])//2//100 #circle thickness based on img size
  cv2.circle(marked_image, (start_x, start_y), circle_thickness, (0,255,0),-1)
  cv2.circle(marked_image, (finish_x, finish_y), circle_thickness, (255,0,0),-1)
  st.image(marked_image, channels="RGB", width=800)
