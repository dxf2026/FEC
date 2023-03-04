import streamlit as st
from PIL import Image

st.set_page_config(page_title="Divinity", page_icon="logo.png", layout="wide")

menu = ["Home","About"]
choice = st.sidevar.selectbox("Menu",menu)
with st.container():
  st.subheader("I Love Big Black Men :wave:")
  st.title("I like dudes")
  "I am baller"
  st.write("[Like men too?](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
  "Zangbus"
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("What I Do")
    "Ballingus"
  with right_column:
    st.header("man liker")
    "Gugga"
