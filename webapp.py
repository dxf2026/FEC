import streamlit as st
from PIL import Image

st.set_page_config(page_title="Divinity", page_icon="logo.png", layout="wide")

st.header("Upload Sound File")
video_file = st.file_uploader("", type=["mp4"])
l_column, r_column = st.columns(2)
with l_column:
  if st.button("Calculate emotions"):
    with st.container():
      st.subheader("I Love Big Black Men :wave:")
      st.title("I like dudes")
      "I am baller"
      st.write("[Like men too?](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with r_column:
  if st.button("Calculate tone"):
    st.write("Grippy")
    with st.container():
      "Zangbus"
      left_column, right_column = st.columns(2)
    with left_column:
      st.header("What I Do")
      "Ballingus"
    with right_column:
      st.header("man liker")
      "Gugga"
